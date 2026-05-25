num = 1001
n = num
sum = 0
r = 0

while n > 0:
    r = n % 10
    n = n // 10
    sum = (sum * 10) + r

if sum == num:
    print("palendrom")
else:
    print("not palendrom")