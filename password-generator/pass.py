# ask user to length of password at least 4
# add character, symbol, numeric lists
# use random to select random choice
# shall make def
import random
import string
import pyperclip

pass_len = int(input('Please enter desired length of the password: '))
while pass_len < 4:
    pass_len = int(input(
        'Please enter desired length of the password (4 Minimum!): '))
numbers = string.digits
letters = string.ascii_letters
symbols = string.punctuation


def pass_generator():

    rand = [random.choice(letters), str(
        random.choice(numbers)), random.choice(symbols)]
    return random.choice(rand)


generated = ''


while len(generated) < pass_len:
    character = pass_generator()
    generated = generated + character

print(
    f'Your generated password is: {generated} and it\'s been copied to clipboard.')
pyperclip.copy(generated)
input()
