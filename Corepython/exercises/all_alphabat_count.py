name = "himanshu amlavad"
count = 0

for i in "abcdefghijklmnopqrstuvwxyz":
    count = 0
    for j in name:
        if i == j:
            count += 1
    if count > 0:
        print(i, "=", count)

for i in name[::-1]:
    print(i,end="")

    for ch in range(len(name) - 1, -1, -1):
        print(name[ch], end='')