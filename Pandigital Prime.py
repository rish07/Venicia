#!/user/bin/python
import numpy as np
import itertools
great = 0
def PrimeChecker(m):
    for a in range(2, m):
        if m % a != 0:
            return a
m = 0
checker = True
for z in range(1, 11):
    MyArray = np.asarray(list(itertools.permutations('0123456789', z)))
    for a in range(0, int(len(MyArray))):
        n = MyArray[a]
        n = " ".join(n)
        n = n.replace(" ", "")
        m = int(n)

                checker = False
        if checker == True:
            if a > great:
                great = a
                print great
print great
