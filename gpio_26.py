# install before run
# pip3 install gpiod
import gpiod

chip = gpiod.chip(0)
pin = 26
gpiod_pin = chip.get_line(pin)
config = gpiod.line_request()
config.consumer = "Blink"
config.request_type = gpiod.line_request.DIRECTION_OUTPUT
gpiod_pin.request(config)

gpiod_pin.set_value(1)
