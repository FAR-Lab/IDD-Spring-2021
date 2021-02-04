import board
import busio
import adafruit_apds9960.apds9960
import time
i2c = busio.I2C(board.SCL, board.SDA)
sensor = adafruit_apds9960.apds9960.APDS9960(i2c)

sensor.enable_proximity = True


with open('log.csv', 'a') as outfile:
	while True:
		prox = sensor.proximity
		outfile.write(f"{time.time()},{prox}\n")
		print(prox)
		time.sleep(0.2)