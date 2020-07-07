scores = input().split()
# put your python code here
correct = 0
incorrect = 0

if 15 <= len(scores) <= 50:
    for s in scores:
        if s == 'C':
            correct += 1
        elif s == 'I':
            incorrect += 1
            if incorrect == 3:
                print('Game over')
                break

if incorrect < 3:
    print('You won')

print(correct)
