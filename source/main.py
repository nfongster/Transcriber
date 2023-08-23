import movReader
import os


def main():
    print("Enter *.mov filename, without the extension: ")
    mov_filename = input() + ".mov"
    movReader.extract_audio(os.path.join(os.path.curdir, mov_filename))


if __name__ == '__main__':
    main()
