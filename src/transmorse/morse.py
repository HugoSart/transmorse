# -*- coding: utf-8 -*-
# Arquivo principal do transmorce. Jás aqui a lógica da tradução.

from enum import Enum, unique
import numpy as np

from transmorse.util import is_number


@unique
class Alphabet(Enum):
    """
    Enumeração com o alfabeto morse utilizado como linguagem intermediária para facilitação da tradução.
    """
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


class Encoder:
    alpha_map = Alphabet.to_map()

    @staticmethod
    def from_text(plain):
        if type(plain) is not str:
            raise TypeError('Incorrect parameter type. Should be string.')
        plain = str(plain)

        text = ''
        words = plain.split(' ')
        for word in words:
            for letter in word:

                # Pega atributo correspondente do alfabeto morse
                elname = letter.capitalize()
                if is_number(elname):
                    elname = 'A' + elname

                l = Alphabet.__getattr__(elname)
                text += l.value + ' '
            text += ' '

        return text.lower().capitalize().strip()

    @staticmethod
    def from_morse(plain):
        if type(plain) is not str:
            raise TypeError('Incorrect parameter type. Should be string.')
        plain = str(plain)

        encoded = ''
        words = plain.split('0000000')
        for word in words:
            letters = word.split('000')
            for letter in letters:
                parts = letter.split('0')
                for part in parts:
                    encoded += '.' if len(part) == 1 else '-'
                encoded += ' '
            encoded += ' '
        return encoded.strip()

    @staticmethod
    def from_audio(waves):
        bin = ''
        for wave in waves:
            if not np.any(wave):
                bin += '0'
            else:
                bin += '1'
        return Encoder.from_morse(bin)


class Decoder:
    alpha_map = Alphabet.to_map()

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
                if l != '':
                    text += str(Decoder.alpha_map[l]).replace('Alphabet.', '')
            text += ' '
        return text.lower().capitalize().strip()

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
        return text.strip('0')

    @staticmethod
    def to_audio(plain, sample_rate=48000, frequency=440, wave_duration=0.25):
        if type(plain) is not str:
            raise TypeError('Incorrect parameter type. Should be string.')
        plain = str(plain)

        n = int(sample_rate * wave_duration)

        waves = np.array([[]])
        bin = Decoder.to_morse(plain)
        for b in bin:
            waves = np.append(waves, np.array([np.sin(2 * np.pi * frequency * x / sample_rate) for x in range(n)] if b != '0' else [0] * n))
        return np.split(waves, range(n, len(waves), n))
