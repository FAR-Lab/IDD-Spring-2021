import board
import busio
import adafruit_apds9960.apds9960
import time

import digitalio
from PIL import Image, ImageDraw, ImageFont
import adafruit_rgb_display.st7789 as st7789

print('hello')

# # Configuration for CS and DC pins (these are FeatherWing defaults on M0/M4):
# cs_pin = digitalio.DigitalInOut(board.CE0)
# dc_pin = digitalio.DigitalInOut(board.D25)
# reset_pin = None

# # Config for display baudrate (default max is 24mhz):
# BAUDRATE = 64000000

# backlight = digitalio.DigitalInOut(board.D22)
# backlight.switch_to_output()
# backlight.value = True

# # Setup SPI bus using hardware SPI:
# spi = board.SPI()

# # Create the ST7789 display:
# disp = st7789.ST7789(
#     spi,
#     cs=cs_pin,
#     dc=dc_pin,
#     rst=reset_pin,
#     baudrate=BAUDRATE,
#     width=135,
#     height=240,
#     x_offset=53,
#     y_offset=40,
# )

# height = disp.width  # we swap height/width to rotate it to landscape!
# width = disp.height
# image = Image.new("RGB", (width, height))
# draw = ImageDraw.Draw(image)

# draw.rectangle((0, 0, width, height), fill=(0, 255, 0))
# disp.image(image)

# i2c = busio.I2C(board.SCL, board.SDA)
# sensor = adafruit_apds9960.apds9960.APDS9960(i2c)

# sensor.enable_color = True

# while True:
# 	r, g, b, c = sensor.color_data
# 	color =list(map(lambda x: int(x* 255 / 65536) , [r,g,b]))
# 	print(f"Red: {r}, Green: {g}, Blue: {b}, Clear: {c}")
# 	time.sleep(.2)
# 	