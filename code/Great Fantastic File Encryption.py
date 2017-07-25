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
    # for letter in line[:10]:
    #     caesar_shift = unicode_index(letter)
    #     if caesar_shift is not None:
    #         break
    # TODO Think about abstracting to function?
    shifted = caesar(line, caesar_shift)
    unicoded = ' '.join(str(ord(letter) + index) for index, letter in enumerate(shifted))
    return unicoded


def decrypt(line):
    unicode_nums = [int(x) for x in line.split(' ')]
    print(unicode_nums)
    caesar_shift = -1
    plain_unicode = ''.join(chr(num - index) for index, num in enumerate(unicode_nums))

    # for letter in plain_unicode[11::-1]:
    #     caesar_shift = unicode_index(letter)
    #     if caesar_shift is not None:
    #         break

    return caesar(plain_unicode, caesar_shift)


def main():
    # TODO Exception handling
    scramble = []
    filename = 'test-file.txt'
    descramble = ''
    for line in file_handler(filename):
        scramble.append(encrypt(line))

    for line in scramble:
        if line != '\n':
            descramble += decrypt(line) + '\n'

    print(descramble)


if __name__ == '__main__':
    main()
# print(decrypt(scramble.rstrip(' ')))

# test_line = "akwhegkwem klwane la;w,'eaw jiorl;kao;we',wal;rmawe,"
# encry = encrypt(test_line)
# print(encry)
# decoded = decrypt(encry)
# print(decoded)
