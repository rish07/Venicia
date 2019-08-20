#!/user/bin/python
exp = 1
sum = 0
for a in range(2, 1000):
    for b in range(100000000, 999999999):
        exp = a^b
        c = exp % 1000000000
        if  c == b:
            sum += c
            print sum
print sum

