# Arquivo que contém utilizades para o módulo transmorce.

import numpy as np
import scipy.io.wavfile as wavefile


def is_number(s):
    """
    Verifica se uma determinada string está em um formato numérico.
    :param s: a string a ser verificada.
    :return: True se a string estiver em formato numérico, False caso contrário.
    """
    try:
        float(s)
        return True
    except ValueError:
        pass

    try:
        import unicodedata
        unicodedata.numeric(s)
        return True
    except (TypeError, ValueError):
        pass

    return False


def wav_to_waves(path):
    """
    Le e converte um arquivo .wav para um array de n dimensões, onde cada subarray é uma onda com duração 25 ms.
    :param path: o caminho do arquivo a ser lido.
    :return: um array de ondas.
    """
    freq, data = wavefile.read(path)
    n = int(freq * 0.25)
    return np.split(data, range(n, len(data), n))
