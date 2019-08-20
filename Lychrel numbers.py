#!/user/bin/python
def reverse(string):
    string = reversed(string)
    return string


c = 0

for a in range(1, 10001):
    s = a
    for z in range(1, 51):
        b = str(reverse(s))
        b = int(b)
        sum = s + b
        s = sum
    if s == reverse(str(sum)):
        c += 1
        print c
print c
