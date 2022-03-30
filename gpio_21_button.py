# install before run
# pip3 install gpiod
import gpiod
import time
import os
from datetime import timedelta

chip = gpiod.chip(0)
pin = 21
#BUTTON_EDGE = gpiod.line_request.EVENT_RISING_EDGE
#BUTTON_EDGE = gpiod.line_request.EVENT_FALLING_EDGE
BUTTON_EDGE = gpiod.line_request.EVENT_BOTH_EDGES

button = chip.get_line(pin)

config = gpiod.line_request()
config.consumer = "Button"
config.request_type = BUTTON_EDGE

button.request(config)

while True:
    if button.event_wait(timedelta(seconds=10)):
        # event_read() is blocking function.
        event = button.event_read()
        if event.event_type == gpiod.line_event.RISING_EDGE:
            print("rising: ", event.timestamp)
        else:
            print("falling: ", event.timestamp)
    else:
        print("timeout(10s)")