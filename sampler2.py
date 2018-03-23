#!/usr/bin/env python3
import pyaudio
import wave
import sys
import os
from time import sleep

import RPi.GPIO as gpio
gpio.setmode(gpio.BCM)
gpio.setup(17, gpio.IN, pull_up_down=gpio.PUD_UP)
gpio.setup(22, gpio.IN, pull_up_down=gpio.PUD_UP)


def recorder():
    CHUNK = 512
    FORMAT = pyaudio.paInt16 #paInt8
    CHANNELS = 1
    RATE = 44100 #sample rate
    RECORD_SECONDS = 5
    WAVE_OUTPUT_FILENAME = "pyaudio-output.wav"

    p = pyaudio.PyAudio()

    stream = p.open(format=FORMAT,
                    channels=CHANNELS,
                    rate=RATE,
                    input=True,
                    frames_per_buffer=CHUNK) #buffer

    print("* recording")

    frames = []

    for i in range(0, int(RATE / CHUNK * RECORD_SECONDS)):
        data = stream.read(CHUNK)
        frames.append(data) # 2 bytes(16 bits) per channel

    print("* done recording")

    stream.stop_stream()
    stream.close()
    p.terminate()

    wf = wave.open(WAVE_OUTPUT_FILENAME, 'wb')
    wf.setnchannels(CHANNELS)
    wf.setsampwidth(p.get_sample_size(FORMAT))
    wf.setframerate(RATE)
    wf.writeframes(b''.join(frames))
    wf.close()
    return

def player():
    #define stream chunk
    chunk = 1024

    #open a wav format music
    f = wave.open("pyaudio-output.wav","rb")
    #instantiate PyAudio
    p = pyaudio.PyAudio()
    #open stream
    stream = p.open(format = p.get_format_from_width(f.getsampwidth()),
                    channels = f.getnchannels(),
                    rate = f.getframerate(),
                    output = True)
    #read data
    data = f.readframes(chunk)

    #play stream
    while data:
        stream.write(data)
        data = f.readframes(chunk)

    #stop stream
    stream.stop_stream()
    stream.close()

    #close PyAudio
    p.terminate()



while True:
    input_value = gpio.input(17)
    if input_value == False:
        print('The record button has been pressed...')
        recorder()
        while input_value == False:
            input_value = gpio.input(17)

while True:
    input_value = gpio.input(22)
    if input_value == False:
        print('The play button has been pressed...')
        os.system("aplay --device=plughw:1,0 pyaudio-output.wav")
        while input_value == False:
            input_value = gpio.input(22)                   
