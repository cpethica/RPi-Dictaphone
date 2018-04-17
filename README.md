# RPi-Dictaphone

A raspberry pi zero based dictaphone. Press button 1 to record audio from microphone to file. Press button 2 to play last recorded file.

## Hardware

[USB Audio Interface](https://thepihut.com/collections/raspberry-pi-usb-accessories/products/usb-audio-adapter)


[Electret microphone](http://uk.farnell.com/adafruit/1063/for-use-with-mcu-sensor-evaluation/dp/2419156)

[Mini speaker](https://www.ebay.co.uk/itm/Portable-Mini-Outdoor-Speaker-MP3-Music-Player-with-Wired-Headphone-USB-Charging/173243587344?hash=item28561f5b10:m:mgvwdJbQIyCGyQSL1laNYPw)
[3.3v Regulator](https://www.ebay.co.uk/itm/AMS1117-3-3V-800mA-AMS-1117-Voltage-Regulator-Module-LM1117-Arduino-PIC-UK-B101/162150926391?hash=item25c0f2c837:g:pegAAOSwZVlXmdbi)
Push to Make Buttons



## Pi Zero Wifi Settings:

hostname: rpi-dictaphone.lan   (can be set with raspi-config)
login: pi                      (default)
password: raspberry            (default)

## Startup Script

Code runs on startup using python script located in
/home/pi/sampler/

This can be changed by commenting out a line in:
/etc/init.d/startup_scripts

## Audio files:

Audio files are saved sequentially to "/home/pi/audio_files" and can be accessed using sftp.

## Dependencies:

pyaudio   [link](https://gist.github.com/brecke/9833cd6b1ae4077c4b5c)

## Other Settings:

Alsamixer volume settings:
Use 'alsamixer' command to adjust both microphone and speaker levels
