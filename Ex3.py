import math
ev = math.e
apx = 0
while True:
    print("entrer un nombre supérieur à 50")
    nb = int(input())
    if nb > 50:
        break
for i in range(nb):
    apx += 1/math.factorial(i)
tab = []
tab.append(ev)
tab.append(apx)
print(tab)