# -*- coding: utf-8 -*-

def string_to_morse_code(x):
    """
    Returns the morse code of a string x.
    If x is not a string, returns 'ValueError, string expected!'.
    """
    if not isinstance(x, str):
        return 'ValueError, string expected!'
    x = x.upper()
    mcode = {'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.',
             'F': '..-.', 'G': '--.', 'H': '....', 'I': '..', 'J': '.---',
             'K': '-.-', 'L': '.-..', 'M': '--',   'N': '-.', 'O': '---',
             'P': '.--.', 'Q': '--.-', 'R': '.-.',  'S': '...', 'T': '-',
             'U': '..-', 'V': '...-', 'W': '.--',  'X': '-..-', 'Y': '-.--',
             'Z': '--..', ' ': ' ', '0': '-----', '1': '.----', '2': '..---',
             '3': '...--', '4': '....-',  '5': '.....',  '6': '-....',
             '7': '--...', '8': '---..',  '9': '----.',  '&': '.-...',
             "'": '.----.', '@': '.--.-.', ')': '-.--.-', '(': '-.--.',
             ':': '---...', ',': '--..--', '=': '-...-',  '!': '-.-.--',
             '.': '.-.-.-', '-': '-....-', '+': '.-.-.',  '"': '.-..-.',
             '?': '..--..', '/': '-..-.'}
    out = [mcode[x[0]]]
    for char in x[1:]:
        out.append(mcode[char])
    out = ' '.join(out)
    return out
