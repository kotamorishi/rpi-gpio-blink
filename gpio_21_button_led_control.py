# install before run
# pip3 install gpiod
import gpiod
import time
import os
from datetime import timedelta

led_pin = 26
chip = gpiod.chip(0)

gpiod_pin = chip.get_line(led_pin)
config_led = gpiod.line_request()
config_led.consumer = "Blink"
config_led.request_type = gpiod.line_request.DIRECTION_OUTPUT
gpiod_pin.request(config_led)

gpiod_pin.set_value(1)


def led_on():
    gpiod_pin.set_value(1)

def led_off():
    gpiod_pin.set_value(0)


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
            #print("rising: ", event.timestamp)
            led_off()
        else:
            #print("falling: ", event.timestamp)
            led_on()
    else:
        print("timeout(10s)")


