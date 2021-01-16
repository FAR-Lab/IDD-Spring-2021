# Welcome to the Pi Shop

This lab will introduce you to the raspberry pi. The raspberry pi is a small cheap single board computer. It's capable of doing most things you might expect from a desktop computer. You can connect to the internet, run code, plug in a monitor and keyboard/mouse.

## Setup

#### From your kit you will need:
- [Raspberry Pi 4](https://www.adafruit.com/product/4296)
- [Power Supply](https://www.adafruit.com/product/4298)
- [SD card](https://www.bhphotovideo.com/c/product/1536561-REG/silicon_power_sp032gbsthbv1v20sp_32gb_elite_a1_uhs_1.html/reviews)
- [SD card reader](https://www.bhphotovideo.com/c/product/751120-REG/Iogear_GFR204SD_10_in_1_USB_2_0_SD_MicroSD_MMC.html)

#### On your computer download
- [Raspberry Pi Imager](https://www.raspberrypi.org/software/)
- [Our Copy of Raspbian at ftp://farlab.infosci.cornell.edu/](ftp://farlab.infosci.cornell.edu/)
(this is a large file and may take a few minutes to download)
- If using windows: [Windows 10 SSH Client](https://docs.microsoft.com/en-us/windows/terminal/tutorials/ssh) or [PuTTY](https://www.putty.org/)

#### Setting up your OS
1. Plug the SD card into your computer using the card reader
2. Choose the downloaded file for "Choose OS" and the SD card for "Choose SD card" then hit write.
![Imager GUI](https://www.raspberrypi.org/homepage-9df4b/static/md-67e1bf35c20ad5893450da28a449efc4.png)

3. Create a file called [wpa_supplicant.conf](https://www.raspberrypi.org/documentation/configuration/wireless/headless.md) in the Boot image of the new disk. the file contents should have the following:

	```
	ctrl_interface=DIR=/var/run/wpa_supplicant GROUP=netdev
	update_config=1
	country=<Insert 2 letter ISO 3166-1 country code here, for the United states it is US>
	
	network={
	 ssid="<Name of your wireless LAN>"
	 psk="<Password for your wireless LAN>"
	}
	```
	make sure to update with your own network information.
	
	This information gets copied over to your Raspberry Pi when it boots up, so that the Pi gets a DHCP address from your network router and can show up on your network

4. Eject or unmount the microSD card drive, and then remove it and reinsert it into the RPi in the slot on the bottom (silver rectangle on the right)
![Pi bottom side](https://cdn-shop.adafruit.com/1200x900/4296-12.jpg)

5. Boot the RPi by connecting it to a power source

#### Connecting to your Pi

Unlike your laptop the Pi doesn't come with its own keyboard or mouse. While you could plug in a monitor, keyboard, and mouse we will be connecting to your Pi over SSH. You can do this in [Mac Terminal](https://blog.teamtreehouse.com/introduction-to-the-mac-os-x-command-line) or [Windows 10 SSH Client](https://docs.microsoft.com/en-us/windows/terminal/tutorials/ssh). Make sure you connect your laptop to the same network as you entered in your `wpa_supplicant.conf` above.

1. In Terminal type `$ arp -a` and you should see output that looks like this:
    ```
	rt-ac5300-c020 (192.168.2.1) at b0:6e:bf:86:c0:20 on en0 ifscope [ethernet]
	ixe00 (192.168.1.131) at (incomplete) on en0 ifscope [ethernet]
	? (224.0.0.251) at 1:0:5e:0:0:fb on en0 ifscope permanent [ethernet]
	? (239.255.255.250) at 1:0:5e:7f:ff:fa on en0 ifscope permanent [ethernet]
   ```
Take note the ip address in the line that starts with `ixe00`. For me that is `192.168.2.131` but you should use whatever number you see there.

2. Verify your pi is online. In terminal type `ping 192.168.2.131` replacing that number with your own.
    ```
	 ping 192.168.1.131
	PING 192.168.1.131 (192.168.1.131): 56 data bytes
	64 bytes from 192.168.1.131: icmp_seq=0 ttl=64 time=252.118 ms
	64 bytes from 192.168.1.131: icmp_seq=1 ttl=64 time=10.331 ms
	64 bytes from 192.168.1.131: icmp_seq=2 ttl=64 time=10.209 ms
	64 bytes from 192.168.1.131: icmp_seq=3 ttl=64 time=14.816 ms
	^C
	--- 192.168.1.131 ping statistics ---
	4 packets transmitted, 4 packets received, 0.0% packet loss
	round-trip min/avg/max/stddev = 10.209/71.868/252.118/104.084 ms
	```
You can use `control-C` to interrupt and exit the ping (press the `control` key, and while holding it down, also press the `C` key, then let go of both together--this looks like `^C` in the terminal).

2.  SSH into the Pi.

When you first log in it will show you a "fingerprint" and ask you whether you want to continue connecting. Say `yes`.



```shell
ssh pi@192.168.1.131
The authenticity of host '192.168.1.131' can't be established.
ECDSA key fingerprint is SHA256:Y9S4oMH2H70fz3K/L42Kw39k+zkpyfr0DmGdzBx7SKk.
Are you sure you want to continue connecting (yes/no)? yes
```
From your terminal, log in to your Pi using the command `ssh pi@192.168.1.131` with the password: `raspberry` 

After you say yes, type the password `raspberry` and hit Enter. You should see this:

```shell
pi@192.168.1.131's password:
Linux ixe00 4.9.59-v7+ #1047 SMP Sun Oct 29 12:19:23 GMT 2017 armv7l

The programs included with the Debian GNU/Linux system are free software;
the exact distribution terms for each program are described in the
individual files in /usr/share/doc/*/copyright.

Debian GNU/Linux comes with ABSOLUTELY NO WARRANTY, to the extent
permitted by applicable law.
Last login: Wed Jan 17 10:42:03 2018

SSH is enabled and the default password for the 'pi' user has not been changed.
This is a security risk - please log


in as the 'pi' user and type 'passwd' to set a new password.

pi@ixe00:~ $ 
```

Once you are signed in, your terminal will now connected directly to the 'terminal' on your Pi, via `ssh`. You can tell this by looking at the user and hostname at the beginning of each line, which should now look like:

```shell
pi@ixe00 ~ $
```

### Change the password

Because the Pi asked you to! Also to keep your RPi from getting hacked.

Write it down somewhere, because we don't know how to recover lost passwords on the RPi.

## Explore the RPi

### Enable X Windows
We will want to enable X windows usage on the Raspberry Pi. (Should this not work see below for instructions on how to use VNC)

On the Mac, please install [XQuartz](https://www.xquartz.org).

On the PC, please install [XMing](https://sourceforge.net/projects/xming/).

To enable XWindows to open with the Pi, we need to log into the Pi with the -X flag to enable xwindows forwarding:
```
shell
$ ssh -X pi@ixe00.local
pi@ixe00.local's password: 
Linux ixe00 4.19.66-v7+ #1253 SMP Thu Aug 15 11:49:46 BST 2019 armv7l

The programs included with the Debian GNU/Linux system are free software;
the exact distribution terms for each program are described in the
individual files in /usr/share/doc/*/copyright.

Debian GNU/Linux comes with ABSOLUTELY NO WARRANTY, to the extent
permitted by applicable law.
Last login: Thu Jul 30 17:50:45 2020 from fe80::480:f9c8:6452:925e%wlan0
pi@ixe00:~ $ xeyes
```
Here, we test out the Xwindows using the Xeyes program. Use Ctrl-C afterwards to end the program.

Look in the RPi image and see where things are at. In specific, see if you can find:

``Banana.jpg``
``Wormy.py``

### Using VNC
Another way to connect to your IxE is using VNC (Virtual Network Computing). It essentially is remote login. The easiest client to use is [VNC Connect](https://www.realvnc.com/en/connect/download/viewer/). Download and install it. Once that's done type the IP address of the IxE in the text-box at the top. 
![](images/VNC1.png)

After that a login window should appear, use your normal logins (originally: Account=pi, Password=raspberry).
![](images/VNC2.png)

At that point the normal RPI desktop should appear and you can start and stop programs from here. 


![](images/VNC3.png)
The image below shows where to find the terminal and how to run one of the object recognition examples. 

**Make sure to plug your camera if you try this.***

![](images/VNC4.png)

For easy copy and paste:
```shell
cd pi-object-detection/
./test_object_detection.sh 
```

### Try some Python code on the Pi

To keep our python dependencies and packages organized we will be using [virtualenvwrapper](https://virtualenvwrapper.readthedocs.io/en/latest/command_ref.html#managing-environments). 

The important commands to remember:

- **mkvirtualenv**: create a new environment.
- **workon**: select the environment you wish to work with
- **deactivate**: unselect the environment you were using
- **lsvirtualenv**: list available virtual environments
- **rmvirtualenv**: remove an environment you no longer use

We will be using Python in future modules, so try running some of the sample python code in ``python_games``:

1. First create an environment by typing `mkvirtualenv games`. you should see you are in the virtual environment by the name in parenthesis in the prompt.
2. install pygame by typing `pip install pygame`
3. `cd python_games`
4. Try playing a game by typing `python wormy.py`	
``wormy.py``
``catanimation.py``
``tetromino.py``

Take a look at the code in the python file, using ``cat``, or ``nano``.

Also try the shellscripts in the ``textToSpeech`` directory.

** How do you know what the shell script is doing? **

Adapt the scripts so that they say what you want them to say.


### Experimenting with Linux processes


Try running multiple programs at the same time using the ‘&’ to make each process a background process:
```shell
pi@ixe00:~ $ cd python_games/
pi@ixe00:~/python_games $ python2 wormy.py &
[1] 2851
pi@ixe00:~/python_games $ python2 drawing.py &
[2] 2856
pi@ixe00:~/python_games $ 
```
Make the last background process a foreground process with ‘fg’”
```shell
pi@ixe00:~/python_games $ python2 drawing.py &
[1] 2879
pi@ixe00:~/python_games $ fg
python drawing.py
```

One a process is in the foreground, it is possible to end it by typing Ctrl-c.

Sometimes, we want to push a process to the background after we’ve started it. Here is how to do that:

```shell
pi@ixe00:~/python_games $ python2 drawing.py
^Z
[1]+  Stopped                 python2 drawing.py
pi@ixe00:~/python_games $ bg
[1]+ python drawing.py &
pi@ixe00:~/python_games $ 
```

Also, it is possible to kill background processes through their process ids. We highlight where you can look for that process id:

```shell
pi@ixe00:~/python_games $ python2 drawing.py &
[1] 2894
pi@ixe00:~/python_games $ ps -x
  PID TTY      STAT   TIME COMMAND
  497 ?        Ss     0:00 /lib/systemd/systemd --user
  500 ?        S      0:00 (sd-pam)
  505 ?        Ssl    0:00 /usr/bin/lxsession -s LXDE-pi -e LXDE
 <various processes left out>
 2474 ?        S      0:42 sshd: pi@pts/0
 2477 pts/0    Ss     0:00 -bash
 2894 pts/0    Sl     0:01 python drawing.py
 2907 pts/0    R+     0:00 ps -x
pi@ixe00:~/python_games $ kill -9 2894
pi@ixe00:~/python_games $ 
[1]+  Killed                  python2 drawing.py
pi@ixe00:~/python_games $ 
```

<!--**Submit your code to Github**

This project is going to be the submission of this week. You will need to upload the changes you made on the Pi to the GitHub page. To do that you need to follow three simple steps: Stage => Commit => Push! 

[Uploading on github via terminal](https://docs.github.com/en/free-pro-team@latest/github/managing-files-in-a-repository/adding-a-file-to-a-repository-using-the-command-line)

```
$ git add .
# Adds the file to your local repository and stages it for commit. To unstage a file, use 'git reset HEAD YOUR-FILE'.

$ git commit -m "Add existing file"
# Commits the tracked changes and prepares them to be pushed to a remote repository. To remove this commit and modify the file, use 'git reset --soft HEAD~1' and commit and add the file again.

$ git push origin your-branch
# Pushes the changes in your local repository up to the remote repository you specified as the origin
```

You might be required to login in the terminal to your GitHub account. For more details on how the Git commands work or what other commands are available checkout this [cheatsheet](https://education.github.com/git-cheat-sheet-education.pdf).  -->


#### Pro-tips and other commands
`nano` is a general purpose text editor, so you can use it for any type of text file like the `.js`, `.html`, and `.css` files in this project.

Notice on the bottom of the terminal window that there is some text showing things like `^G Get Help` and `^O Write Out`. These are the commands that you can use in `nano`. The `^` character stands for `Ctrl`. So to `Write Out` (which means to save the file), you would type `Ctrl` and `O` (that's the letter `O`, not the number `0`). When you've typed these, you will see a bar appear at the bottom of the terminal that says `File Name to Write: chatServer.js`. This is the file name you are saving to. In this case, we want the same name, so we can just hit the `Enter` key. You will then see a message on the bottom that tells you how many lines were written, something like `[ Wrote 116 lines ]`.


