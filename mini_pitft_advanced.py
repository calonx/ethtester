# SPDX-License-Identifier: MIT

"""
Advanced Mini PiTFT demo with rotating colors and dynamic text
"""

import board
import displayio
import terminalio
import time
from adafruit_display_text import label
from fourwire import FourWire

from adafruit_st7789 import ST7789

displayio.release_displays()

spi = board.SPI()
display_bus = FourWire(spi, command=board.D25, chip_select=board.CE0)

display = ST7789(
    display_bus,
    rotation=90,
    width=240,
    height=135,
    rowstart=40,
    colstart=53
)

splash = displayio.Group()
display.root_group = splash

# Create a dynamic text label
text_area = label.Label(
    terminalio.FONT,
    text="Mini PiTFT",
    color=0xFFFF00,
    scale=2,
    # anchor_point=(0.5, 0.5),
    # anchored_position=(display.width // 2, display.height // 2)
)
splash.append(text_area)

# Color palette for cycling
colors = [0xFF0000, 0x00FF00, 0x0000FF, 0xFFFF00, 0xFF00FF, 0x00FFFF]
color_index = 0

print("Running advanced demo. Press Ctrl+C to exit.")
try:
    while True:
        # Cycle through colors
        text_area.color = colors[color_index % len(colors)]
        color_index += 1
        time.sleep(0.5)
except KeyboardInterrupt:
    print("\nExiting...")