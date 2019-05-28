from abc import abstractmethod
from enum import Enum, unique
import numpy as np

@unique
class Alphabet(Enum):
    A = '.-'
    B = '-...'
    C = '-.-.'
    D = '-..'
    E = '.'
    F = '..-.'
    G = '--.'
    H = '....'
    I = '..'
    J = '.---'
    K = '-.-'
    L = '.-..'
    M = '--'
    N = '-.'
    O = '---'
    P = '.--.'
    Q = '--.-'
    R = '.-.'
    S = '...'
    T = '-'
    U = '..-'
    V = '...-'
    W = '.--'
    X = '-..-'
    Y = '-.--'
    Z = '--..'
    A0 = '-----'
    A1 = '.----'
    A2 = '..---'
    A3 = '...--'
    A4 = '....-'
    A5 = '.....'
    A6 = '-....'
    A7 = '--...'
    A8 = '---..'
    A9 = '----.'
    LETTER_SPACE = ' '
    WORD_SPACE = '  '

    @classmethod
    def to_map(cls):
        m = {}
        for a in Alphabet:
            m[a.value] = a
        return m


class Translator:
    alpha_map = Alphabet.to_map()

    @staticmethod
    def to_audio(plain):
        if type(plain) is not str:
            raise TypeError('Incorrect parameter type. Should be string.')
        plain = str(plain)

        rate = 4800
        freq = 440
        wave_length = int(rate * 0.25)

        waves = []
        bin = Translator.to_morse(plain)
        for b in bin:
            waves.append(
                [np.sin(2 * np.pi * freq * x / rate) for x in range(wave_length)] if b != '0'
                else [0] * wave_length
            )
        return waves

    @staticmethod
    def to_text(plain):
        if type(plain) is not str:
            raise TypeError('Incorrect parameter type. Should be string.')
        plain = str(plain)

        text = ''
        words = plain.split(Alphabet.WORD_SPACE.value)
        for w in words:
            letters = w.split(Alphabet.LETTER_SPACE.value)
            for l in letters:
                text += str(Translator.alpha_map[l]).replace('Alphabet.', '')
            text += ' '
        return text.lower().capitalize()

    @staticmethod
    def to_morse(plain):
        if type(plain) is not str:
            raise TypeError('Incorrect parameter type. Should be string.')
        plain = str(plain)

        text = ''
        words = plain.split(Alphabet.WORD_SPACE.value)
        for w in words:
            letters = w.split(Alphabet.LETTER_SPACE.value)
            for l in letters:
                for i, c in enumerate(l):
                    if c == '.':
                        text += '1'
                    elif c == '-':
                        text += '111'
                    text += '0'
                text += '00'
            text += '0000'
        return text[:-7]
