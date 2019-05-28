import transmorse.morse as morse


def main():
    test = '.-  - . .-. .-. .-  - . --  ..-. --- .-. -- .-  -.-. --- -. ...- . -..- .-  --- -... ... . .-. ...- . --  ---  --- .-. -... .. - .- .-.  -.. .-  .-.. ..- .-'
    trans = morse.Translator()
    print('bin: ' + trans.to_morse(test))
    print('mor: ' + trans.to_text(test))
    print('aud: ' + str(trans.to_audio(test)))


if __name__ == "__main__":
    main()
