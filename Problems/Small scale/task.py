floats = list()

while True:
    str_ = input()
    if str_ != '.':
        floats.append(float(str_))
    else:
        break

print(min(floats))
