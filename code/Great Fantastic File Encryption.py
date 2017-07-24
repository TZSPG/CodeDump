def unicode_index(letter):
    if letter.isalpha():
        return ord(letter.lower()) - 96


def caesar(line, shift):
    """Applies caesar shift to line"""
    for letter in line:
        pass



def encrypt(line):
    # TODO make unicode function start at the index of the line itself
    for letter in line[:10]:
        caesar_shift = unicode_index(letter)
        if caesar_shift is not None:
            break
    # TODO Think about abstracting to function



def decrypt():
    pass


def file_handler():
    pass


test_line = "This is a test. Please don't hurt me!"
# print(unicode_index('A'))
encrypt('123l')
