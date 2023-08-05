# SPDX-FileCopyrightText: 2019 Dave Astels for Adafruit Industries
# SPDX-FileCopyrightText: 2022 Matt Land
#
# SPDX-License-Identifier: MIT

"""
`adafruit_bitmapsaver`
================================================================================

Save a displayio.Bitmap (and associated displayio.Palette) in a BMP file.
Make a screenshot (the contents of a displayio.Display) and save in a BMP file.


* Author(s): Dave Astels, Matt Land

Implementation Notes
--------------------

**Hardware:**


**Software and Dependencies:**

* Adafruit CircuitPython firmware for the supported boards:
  https://github.com/adafruit/circuitpython/releases

"""

# imports

import gc
import struct
import board
from displayio import Bitmap, Palette, Display

try:
    from typing import Tuple, Optional, Union
    from io import BufferedWriter
except ImportError:
    pass

__version__ = "0.0.0-auto.0"
__repo__ = "https://github.com/adafruit/Adafruit_CircuitPython_BitmapSaver.git"


def _write_bmp_header(output_file: BufferedWriter, filesize: int) -> None:
    output_file.write(bytes("BM", "ascii"))
    output_file.write(struct.pack("<I", filesize))
    output_file.write(b"\00\x00")
    output_file.write(b"\00\x00")
    output_file.write(struct.pack("<I", 54))


def _write_dib_header(output_file: BufferedWriter, width: int, height: int) -> None:
    output_file.write(struct.pack("<I", 40))
    output_file.write(struct.pack("<I", width))
    output_file.write(struct.pack("<I", height))
    output_file.write(struct.pack("<H", 1))
    output_file.write(struct.pack("<H", 24))
    for _ in range(24):
        output_file.write(b"\x00")


def _bytes_per_row(source_width: int) -> int:
    pixel_bytes = 3 * source_width
    padding_bytes = (4 - (pixel_bytes % 4)) % 4
    return pixel_bytes + padding_bytes


def _rotated_height_and_width(pixel_source: Union[Bitmap, Display]) -> Tuple[int, int]:
    # flip axis if the display is rotated
    if isinstance(pixel_source, Display) and (pixel_source.rotation % 180 != 0):
        return pixel_source.height, pixel_source.width
    return pixel_source.width, pixel_source.height


def _rgb565_to_bgr_tuple(color: int) -> Tuple[int, int, int]:
    blue = (color << 3) & 0x00F8  # extract each of the RGB triple into it's own byte
    green = (color >> 3) & 0x00FC
    red = (color >> 8) & 0x00F8
    return blue, green, red


# pylint:disable=too-many-locals
def _write_pixels(
    output_file: BufferedWriter,
    pixel_source: Union[Bitmap, Display],
    palette: Optional[Palette],
) -> None:
    saving_bitmap = isinstance(pixel_source, Bitmap)
    width, height = _rotated_height_and_width(pixel_source)
    row_buffer = bytearray(_bytes_per_row(width))
    result_buffer = False
    for y in range(height, 0, -1):
        buffer_index = 0
        if saving_bitmap:
            # pixel_source: Bitmap
            for x in range(width):
                pixel = pixel_source[x, y - 1]
                color = palette[pixel]  # handled by save_pixel's guardians
                for _ in range(3):
                    row_buffer[buffer_index] = color & 0xFF
                    color >>= 8
                    buffer_index += 1
        else:
            # pixel_source: Display
            result_buffer = bytearray(2048)
            data = pixel_source.fill_row(y - 1, result_buffer)
            for i in range(width):
                pixel565 = (data[i * 2] << 8) + data[i * 2 + 1]
                for b in _rgb565_to_bgr_tuple(pixel565):
                    row_buffer[buffer_index] = b & 0xFF
                    buffer_index += 1
        output_file.write(row_buffer)
        if result_buffer:
            for i in range(width * 2):
                result_buffer[i] = 0
        gc.collect()


# pylint:enable=too-many-locals


def save_pixels(
    file_or_filename: Union[str, BufferedWriter],
    pixel_source: Union[Display, Bitmap] = None,
    palette: Optional[Palette] = None,
) -> None:
    """Save pixels to a 24 bit per pixel BMP file.
    If pixel_source if a displayio.Bitmap, save it's pixels through palette.
    If it's a displayio.Display, a palette isn't required.

    :param file_or_filename: either the file to save to, or it's absolute name
    :param pixel_source: the Bitmap or Display to save
    :param palette: the Palette to use for looking up colors in the bitmap
    """
    if not pixel_source:
        if not hasattr(board, "DISPLAY"):
            raise ValueError("Second argument must be a Bitmap or Display")
        pixel_source = board.DISPLAY

    if isinstance(pixel_source, Bitmap):
        if not isinstance(palette, Palette):
            raise ValueError("Third argument must be a Palette for a Bitmap save")
    elif not isinstance(pixel_source, Display):
        raise ValueError("Second argument must be a Bitmap or Display")
    try:
        if isinstance(file_or_filename, str):
            output_file = open(  # pylint: disable=consider-using-with
                file_or_filename, "wb"
            )
        else:
            output_file = file_or_filename

        width, height = _rotated_height_and_width(pixel_source)
        filesize = 54 + height * _bytes_per_row(width)
        _write_bmp_header(output_file, filesize)
        _write_dib_header(output_file, width, height)
        _write_pixels(output_file, pixel_source, palette)
    except Exception as ex:
        raise ex
    else:
        output_file.close()
