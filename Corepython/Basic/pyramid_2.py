rows = 5

for i in range(rows):

    # spaces
    for j in range(rows - i - 1):
        print(end="\t")

    # upper stars
    for k in range(2 * i + 1):
        print("*", end="\t")

    print()

for i in range(rows - 2, -1, -1):

    # spaces
    for j in range(rows - i - 1):
        print(end="\t")

    # lower stars
    for k in range(2 * i + 1):
        print("*", end="\t")

    print()