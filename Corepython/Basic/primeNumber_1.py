num = 7
count = 0
for i in range(2,num):
    if num%i == 0:
       count += 1

if count == 0:
    print("prime number")
else:
    print("not prime number")
