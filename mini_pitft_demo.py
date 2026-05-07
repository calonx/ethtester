# SPDX-License-Identifier: MIT

"""
Mini PiTFT demo - displays graphics and text
"""

import board
import displayio
import terminalio
from adafruit_display_text import label
from fourwire import FourWire

from adafruit_st7789 import ST7789

# Configuration
BORDER = 15
FONTSCALE = 2
BACKGROUND_COLOR = 0x00FF00  # Bright Green
FOREGROUND_COLOR = 0xAA0088  # Purple
TEXT_COLOR = 0xFFFF00  # Yellow

# Release any resources currently in use for the displays
displayio.release_displays()

# Initialize SPI and display
spi = board.SPI()
tft_cs = board.CE0
tft_dc = board.D25

display_bus = FourWire(spi, command=tft_dc, chip_select=tft_cs)

# Initialize display (240x135 resolution)
display = ST7789(
    display_bus,
    rotation=90,
    width=240,
    height=135,
    rowstart=40,
    colstart=53
)

# Create display group (container for all visual elements)
splash = displayio.Group()
display.root_group = splash

# Draw background rectangle
color_bitmap = displayio.Bitmap(display.width, display.height, 1)
color_palette = displayio.Palette(1)
color_palette[0] = BACKGROUND_COLOR

bg_sprite = displayio.TileGrid(
    color_bitmap,
    pixel_shader=color_palette,
    x=0,
    y=0
)
splash.append(bg_sprite)

# Draw inner rectangle
inner_bitmap = displayio.Bitmap(
    display.width - (BORDER * 2),
    display.height - (BORDER * 2),
    1
)
inner_palette = displayio.Palette(1)
inner_palette[0] = FOREGROUND_COLOR

inner_sprite = displayio.TileGrid(
    inner_bitmap,
    pixel_shader=inner_palette,
    x=BORDER,
    y=BORDER
)
splash.append(inner_sprite)

# Draw text label
text = "Hello World!"
text_area = label.Label(terminalio.FONT, text=text, color=TEXT_COLOR)

text_width = text_area.bounding_box[2] * FONTSCALE
text_group = displayio.Group(
    scale=FONTSCALE,
    x=display.width // 2 - text_width // 2,
    y=display.height // 2,
)
text_group.append(text_area)
splash.append(text_group)

# Keep display active
print("Display initialized! Press Ctrl+C to exit.")
try:
    while True:
        pass
except KeyboardInterrupt:
    print("\nExiting...")