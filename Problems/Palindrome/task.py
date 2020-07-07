def palindrome(word: str):
    len_ = len(word)
    if len_ % 2 == 0:
        for i, j in zip(word, reversed(word)):
            if i != j:
                return False
    else:
        return False
    return True


word_ = input()

if palindrome(word_):
    print('Palindrome')
else:
    print('Not palindrome')
