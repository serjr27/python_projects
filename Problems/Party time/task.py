party_list = list()
while True:
    name = input()
    if name != '.':
        party_list.append(name)
    else:
        break
print(str(party_list))
print(len(party_list))
