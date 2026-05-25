space1 = 4
space2 = 2
for i in range(1, 10, 2):
    for j in range(space1, 0, -1):
        print(end="\t")
    space1 -= 1
    for k in range(1, i + 1):
        print("*", end="\t")
    print()

for i in range(7, 0, -2):
    for j in range(1, space2):
        print(end="\t")
    space2 += 1
    for k in range(1, i + 1):
        print("*", end="\t")
    print()
