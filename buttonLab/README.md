# Interfacing with the Pi (or Pi Toppings)

The Raspberry Pi 4 has a variety of interfacing options. When you plug the pi in the red power LED turns on. Any time the SD card is accessed the green LED flashes. It has standard USB ports and HDMI ports. Less familiar it has a set of 20x2 pin headers that allow you to connect a various peripherals.
![pi gpio diagram](https://www.raspberrypi.org/documentation/usage/gpio/images/GPIO-Pinout-Diagram-2.png)
To learn more about any individual pin and what it is for go to [pinout.xyz](https://pinout.xyz/pinout/3v3_power) and click on the pin. Some terms may be unfamiliar but we will go over the relevant ones as they come up.

## Pre-lab
- Many of the components we will be using in this class will communicate with the I2C protocol. Prior to the lab read through [this](https://learn.sparkfun.com/tutorials/i2c/all) tutorial on how it works.
- In this class you will see the words Stemma, StemmaQT and Qwiic come up. these are all different kinds of connectors for use with the I2C protocol. We have tried to keep things consistent to StemmaQT and and Qwiic which are interchangeable. Read over [this](https://learn.adafruit.com/introducing-adafruit-stemma-qt/what-is-stemma) and [this](https://www.sparkfun.com/qwiic#overview) to get a better idea of what these terms mean.

## Connecting a Button

### Hardware

From your kit take out the [mini-PiTFT](https://learn.adafruit.com/adafruit-mini-pitft-135x240-color-tft-add-on-for-raspberry-pi), a [stemmaQT cable](https://www.adafruit.com/product/4210) and the [Qwiic Button](https://www.sparkfun.com/products/16842). <p float="left">
  <img src="https://cdn-learn.adafruit.com/assets/assets/000/082/842/large1024/adafruit_products_4393_iso_ORIG_2019_10.jpg?1571856509" height="200" />
  <img src="https://cdn-shop.adafruit.com/970x728/4210-02.jpg" height="200">
  <img src="https://cdn.sparkfun.com//assets/parts/1/5/7/6/7/16842-SparkFun_Qwiic_Button_-_Green_LED-01.jpg" height="200">
</p>

Connect the one side of cable to the stemmaQT port on the underside of the screen. Line up the screen and press it on the headers. The hole in the screen should match up with the hole on the raspberry pi.

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
(circuitpython) pi@ixe00:~/buttonLab $ pip install -r requirements.txt 
```

#### Scan the I2C Bus

run the file `I2CTest.py` and the output should look like:

```
(circuitpython) pi@ixe00:~/buttonLab $ python I2CTest.py 
I2C ok!
I2C addresses found: []

```

Now plug the other end of the cable into the ports on the right of the button board. The pwr LED should turn on. Run the file again and you should see the device ID.

```
(circuitpython) pi@ixe00:~/buttonLab $ python I2CTest.py 
I2C ok!
I2C addresses found: ['0x6f']
```
#### Read device registers

With I2C devices we can read the registers directly with `button_registers.py`

#### Leverage abstraction

Use a higher level device interface can make reading and writing registers for I2C devices easier. Try running `button_device.py` and pressing the button. Look at the code and the [list of registers](https://cdn.sparkfun.com/assets/learn_tutorials/1/1/0/8/Qwiic_Button_I2C_Register_Map.pdf) and see if you can figure out what line 56 is for.

```
56               write_register(device, STATUS, 0)
```

#### Open source hardware and software

This class uses a lot of material that is developed with the intention of being free, open and accessible. All of the parts you used for this lab openly post their code and schematics should others want to riff on these designs or learn how they work. You are encouraged to [take](https://learn.adafruit.com/adafruit-mini-pitft-135x240-color-tft-add-on-for-raspberry-pi/downloads) [a](https://www.raspberrypi.org/documentation/hardware/raspberrypi/schematics/rpi_SCH_4b_4p0_reduced.pdf) [look](https://github.com/sparkfun/Qwiic_Button). You may find that someone has solved your problems for you and neatly packed them in a [library](https://github.com/gmparis/CircuitPython_I2C_Button). Feel free to look at and use solutions that others have posted so long as you **always cite their contributions**. 

Run `library_example.py` then look at the code, then take a look at how it's made on [github](https://github.com/gmparis/CircuitPython_I2C_Button).

