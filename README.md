# RPi-Dictaphone

Press button 1 to record audio from microphone to file. Press button 2 to play last recorded file.

Audio files are saved sequentially to "/home/pi/sampler/audio" and can be accessed using ftp.

## Pi Zero Wifi Settings:

hostname: rpi-dictaphone.lan (can be set with raspi-config)
login: pi             (default)
password: raspberry     (default)

## Startup Script

Code runs on startup using python script located in
/home/pi/sampler/

This can be changed by commenting out a line in:
/etc/init.d/startup_scripts

## Dependencies:

pyaudio   [link](https://gist.github.com/brecke/9833cd6b1ae4077c4b5c)

## Other Settings:

Alsamixer volume settings:
Use 'alsamixer' command to adjust both microphone and speaker levels
