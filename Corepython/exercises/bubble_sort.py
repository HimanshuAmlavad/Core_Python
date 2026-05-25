lis = [100, 2, 30, 4, 50, 70, 6, 3, 1]

for i in range(0 , len(lis) - 1):
    for j in range(i+1, len(lis)):
        if lis[i]>lis[j]:
            tem = lis[i]
            lis[i] = lis[j]
            lis[j] = tem
print(lis)