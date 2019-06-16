# Transmorse
Um tradutor morse implementando utilizando a linguagem Python 3.
<br><br>
Possuí suporte para três tipos de entradas:
- **.txt**: texto convêncional em Português (Brasil) sem suporte para caracteres especiais.
- **.morse**: texto binário (zeros e uns);
- **.wav**: áudio morse (48 KHz);

## Dependências
Este programa possui duas depenêndias:
- _numpy_
- _scipy.io.wavfile_

Para a execução do programa, é necessário que estas dependências estejam devidamente instaladas no seu ambiente de execução python.

## Execução
Para executar o tradutor, navege até a pasta _transmorce/src_ e digite o seguinte comando:
- _python -m transmorce.app -i <INPUT_FILE> -o <OUTPUT_FOLDER>_

Para execurar os testes, utilize o seguinte comando, também na pasta _transmorce/src_:
- _python -m transmorce.test_