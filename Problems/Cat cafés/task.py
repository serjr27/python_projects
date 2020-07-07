str_ = ''
max_cats = 0
cafe_name = ''

while True:
    str_ = input().split()
    if str_[0] != 'MEOW':
        if int(str_[1]) > max_cats:
            cafe_name = str_[0]
            max_cats = int(str_[1])
    else:
        break

print(cafe_name)
