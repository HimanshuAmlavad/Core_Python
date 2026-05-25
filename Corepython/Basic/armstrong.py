num = 153
n = num
r = 0
sum = 0

while n > 0:
    r = n % 10
    sum = sum + (r*r*r)
    n = n // 10

if sum == num:
    print("is armstrong")
else:
    print("not armstrong")