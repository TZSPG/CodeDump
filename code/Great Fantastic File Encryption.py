def unicode_index(letter):
    # TODO Unused function. Use or cleanp please
    if letter.isalpha():
        return ord(letter.lower()) - 96


def shifter(line, shift):
    """Applies caesar shift to line"""
    return line[shift:] + line[:shift]


def file_handler(filename):
    """Returns an array of separate lines (i.e: lines separated by \n characters"""
    with open(filename, 'r') as file:
        return [line.rstrip('\n') for line in file.readlines()]


def encrypt(line, line_index):
    shifted = shifter(line, line_index + 1)
    unicoded = ' '.join(str(ord(letter) + index) for index, letter in enumerate(shifted))
    return unicoded


def decrypt(line, line_index):
    unicode_nums = [int(x) for x in line.split(' ')]
    caesar_shift = (line_index + 1) * -1
    plain_unicode = ''.join(chr(num - index) for index, num in enumerate(unicode_nums))

    return shifter(plain_unicode, caesar_shift)


def output_file(code, filename):
    with open(filename, 'w') as file:
        for line in code:
            file.write(line + '\n')


def interface():
    choice = input("Welcome to Tynan's file encryption. Do you wish to encrypt of decrypt? ")
    if choice.lower() in 'encrypt':
        file = input("Encrypt selected. Please specify the file to be encrypted (with extension): ")
        while True:
            try:
                scramble = [encrypt(line, index) for index, line in enumerate(file_handler(file))]
                output_file(scramble, file + ' - ENCRYPTED.txt')
                break
            except FileNotFoundError:
                file = input("That file doesn't exist. Please make sure the specified file "
                             "contains the extension: ")
        print("Encryption successful. Thank you for choosing Tynan's file encryption!")

    elif choice.lower() in 'decrypt':
        file = input("Decrypt selected. Please specify the file to be decrypted (with .txt extension): ")
        while True:
            try:
                lines = [decrypt(line, index) for index, line in enumerate(file_handler(file))]
                output_file(lines, file + ' - DECRYPTED.txt')
                break
            except FileNotFoundError:
                file = input("That file doesn't exist. Please make sure the specified file "
                             "contains the extension .txt: ")
            except ValueError:
                file = input('This file cannot be decrypted. Only untampered files encrypted with the '
                             'encryptor bundled with this decryptor can be decrypted: ')
        print("Decryption successful. Thank you for choosing Tynan's file encryption!")

if __name__ == '__main__':
    interface()
