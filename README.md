# Adafruit Mini PiTFT Demo

This project contains demo scripts for the Adafruit Mini PiTFT 1.14" (240x135) display.

## Setup Instructions

### Hardware Requirements
- Adafruit Mini PiTFT 1.14" (240x135) display
- Raspberry Pi with GPIO pins
- SPI connection

### Software Installation

**For Raspberry Pi with Blinka (recommended for beginners):**

```bash
# Update system
sudo apt-get update
sudo apt-get upgrade

# Install Blinka and dependencies
pip3 install --upgrade adafruit-python-shell
wget https://raw.githubusercontent.com/adafruit/Raspberry-Pi-Installer-Scripts/master/raspi-blinka.py
sudo python3 raspi-blinka.py

# Install required libraries
pip3 install -r requirements.txt
```

**Wiring (Raspberry Pi GPIO):**
- Display CS → GPIO CE0 (Pin 24)
- Display DC → GPIO D25 (Pin 22)
- Display SDA (MOSI) → GPIO SDA (Pin 10)
- Display SCK → GPIO SCK (Pin 11)
- Display GND → GND
- Display VCC → 3.3V

## Running the Demos

### Simple Demo
Displays static graphics and text.

```bash
python3 mini_pitft_demo.py
```

### Advanced Demo
Displays dynamic text with color cycling.

```bash
python3 mini_pitft_advanced.py
```

Press Ctrl+C to exit any demo.

## Key Libraries & References

| Library | Purpose | Install |
|---------|---------|---------|
| `adafruit-circuitpython-st7789` | ST7789 display driver | `pip3 install` |
| `adafruit-circuitpython-display-text` | Text rendering | `pip3 install` |
| `Blinka` | CircuitPython compatibility layer | `sudo python3 raspi-blinka.py` |

## Quick Tips

- **Rotation**: Use `rotation=90` or `rotation=270` for landscape
- **Colors**: Use hex format `0xRRGGBB` (e.g., `0xFF0000` = red)
- **Text Scaling**: Use `scale` parameter to resize fonts (multiply default size)
- **Position**: Use `anchor_point=(0.5, 0.5)` to center text on coordinates
- **Brightness**: Control with `display.brightness = 0.5` (0.0-1.0)

The Mini PiTFT integrates seamlessly with CircuitPython via Blinka, making it ideal for rapid prototyping with clear, concise APIs for graphics and text rendering.