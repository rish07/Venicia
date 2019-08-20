#!/user/bin/python
sum = 0
for num in range(0, 2000000):
       for i in range(2,num):
           if (num % i) == 0:
               break
       else:
           print num
           sum += num
print sum