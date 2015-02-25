import RPi.GPIO as GPIO
import string_to_morse as morse
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

def space_word():
    wait_for_units(7)

def cleanup():
    GPIO.cleanup()

def do_command(command):
    if command == morse.dot:
        dot()
    elif command == morse.dash:
        dash()
    elif command == morse.part_break:
        space_part()
    elif command == morse.letter_break:
        space_letter()
    elif command == morse.word_break:
        space_word()
    else:
        print 'ERROR: Unrecognized command ' + str(command)

def transmit_string(string):
    morse_commands = morse.string_to_morse(string)
    for command in morse_commands:
        do_command(command)
    cleanup()
