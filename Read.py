#!/usr/bin/env python3

import RPi.GPIO as GPIO
from mfrc522 import SimpleMFRC522
import subprocess

reader = SimpleMFRC522()

try:
    id, text = reader.read()
    print(id)
    print(text)
    ret_code = subprocess.call("omxplayer -o both " + text, shell=True)
    sleep(2)
finally:
    GPIO.cleanup()
