#!/user/bin/python

flag = 0
i = 1
while flag == 1:
    j = 0
    for a in range(1, 11):
        if i % a == 0:
            j += 1
    i += 1
    print i
    if j == 20:
        print i
        flag = 1