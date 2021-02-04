# Pre-Lab

What should they do for the prelab?

### I2C Sensors

Sensors take a physical property from world and translate them into electrical signals computers can log, react or analyze. How the sensor does that depends on what is being measured but most of the sensors we will use in this class take physical phenomenon and translate them into a varying voltage, current or resistance. The sensors in your kit are StemmaQT/Qwiic compatible. This means they use I2C to communicate. Like the button from the button lab each sensor will have a data sheet with register maps for communicating with the host device (the Pi in our case). Most of the sensors included in your kit already have circuitpython libraries that make it easy to communicate with Pi.

### Hardware

From your kit take out the [mini-PiTFT](https://learn.adafruit.com/adafruit-mini-pitft-135x240-color-tft-add-on-for-raspberry-pi), a [stemmaQT cable](https://www.adafruit.com/product/4210) and the [APDS9960 Proximity, Light, RGB, and Gesture Sensor](https://www.adafruit.com/product/3595). <p float="left">
  <img src="https://cdn-learn.adafruit.com/assets/assets/000/082/842/large1024/adafruit_products_4393_iso_ORIG_2019_10.jpg" height="200" />
  <img src="https://cdn-shop.adafruit.com/970x728/4210-02.jpg" height="200">
  <img src="https://cdn-shop.adafruit.com/1200x900/3595-03.jpg" height="200">
</p>

Connect the one side of cable to the stemmaQT port on the underside of the screen. Line up the screen and press it on the headers. The hole in the screen should match up with the hole on the raspberry pi. With the other end connect the sensor.

<p float="left">
<img src="https://cdn-learn.adafruit.com/assets/assets/000/087/539/medium640/adafruit_products_4393_quarter_ORIG_2019_10.jpg?1579991932" height="200" />
<img src="https://cdn-learn.adafruit.com/assets/assets/000/082/861/original/adafruit_products_image.png" height="200">
</p>

### Software 

#### Reading values

Clone the repo for this assignment and create a branch with your netId

```
pi@ixe00:~$ git clone path/to/repo
pi@ixe00:~$ cd repo
```

We will continue to use the python environment we created previously. Activate that that environment by typing `workon circuitpython` then installing the requirements for this lab.
your terminal should now look like this
```
pi@ixe00:~/repo $ workon circuitpython
(circuitpython) pi@ixe00:~/repo $ pip install -r requirements.txt 
```

An Adafruit library makes using this sensor incredibly easy. If we look at `proximity.py`:

```
import board
import busio
import adafruit_apds9960.apds9960
import time

i2c = busio.I2C(board.SCL, board.SDA)
sensor = adafruit_apds9960.apds9960.APDS9960(i2c)

sensor.enable_proximity = True

while True:
	prox = sensor.proximity
	print(prox)
	time.sleep(0.2)
``` 
After some imports and setup the actual code is incredibly simple. In `logging.py` with just a couple more lines you can log readings to a csv file. If the pi is connected to the internet there's no reason you couldn't log them to a google sheet and serve them online.

We can detect colors and draw them to the display.

### State

