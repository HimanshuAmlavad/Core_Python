def armstrong(num):
    n = num
    r = 0
    sum = 0

    while n > 0:
        r = n % 10
        sum = sum + (r ** 3)
        n = n // 10

    if sum == num:
        return 'Is an Armstrong: ' + str(num)
    else:
        return 'Is Not armstrong: ' + str(num)


def triangle_pattern(num):
    row = num
    col = num

    for r in range(1, row + 1):
        for c in range(1, r + 1):
            print(c, end='\t')
        print()


def pyramid(num):
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


def prine_number(num):
    count = 0
    for i in range(2, num):
        if num % i == 0:
            count += 1

    if count == 0:
        return "Prime Number: " + str(num)
    else:
        return "not prime number: " + str(num)

def palendrom(num):
    n = num
    r = 0
    sum = 0

    while n > 0:
        r = n % 10
        sum = (sum * 10) + r
        n = n // 10

    if num == sum:
        return "is pelondrom: " + str(num)
    else:
        return "not pelondrom: " + str(num)

def note_counter(amount):

    notes = [500, 200, 100, 50, 20, 10, 5, 2, 1]
    count = 0
    for note in notes:
        count = amount // note

        if count > 0:
            print(note, " = ", count)

        amount = amount % note

def alphabat_counter(name):

    count = 0
    for i in "abcdefghijklmnopqrstuvwxyz":
        count = 0
        for j in name:
            if i == j:
                count += 1
        if count > 0:
            print(i, "=", count)

def bubble_sort(list):

    for i in range(0, len(list) - 1):
        for j in range(i + 1, len(list)):
            if list[i] > list[j]:
                tem = list[i]
                list[i] = list[j]
                list[j] = tem
    print('Bubble sort = ', list)

# print(armstrong(153))
#print(triangle_pattern(5))
#print(bubble_sort(list = [100, 2, 30, 4, 50, 70, 6, 3, 1]))
