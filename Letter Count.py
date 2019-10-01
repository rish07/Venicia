import string

s = input()

s = ("".join(s.split())).lower()



checkdata = list(s.lower())
data = list(string.ascii_lowercase)

countdata = {}
for k in s:
    countdata[k] = 0
for i in s:
    for j in data:
        if i == j:
            countdata[i] = countdata[i] + 1
    

print(countdata)



