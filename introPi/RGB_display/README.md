# Interfacing with the Pi I

## PreLab



The raspberry Pi we are using in this course is used extensively by hobbyists and professionals. In the years since its initial release an ecosystem of add-ons, hats and peripherals have grown around it. In this lab we will introduce you to the [Adafruit MiniPiTFT](https://www.adafruit.com/product/4393) and Python on the Pi.

![Pi TFT](https://cdn-learn.adafruit.com/assets/assets/000/082/842/large1024/adafruit_products_4393_iso_ORIG_2019_10.jpg)

The Raspberry Pi 4 has a variety of interfacing options. When you plug the pi in the red power LED turns on. Any time the SD card is accessed the green LED flashes. It has standard USB ports and HDMI ports. Less familiar it has a set of 20x2 pin headers that allow you to connect a various peripherals.
![pi gpio diagram](https://www.raspberrypi.org/documentation/usage/gpio/images/GPIO-Pinout-Diagram-2.png)
To learn more about any individual pin and what it is for go to [pinout.xyz](https://pinout.xyz/pinout/3v3_power) and click on the pin. Some terms may be unfamiliar but we will go over the relevant ones as they come up.

## Connecting a Display

### Hardware

From your kit take out the [mini-PiTFT](https://learn.adafruit.com/adafruit-mini-pitft-135x240-color-tft-add-on-for-raspberry-pi) and the [Raspberry Pi 4](https://www.adafruit.com/product/4296)

Line up the screen and press it on the headers. The hole in the screen should match up with the hole on the raspberry pi.

<p float="left">
<img src="https://cdn-learn.adafruit.com/assets/assets/000/087/539/medium640/adafruit_products_4393_quarter_ORIG_2019_10.jpg?1579991932" height="200" />
<img src="https://cdn-learn.adafruit.com/assets/assets/000/082/861/original/adafruit_products_image.png" height="200">
</p>

### Software

In terminal SSH on to the pi

```
ssh pi@ixe00.local
```

Clone the repo for this assignment and create a branch with your netId

```
pi@ixe00:~$ git clone path/to/repo
pi@ixe00:~$ cd repo
```

Set up your python environment, install the packages from the requirements.txt., and 

```
pi@ixe00:~/repo $ mkvirtualenv circuitpython
(circuitpython) pi@ixe00:~/displayLab $ pip install -r requirements.txt 
```

#### Testing your Screen

The display uses a communication protocol called [SPI](https://www.circuitbasics.com/basics-of-the-spi-communication-protocol/) to speak with the raspberry pi. We won't go in depth in this course over how SPI works. The port on the bottom of the display connects to the SDA and SCL pins used for the I2C communication protocol which we will cover later. GPIO (General Purpose Input/Output) pins 23 and 24 are connected to the two buttons on the left. GPIO 22 controls the display backlight.

We can test it by typing 
```
python screenTest.py
```

You can type the name of a color then press either of the buttons to see what happens on the display. take a look at the code with
```
cat screenTest.py
```

#### Displaying Info
You can look in `stats.py` for how to display text on the screen

#### Displaying an image

You can look in `image.py` for an example of how to display an image on the screen. Can you make it switch to another image when you push one of the buttons?



