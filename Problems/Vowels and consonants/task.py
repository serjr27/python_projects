vowels = 'aeiouyAEIOY'
consonats = 'bcdfghjklmnpqrstvwxzBCDFGHJKLMNPQRSTVWXZ'

word = input()

for letter in word:
    if letter in vowels:
        print('vowel')
    elif letter in consonats:
        print('consonant')
    else:
        break
