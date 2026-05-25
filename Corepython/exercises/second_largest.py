lis = [100, 2, 30, 4, 50, 70, 6, 3, 1]
largest = 0
for i in lis:
    if i > largest:
        largest = i
print("Largest in list", largest)

sec_l = 0
for i in lis:
    if i > sec_l and i < largest:
        sec_l = i
print("Second largest in list", sec_l)
