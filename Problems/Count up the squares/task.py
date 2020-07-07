# put your python code here
numbers = []
first = True
i = 0
sum_squares = 0

while True:
    n = int(input())
    if n != 0:
        first = False
        numbers.append(n)
        if sum(numbers) == 0:
            break
    elif n == 0 and first is True:
        break

while i in range(len(numbers)):
    sum_squares += (numbers[i] ** 2)
    i += 1
print(sum_squares)
