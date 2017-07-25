def unicode_index(letter):
    if letter.isalpha():
        return ord(letter.lower()) - 96


def caesar(line, shift):
    """Applies caesar shift to line"""
    return line[shift:] + line[:shift]


def file_handler(filename):
    """Returns an array of separate lines (i.e: lines separated by \n characters"""
    with open(filename, 'r') as file:
        return [line.rstrip('\n') for line in file.readlines()]


def encrypt(line):
    # TODO make unicode function start at the index of the line itself
    caesar_shift = 1

    shifted = caesar(line, caesar_shift)
    unicoded = ' '.join(str(ord(letter) + index) for index, letter in enumerate(shifted))
    return unicoded


def decrypt(line):
    unicode_nums = [int(x) for x in line.split(' ')]
    caesar_shift = -1
    plain_unicode = ''.join(chr(num - index) for index, num in enumerate(unicode_nums))

    return caesar(plain_unicode, caesar_shift)


def output_file(code, filename):
    with open(filename, 'w') as file:
        for line in code:
            file.write(line + '\n')


def test():
    # TODO Exception handling
    scramble = []
    filename = 'test-file'
    descramble = ''
    for line in file_handler(filename):
        scramble.append(encrypt(line))

    for line in scramble:
        if line != '\n':
            descramble += decrypt(line) + '\n'

    print(descramble)


def interface():
    choice = input("Welcome to Tynan's file encryption. Do you wish to encrypt of decrypt? ")
    if choice.lower() in 'encrypt':
        file = input("Encrypt selected. Please specify the file to be encrypted (with extension): ")
        while True:
            try:
                scramble = [encrypt(line) for line in file_handler(file)]
                output_file(scramble, file + ' - ENCRYPTED.txt' )
                break
            except FileNotFoundError:
                file = input("That file doesn't exist. Please make sure the specified file "
                             "contains the extension: ")
        print("Encryption successful. Thank you for choosing Tynan's file encryption!")

    elif choice.lower() in 'decrypt':
        file = input("Decryption selected. Please specify the file to be decrypted (with .txt extension): ")
        while True:
            try:
                lines = [decrypt(line) for line in file_handler(file)]
                output_file(lines, file + ' - DECRYPTED.txt')
                break
            except FileNotFoundError:
                file = input("That file doesn't exist. Please make sure the specified file "
                             "contains the extension .txt: ")
        print("Decryption successful. Thank you for choosing Tynan's file encryption!")

if __name__ == '__main__':
    interface()
