num = 7
result = 1
for i in range(2,num):
    if num%i == 0:
       result = 0
       break

if result:
    print("prime number")
else:
    print("not prime number")
