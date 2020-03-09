# ask user to length of password at least 4
# add character, symbol, numeric lists
# use random to select random choice
# shall make def
import random
import string
import pyperclip

pass_len = int(input('Please enter desired length of the password: '))
while pass_len < 4:
    pass_len = int(
        input('Please enter desired length of the password (4 Minimum!): '))

numbers = string.digits
letters = string.ascii_letters
symbols = string.punctuation

numlen = pass_len * 30 // 100
letlen = pass_len * 50 // 100
sylen = pass_len * 20 // 100


def pass_generator(x):
    return random.choice(x)


generated = ''

for i in range(sylen):
    y = pass_generator(symbols)
    generated = generated + y
for i in range(numlen):
    y = pass_generator(numbers)
    generated = generated + y
for i in range(letlen):
    y = pass_generator(letters)
    generated = generated + y

liste = list(generated)
random.shuffle(liste)
result = ''.join(liste)
print(
    f'Your generated password is: {result} and it\'s been copied to clipboard.')
pyperclip.copy(result)
input()
