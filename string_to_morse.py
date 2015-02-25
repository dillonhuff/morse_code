from itertools import chain, izip, repeat, islice

dot = 1
dash = 2
letter_break = 3
word_break = 4
part_break = 5

letter_morse_codes = {'A' : [dot, dash],
                      'B' : [dash, dot, dot, dot],
                      'C' : [dash, dot, dash, dot],
                      'D' : [dot, dash, dash],
                      'E' : [dot],
                      'F' : [dot, dot, dash, dot],
                      'G' : [dash, dash, dot],
                      'H' : [dot, dot, dot, dot],
                      'I' : [dot, dot],
                      'J' : [dot, dash, dash, dash],
                      'K' : [dash, dot, dash],
                      'L' : [dot, dash, dot, dot],
                      'M' : [dash, dash],
                      'N' : [dash, dot],
                      'O' : [dash, dash, dash],
                      'P' : [dot, dash, dash, dot],
                      'Q' : [dash, dash, dot, dash],
                      'R' : [dot, dash, dot],
                      'S' : [dot, dot, dot],
                      'T' : [dash],
                      'U' : [dot, dot, dash],
                      'V' : [dot, dot, dot, dash],
                      'W' : [dot, dash, dash],
                      'X' : [dash, dot, dot, dash],
                      'Y' : [dash, dot, dash, dash],
                      'Z' : [dash, dash, dot, dot] }

def intersperse(delimiter, seq):
    return islice(chain.from_iterable(izip(repeat(delimiter), seq)), 1, None)

def letter_to_morse_code(letter):
    letter_code = letter_morse_codes[letter]
    return list(intersperse(part_break, letter_code))

    
