x = 100
y = 1000
for num in range(x, y+ 1):
    order= len(str(num))
    sum=0
    temp = num
    while temp > 0:
        digit = temp % 10
        sum += digit** order
        temp //= 10
    if num == sum:
        print(num)
