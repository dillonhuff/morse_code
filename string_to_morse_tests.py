import string_to_morse as morse
import test_utils as test

def test_string_to_morse(word, expected):
    test.test_result(morse.string_to_morse(word), expected, word + ' to morse')

def all_morse_tests():
    test_string_to_morse('A', [morse.dot, morse.part_break, morse.dash])
    test_string_to_morse('NO', [morse.dash, morse.part_break, morse.dot, morse.letter_break, morse.dash, morse.part_break, morse.dash, morse.part_break, morse.dash])
    test_string_to_morse('BE ZWP', [morse.dash, morse.part_break, morse.dot, morse.part_break, morse.dot, morse.part_break, morse.dot, morse.letter_break, morse.dot, morse.word_break, morse.dash, morse.part_break, morse.dash, morse.part_break, morse.dot, morse.part_break, morse.dot, morse.letter_break, morse.dot, morse.part_break, morse.dash, morse.part_break, morse.dash, morse.letter_break, morse.dot, morse.part_break, morse.dash, morse.part_break, morse.dash, morse.part_break, morse.dot])
    test_string_to_morse('\t\nbe zwp  ', [morse.dash, morse.part_break, morse.dot, morse.part_break, morse.dot, morse.part_break, morse.dot, morse.letter_break, morse.dot, morse.word_break, morse.dash, morse.part_break, morse.dash, morse.part_break, morse.dot, morse.part_break, morse.dot, morse.letter_break, morse.dot, morse.part_break, morse.dash, morse.part_break, morse.dash, morse.letter_break, morse.dot, morse.part_break, morse.dash, morse.part_break, morse.dash, morse.part_break, morse.dot])

