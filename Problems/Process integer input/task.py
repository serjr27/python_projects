# put your python code here
n = 0
while True:
    n = int(input())
    if 10 <= n <= 100:
        print(n)
    elif n > 100:
        break
    else:
        continue
