num = 153
n = num
sum = 0
r = 0

while n > 0:
    r = n%10
    n = n//10
    sum = sum  + (r**3)


if sum == num:
    print("Armstrong")
else:
    print("not Armstrong")