import busio
import board
import time
from adafruit_bus_device.i2c_device import I2CDevice

# DEVICE_ADDRESS = 0x23  # device address of our button
# COMMAND_WRITE_ALL_LED_COLOR = 0x72

# i2c = busio.I2C(board.SCL, board.SDA)
# device = I2CDevice(i2c, DEVICE_ADDRESS)

# def write_register(dev, register, value, n_bytes=1):
#     # Write a wregister number and value
#     buf = bytearray(1 + n_bytes)
#     buf[0] = register
#     buf[1:] = value.to_bytes(n_bytes, 'little')
#     with dev:
#         dev.write(buf)

# def read_register(dev, register, n_bytes=1):
#     # write a register number then read back the value
#     reg = register.to_bytes(1, 'little')
#     buf = bytearray(n_bytes)
#     with dev:
#         dev.write_then_readinto(reg, buf)
#     return int.from_bytes(buf, 'little')

# # buf = bytearray(4)
# # buf[0] = COMMAND_WRITE_ALL_LED_COLOR
# # buf[1] = 0xff
# # buf[2] = 0xff
# # buf[3] = 0xff

# # with device:
# # 	device.write(buf)

# # buf = bytearray(1)
	
# # with device:
# # 	device.write()

# def write_register24(addr, value):
#         # Write a byte to the specified 8-bit register address
#         with device:
#             device.write(bytes([addr & 0xFF,
#                                 (value >> 16) & 0xFF,
#                                 (value >> 8) & 0xFF,
#                                 value & 0xFF]))
# write_register24(COMMAND_WRITE_ALL_LED_COLOR, (255 & 0xFF) << 16 |
# 												(0 & 0xFF) << 8 |
#                                					255 & 0xFF)


# SPDX-FileCopyrightText: 2017 Scott Shawcroft, written for Adafruit Industries
# SPDX-FileCopyrightText: Copyright (c) 2021 ilan mandel for Cornell Tech
#
# SPDX-License-Identifier: MIT
"""
`sparkfun_qwiic_led_stick_circuitpython`
================================================================================

CircuitPython librabry for the Sparkfun Qwiic LED Stick


* Author(s): ilan mandel

Implementation Notes
--------------------

**Hardware:**

.. todo:: Add links to any specific hardware product page(s), or category page(s). Use unordered list & hyperlink rST
   inline format: "* `Link Text <url>`_"

**Software and Dependencies:**

* Adafruit CircuitPython firmware for the supported boards:
  https://github.com/adafruit/circuitpython/releases

.. todo:: Uncomment or remove the Bus Device and/or the Register library dependencies based on the library's use of either.

# * Adafruit's Bus Device library: https://github.com/adafruit/Adafruit_CircuitPython_BusDevice
# * Adafruit's Register library: https://github.com/adafruit/Adafruit_CircuitPython_Register
"""

# imports

from adafruit_bus_device.i2c_device import I2CDevice

# Register addresses:
CHANGE_ADDRESS = 0xC7
CHANGE_LED_LENGTH = 0x70
WRITE_SINGLE_LED_COLOR = 0x71
WRITE_ALL_LED_COLOR = 0x72
WRITE_RED_ARRAY = 0x73
WRITE_GREEN_ARRAY = 0x74
WRITE_BLUE_ARRAY = 0x75
WRITE_SINGLE_LED_BRIGHTNESS = 0x76
WRITE_ALL_LED_BRIGHTNESS = 0x77
WRITE_ALL_LED_OFF = 0x78

_DEFAULT_ADDRESS = 0x23



class LED_Stick:
	"""I2C connected LED strip with addressable LEDs https://www.sparkfun.com/products/14783

	:param i2c_addr: I2C address of the button
	:type i2c_addr: int
	:param i2c_obj: initialized I2C object
	:type i2c_obj: adafruit_bus_device.i2c_device.I2CDevice

	"""
	__version__ = "0.0.0-auto.0"
	__repo__ = "https://github.com/FAR-Lab/CircuitPython_SparkFun_Qwiic_LED_Stick_CircuitPython.git"

	def __init__(self, i2c_obj, i2c_addr=_DEFAULT_ADDRESS):
		self.i2c = i2c_obj
		self.device = I2CDevice(i2c_obj, i2c_addr)
		self.length = 10
		self.i2c_addr = i2c_addr

	def __repr__(self):
		return f"{self.__class__.__name__}({self.i2c}, i2c_addr={hex(self.i2c_addr)})"

	def set_LED_color(self, red, green, blue, number = None):
		"""
		set the color for the whole led strip or specify the specific led number (index begins at 1)

		:param red: red value 0-255
		:type int:
		:param green: green value 0-255
		:type int:
		:param blue: blue value 0-255
		:type int:
		:param number: if none set whole array to color values otherwise set led at index starting at 1 to color 

		"""
		if number:
			self._write_register_array(WRITE_SINGLE_LED_COLOR, [number, red, green, blue])
		else:
			self._write_register_array(WRITE_ALL_LED_COLOR, [red, green, blue])

	def set_LED_brightness(self, brightness, number = None):
		"""
		set the brightness for the whole led strip or specify the led number (index starting at 1) and set the brightness

		:param brightness: brightness value 0-255
		:type int:
		:param number: if none set whole array to brightness otherwise set led at index starting at 1 to brightness 
		"""

		if number:
			self._write_register_array(WRITE_SINGLE_LED_BRIGHTNESS, [number, brightness])
		else: 
			self._write_register_array(WRITE_ALL_LED_BRIGHTNESS, [brightness])

	def change_address(self, address):
		"""
		reassign i2c address to avoid conficts. 

		:param address: new i2c address to use
		:type address: int
		"""
		self._write_register_array(CHANGE_ADDRESS, [address])
		self.i2c_addr = address

	def change_length(self, length):
		"""
		reassign the number of leds 

		:param length: change the length of your array (requires soldering on additional LEDs)
		:type length: int
		"""

		self._write_register_array(CHANGE_LED_LENGTH, [length])
		self.length = length
	
	def _write_register_array(self, register, valueArray):
		buf = bytearray(1 + len(valueArray))
		buf[0] = register
		buf[1:] = valueArray
		with self.device as dev:
			dev.write(buf)

i2c = busio.I2C(board.SCL, board.SDA)
stick = LED_Stick(i2c)


stick.set_LED_color(0,255,0)
# time.sleep(2)
# stick.set_LED_color(255, 0, 0, 2)
# time.sleep(2)
stick.set_LED_brightness(1)
stick.set_LED_brightness(255, 1)

