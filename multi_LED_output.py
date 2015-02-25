import RPi.GPIO as GPIO
import string_to_morse as morse
import time

GPIO.setmode(GPIO.BOARD)

unit_length = 1

dot_pin = 7
dash_pin = 11
letter_break_pin = 13
word_break_pin = 15

pins = [dot_pin, dash_pin, letter_break_pin, word_break_pin]

for pin in pins:
    GPIO.setup(pin, GPIO.OUT)

def flash_for_units(pin, num_units):
    GPIO.input(pin)
    GPIO.output(pin, True)
    time.sleep(num_units*unit_length)
    GPIO.output(pin, False)

def wait_for_units(num_units):
    time.sleep(num_units*unit_length)

def dot():
    flash_for_units(dot_pin, 1)

def dash():
    flash_for_units(dash_pin, 1)

def space_part():
    wait_for_units(1)

def space_letter():
    flash_for_units(letter_break_pin, 1)

def space_word():
    flash_for_units(word_break_pin, 1)

def cleanup():
    GPIO.cleanup()

def do_command(command):
    if command == morse.dot:
        print('*'),
        dot()
    elif command == morse.dash:
        print('-'),
        dash()
    elif command == morse.letter_break:
        print(' '),
        space_letter()
    elif command == morse.part_break:
        space_part()
    elif command == morse.word_break:
        print ''
        space_word()

def transmit_string(string):
    morse_commands = morse.string_to_morse(string)
    last = morse.part_break
    for command in morse_commands:
        do_command(command)
    cleanup()
