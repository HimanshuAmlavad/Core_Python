num = 153
n = num
r = 0
sum = 0

while n > 0:
    r = n % 10
    sum = (sum * 10) + r
    n = n // 10

print("reverse number:", sum)

if num == sum:
    print("is pelondrom")
else:
    print("not pelondrom")