lis = [100, 2, 30, 4, 50, 70, 6, 3, 1]
num = 1
en = 0

for i in range(0, len(lis)):
     if lis[i] == num :
         print('Number found:', lis[i],' at index: ',i)
         en = 1
         break
if en == 0:
    print("Number not found:")
