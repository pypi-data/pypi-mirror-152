import logging

import intelhex
from serial import Serial

from mcbootflash.error import (
    BootloaderError,
    FlashEraseError,
    FlashWriteError,
    ChecksumError,
)
from mcbootflash.protocol import (
    FLASH_UNLOCK_KEY,
    BootCommand,
    BootResponseCode,
    CommandPacket,
    ResponsePacket,
    VersionResponsePacket,
    MemoryRangePacket,
)

logger = logging.getLogger(__name__)


class BootloaderConnection(Serial):
    """Communication interface to device running MCC 16-bit bootloader."""

    def flash(self, hexfile: str):
        """Flash application firmware.

        Parameters
        ----------
        hexfile : str
            An Intel HEX-file containing application firmware.

        Raises
        ------
        FlashEraseError
        FlashWriteError
        ChecksumError
        BootloaderError
        """
        self.hexfile = intelhex.IntelHex(hexfile)
        (
            self.version,
            self.max_packet_length,
            self.device_id,
            self.erase_size,
            self.write_size,
        ) = self.read_version()
        legal_range = self._get_memory_address_range()

        self._erase_flash(*legal_range, self.erase_size)

        for segment in self.hexfile.segments():
            # Since the MCU uses 16-bit instructions, each "address" in the
            # (8-bit) hex file is actually only half an address. Therefore, we
            # need to divide by two to get the actual address.
            if (segment[0] // 2 in range(*legal_range)) and (
                segment[1] // 2 in range(*legal_range)
            ):
                logger.info(
                    "Flashing segment "
                    f"{self.hexfile.segments().index(segment)}, "
                    f"[{segment[0]:#08x}:{segment[1]:#08x}]."
                )
                self._flash_segment(segment)
            else:
                logger.info(
                    f"Segment {self.hexfile.segments().index(segment)} "
                    "ignored; not in legal range "
                    f"([{segment[0]:#08x}:{segment[1]:#08x}] vs. "
                    f"[{legal_range[0]:#08x}:{legal_range[1]:#08x}])."
                )

        self._self_verify()

    def _flash_segment(self, segment):
        chunk_size = self.max_packet_length - CommandPacket.size
        chunk_size -= chunk_size % self.write_size
        chunk_size //= 2
        total_bytes = segment[1] - segment[0]
        written_bytes = 0
        # If (segment[1] - segment[0]) % write_size != 0, writing the final
        # chunk will fail. However, I have seen no example where it's not,
        # so not adding code to check for now (YAGNI).
        for addr in range(segment[0] // 2, segment[1] // 2, chunk_size):
            chunk = self.hexfile[addr * 2 : (addr + chunk_size) * 2]
            self._write_flash(addr, chunk.tobinstr())
            self._checksum(addr, len(chunk))
            written_bytes += len(chunk)
            logger.info(
                f"{written_bytes} bytes written of {total_bytes} "
                f"({written_bytes / total_bytes * 100:.2f}%)."
            )

    def read_version(self) -> tuple:
        """Read bootloader version and some other useful information.

        Returns
        -------
        version : int
        max_packet_length : int
            The maximum size of a single packet sent to the bootloader,
            including both the command and associated data.
        device_id : int
        erase_size : int
            Flash page size. When erasing flash memory, the number of bytes to
            be erased must align with a flash page.
        write_size : int
            Write block size. When writing to flash, the number of bytes to be
            written must align with a write block.
        """
        read_version_command = CommandPacket(
            command=BootCommand.READ_VERSION.value
        )
        self.write(bytes(read_version_command))
        read_version_response = VersionResponsePacket.from_serial(self)
        return (
            read_version_response.version,
            read_version_response.max_packet_pength,
            read_version_response.device_id,
            read_version_response.erase_size,
            read_version_response.write_size,
        )

    def _get_memory_address_range(self) -> tuple:
        mem_range_command = CommandPacket(
            command=BootCommand.GET_MEMORY_ADDRESS_RANGE.value
        )
        self.write(bytes(mem_range_command))
        mem_range_response = MemoryRangePacket.from_serial(self)

        if mem_range_response.success != BootResponseCode.SUCCESS.value:
            logger.error(
                "Failed to get program memory range: "
                f"{BootResponseCode(mem_range_response.success).name}"
            )
            raise BootloaderError(
                BootResponseCode(mem_range_response.success).name
            )
        else:
            logger.info(
                "Got program memory range: "
                f"{mem_range_response.program_start:#08x}:"
                f"{mem_range_response.program_end:#08x}."
            )

        return mem_range_response.program_start, mem_range_response.program_end

    def _erase_flash(
        self, start_address: int, end_address: int, erase_size: int
    ):
        erase_flash_command = CommandPacket(
            command=BootCommand.ERASE_FLASH.value,
            data_length=int((end_address - start_address) / erase_size),
            unlock_sequence=FLASH_UNLOCK_KEY,
            address=start_address,
        )
        self.write(bytes(erase_flash_command))
        erase_flash_response = ResponsePacket.from_serial(self)

        if erase_flash_response.success != BootResponseCode.SUCCESS.value:
            logger.error(
                "Flash erase failed: "
                f"{BootResponseCode(erase_flash_response.success).name}."
            )
            raise FlashEraseError(
                BootResponseCode(erase_flash_response.success).name
            )
        else:
            logger.info(
                f"Erased flash area {start_address:#08x}:{end_address:#08x}."
            )

    def _write_flash(self, address: int, data: bytes):
        write_flash_command = CommandPacket(
            command=BootCommand.WRITE_FLASH.value,
            data_length=len(data),
            unlock_sequence=FLASH_UNLOCK_KEY,
            address=address,
        )
        self.write(bytes(write_flash_command) + data)
        write_flash_response = ResponsePacket.from_serial(self)

        if write_flash_response.success != BootResponseCode.SUCCESS.value:
            logger.error(
                f"Failed to write {len(bytes)} bytes to {address:#08x}: "
                f"{BootResponseCode(write_flash_response.success).name}."
            )
            raise FlashWriteError(
                BootResponseCode(write_flash_response.success).name
            )
        else:
            logger.debug(f"Wrote {len(data)} bytes to {address:#08x}.")

    def _self_verify(self):
        self_verify_command = CommandPacket(
            command=BootCommand.SELF_VERIFY.value
        )
        self.write(bytes(self_verify_command))
        self_verify_response = ResponsePacket.from_serial(self)

        if self_verify_response.success != BootResponseCode.SUCCESS.value:
            logger.error(
                "Self verify failed: "
                f"{BootResponseCode(self_verify_response.success).name}."
            )
            raise BootloaderError(
                BootResponseCode(self_verify_response.success).name
            )
        else:
            logger.info("Self verify OK.")

    def _get_checksum(self, address: int, length: int):
        calculcate_checksum_command = CommandPacket(
            command=BootCommand.CALC_CHECKSUM.value,
            data_length=length,
            address=address,
        )
        self.write(bytes(calculcate_checksum_command))
        calculate_checksum_response = ResponsePacket.from_serial(self)

        if (
            calculate_checksum_response.success
            != BootResponseCode.SUCCESS.value
        ):
            logger.error(
                "Failed to get checksum: "
                f"{BootResponseCode(calculate_checksum_response.success).name}"
            )
            raise BootloaderError(
                BootResponseCode(calculate_checksum_response.success).name
            )

        checksum = int.from_bytes(self.read(2), byteorder="little")

        return checksum

    def _calculate_checksum(self, address: int, length: int):
        checksum = 0
        for i in range(address, address + length, 4):
            data = self.hexfile[i : i + 4].tobinstr()
            checksum += int.from_bytes(data, byteorder="little") & 0xFFFF
            checksum += (int.from_bytes(data, byteorder="little") >> 16) & 0xFF
        return checksum & 0xFFFF

    def _checksum(self, address: int, length: int):
        """Compare checksums calculated locally and onboard device.

        Parameters
        ----------
        address : int
            Address from which to start checksum.
        length : int
            Number of bytes to checksum.
        """
        checksum1 = self._calculate_checksum(address * 2, length)
        checksum2 = self._get_checksum(address, length)
        if checksum1 != checksum2:
            logger.error(f"Checksum mismatch: {checksum1} != {checksum2}.")
            raise ChecksumError
        else:
            logger.debug(f"Checksum OK: {checksum1}.")
