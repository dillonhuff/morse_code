import string_to_morse as morse
import test_utils as test

def test_string_to_morse(word, expected):
    test.test_result(morse.string_to_morse(word), expected, word + ' to morse')

def all_morse_tests():
    test_string_to_morse('A', [morse.dot, morse.part_break, morse.dash])
