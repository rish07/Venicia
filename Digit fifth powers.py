#!/user/bin/python
s = 0
f = 0
sum = 0
for a in range(99, 999999):
    g = str(a)
    for b in range(0, len(g)):
        s = int(g[b])
        sum += s*s*s*s*s
    if sum == f:
        print f
