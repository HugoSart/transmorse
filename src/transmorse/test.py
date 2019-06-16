# Arquivo contendo os testes do módulo transmorce.

import numpy as np
import time

import transmorse.morse as morse
import transmorse.util as util


# Tradutor
enc = morse.Encoder()
dec = morse.Decoder()

# Entradas de teste
morse = '101110000000111000100010111010001011101000101110000000111000100011101110000000101011101000111011101110001011101000111011100010111000000011101011101000111011101110001110100010101011100010001110101011100010111000000011101110111000111010101000101010001000101110100010101011100010001110111000000011101110111000000011101110111000101110100011101010100010100011100010111000101110100000001110101000101110000000101110101000101011100010111'
text = 'A terra tem forma convexa observem o orbitar da lua'
audio = util.wav_to_waves('./test/audio.wav')
expected = '.-  - . .-. .-. .-  - . --  ..-. --- .-. -- .-  -.-. --- -. ...- . -..- .-  --- -... ... . .-. ...- . --  ---  --- .-. -... .. - .- .-.  -.. .-  .-.. ..- .-'


def test_from_morse():
    assert expected == enc.from_morse(morse)


def test_from_text():
    assert expected == enc.from_text(text)


def test_from_audio():
    assert expected == enc.from_audio(audio)


def test_to_morse():
    assert morse == dec.to_morse(expected)


def test_to_text():
    assert text == dec.to_text(expected)


def test_to_audio():
    assert np.array_equal(audio, dec.to_audio(expected))


def run_tests():
    """
    Roda todos os testes.
    """
    tests = [
        test_from_morse, test_from_text, test_from_audio,
        test_to_morse, test_to_text, test_to_audio
    ]
    for index, test in enumerate(tests):
        print('[TEST] Test %d -> ' % index, end='')
        start = time.process_time()
        try:
            test()
            end = time.process_time()
            print('%2.2f s \t| SUCCESS!' % (end - start))
        except AssertionError as e:
            end = time.process_time()
            print('%2.2f s \t| FAILED : ' % (end - start), e)


def main():
    run_tests()


if __name__ == "__main__":
    main()
