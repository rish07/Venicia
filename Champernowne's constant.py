#!/user/bin/python
sums = "0."

for a in range(1, 100000001):
    sums += str(a)
result = int(sums[2]) * int(sums[11]) * int(sums[101]) * int(sums[1001]) * int(sums[10001]) * int(sums[100001]) * int(sums[1000001])
print result