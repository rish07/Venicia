#!/user/bin/python
sum = 0
for a in range(1, 1001):
    if(a == 1):
        sum += 3
    elif(a == 2):
        sum += 3
    elif(a == 3):
        sum += 5
    elif(a == 4):
        sum += 4
    elif(a == 5):
        sum += 4
    elif(a == 6):
        sum += 3
    elif(a == 7):
        sum += 5
    elif(a == 8):
        sum += 5
    elif(a == 9):
        sum += 4
    elif(a == 10):
        sum += 3
    elif(a == 11):
        sum += 6
    elif(a == 12):
        sum += 6
    elif(a == 13):
        sum += 8
    elif(a == 14):
        sum += 8
    elif(a == 15):
        sum += 7
    elif(a == 16):
        sum += 7
    elif(a == 17):
        sum += 9
    elif(a == 18):
        sum += 8
    elif(a == 19):
        sum += 8
    elif(a >= 20 and a < 30):
        sum += 6 + 6*9 + 36
    elif(a >= 30 and a < 40):
        sum += 6 + 6*9 + 36
    elif(a >= 40 and a < 50):
        sum += 6 + 6*9 + 36
    elif(a >= 50 and a < 60):
        sum += 5 + 5*9 + 36
    elif(a >= 60 and a < 70):
        sum += 5 + 5*9 + 36
    elif(a >= 70 and a < 80):
        sum += 7 + 7*9 + 36
    elif(a >= 80 and a < 90):
        sum += 6 + 6*9 + 36
    elif(a >= 90 and a < 100):
        sum += 6 + 6*9 + 36
    elif(a >= 100 and a < 200):
        sum += 7*99 + 864 + 3
    elif (a >= 200 and a < 300):
        sum += 10*99 + 864 + 3
    elif (a >= 300 and a < 400):
        sum += 12*99 + 864 + 3
    elif (a >= 400 and a < 500):
        sum += 11*99 + 864 + 3
    elif (a >= 500 and a < 600):
        sum += 11*99 + 864 + 3
    elif (a >= 600 and a < 700):
        sum += 10*99 + 864 + 3
    elif (a >= 700 and a < 800):
        sum += 12*99 + 864 + 3
    elif (a >= 800 and a < 900):
        sum += 12*99 + 864 + 3
    elif (a >= 900 and a < 1000):
        sum += 11*99 + 864 + 3
    elif (a == 1000):
        sum += 11
print sum