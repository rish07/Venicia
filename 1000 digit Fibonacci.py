#!/user/bin/python
'''
n1 = 0
n2 = 1
n3 = 1
flag = 1
count = 1
m = 0
while flag < 1000:
    n3 = n1 + n2
    n1 = n2
    n2 = n3
    count += 1
    m = str(n3)
    if len(m) == 1000:
        flag = 1000
print count
'''

d1 = 1
d2 = 3
d3 = 5
d4 = 7
r = 8
f = 10
f1 = 12
f2 = 14
for i in range(1, 1001):
    d1 += r

    for j in range(1, 1001):
        d2 += f
        f += 8
        d3 += f1
        f1 += 8
        d4 += f2
        f2 += 8

    r += 8

sum1 = d1 + d2 + d3 + d4
print sum1