sum_ = 0
count = 0
while 1:
    inp = input()
    if inp != '.':
        sum_ += int(inp)
        count += 1
    else:
        break
print(sum_ / count)
