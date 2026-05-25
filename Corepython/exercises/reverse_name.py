str = "himanshu amlavad"

name_list = str.split()

for name in name_list:
    for ch in range(len(name) - 1, -1, -1):
        print(name[ch], end='')
    print(' ', end='')
