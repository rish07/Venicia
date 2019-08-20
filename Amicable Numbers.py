#!/user/bin/python
sum1 = 0
sum2 = 0
sum = 0
for a in range(1, 300):
    for b in range(1, a+1):
        if a % b == 0:
            sum1 += b
        for c in range(a+1, 10001):
            if b % c == 0:
                sum2 += c
    if sum1 == sum2:
        sum = sum + a + c
        print sum
print sum
        