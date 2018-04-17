#!/usr/bin/env python3
import pyaudio
import wave
import sys
import os
import time

import RPi.GPIO as gpio
gpio.setmode(gpio.BCM)
gpio.setup(17, gpio.IN, pull_up_down=gpio.PUD_UP)
gpio.setup(22, gpio.IN, pull_up_down=gpio.PUD_UP)


def recorder():
    CHUNK = 512
    FORMAT = pyaudio.paInt16 #paInt8
    CHANNELS = 1
    RATE = 44100 #sample rate
    WAVE_OUTPUT_FILENAME = "pyaudio-output.wav"

    p = pyaudio.PyAudio()

    stream = p.open(format=FORMAT,
                    channels=CHANNELS,
                    rate=RATE,
                    input=True,
                    frames_per_buffer=CHUNK) #buffer

    # Determine the timeout in ms
    timeout = 10000

    print("* recording")

    # Create an empty list for audio recording
    frames = []

    # Determine the timestamp of the start of the response interval
    start_time = time.time()
    current_time = time.time()

    # Record audio until space is pressed
    while (current_time - start_time) < timeout:

        # Record data audio data
        data = stream.read(CHUNK)
        # Add the data to a buffer (a list of chunks)
        frames.append(data)

        # Get new timestamp
        current_time = time.time()

        # Check if space key has been pressed
        key = recorder_keyboard.get_key(timeout=0)[0]

        # If space is pressed, advance to next part of the experiment
        if key == 'space':
            # Record data audio data
            data = stream.read(CHUNK)
            # Add the data to a buffer (a list of chunks)
            frames.append(data)
            break

    else:
        # Record data audio data
        data = stream.read(CHUNK)
        # Add the data to a buffer (a list of chunks)
        frames.append(data)

    print("* done recording")

    stream.close()
    p.terminate()

    wf = wave.open(WAVE_OUTPUT_FILENAME, 'wb')
    wf.setnchannels(CHANNELS)
    wf.setsampwidth(p.get_sample_size(FORMAT))
    wf.setframerate(RATE)
    wf.writeframes(b''.join(frames))
    wf.close()
    return


while True:
    input_value = gpio.input(17)
    if input_value == False:
        print('The record button has been pressed...')
        recorder()
        while input_value == False:
            input_value = gpio.input(17)

    input_value = gpio.input(22)
    if input_value == False:
        print('The play button has been pressed...')
        os.system("aplay --device=plughw:1,0 pyaudio-output.wav")
        while input_value == False:
            input_value = gpio.input(22)
