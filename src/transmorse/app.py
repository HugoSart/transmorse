# -*- coding: utf-8 -*-

import argparse

import numpy as np
import scipy.io.wavfile as wavefile
from transmorse import morse

enc = morse.Encoder()
dec = morse.Decoder()


def main():
    parser = argparse.ArgumentParser(description='Tradutor de código morse')
    parser.add_argument('-i', dest='input', type=str, nargs='?', help='O arquivo contendo o morse a ser traduzido')
    parser.add_argument('-o', dest='output', type=str, nargs='?', help='O nome do diretório a ser criado contendo as traduções')
    args = parser.parse_args()

    extension = args.input.split('.')[-1]
    inter = None
    print('[TRANSMORSE] Codificando para código intermediário ...')
    if extension == 'morse':
        with open(args.input, 'r') as f:
            inter = enc.from_morse(f.read().replace('\n', ''))
    elif extension == 'txt':
        with open(args.input, 'r') as f:
            inter = enc.from_text(f.read().replace('\n', ''))
    elif extension == 'wav':
        with open(args.input, 'r') as f:
            inter = enc.from_audio(f.read().replace('\n', ''))
    else:
        raise RuntimeError('Extensão de entrada inválida: ' + extension)

    # Realiza traduções
    print('[TRANSMORSE] Decodificando para produção dos resultados ...')
    audio = dec.to_audio(inter)
    m = dec.to_morse(inter)
    text = dec.to_text(inter)

    # Escreve resultados
    print('[TRANSMORSE] Escrevendo resultados ...')
    wavefile.write(args.output + '/audio.wav', rate=48000, data=np.reshape(audio, -1))
    with open(args.output + '/code.morse', 'w') as f:
        f.write(m)
    with open(args.output + '/text.txt', 'w') as f:
        f.write(text)


if __name__ == "__main__":
    main()
