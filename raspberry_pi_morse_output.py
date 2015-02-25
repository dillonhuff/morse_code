import RPi.GPIO as GPIO
import time

unit_length = 1
toggle_led_pin = 7

GPIO.setmode(GPIO.BOARD)
GPIO.setup(toggle_led_pin, GPIO.OUT)

def flash_for_units(num_units):
    GPIO.input(toggle_led_pin)
    GPIO.output(toggle_led_pin, True)
    time.sleep(num_units*unit_length)
    GPIO.output(toggle_led_pin, False)

def wait_for_units(num_units):
    time.sleep(num_units*unit_length)

def dot():
    flash_for_units(1)

def dash():
    flash_for_units(3)

def space_part():
    wait_for_units(1)

def space_letter():
    wait_for_units(3)

def space_words():
    wait_for_units(7)

def cleanup():
    GPIO.cleanup()
