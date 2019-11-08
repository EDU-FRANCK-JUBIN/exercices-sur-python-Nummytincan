while True:
    print("entrer un nombre supérieur à 1")
    nb = int(input())
    if nb > 1:
        break
strreponse = "diviseur propre de " + str(nb) + " sont :"
f = 0
for i in range(2, nb):
    if nb % i == 0:
        strreponse += " " + str(i)
        f += 1
if f == 0:
    strreponse += "aucun il est premier"
else:
    strreponse += " " + str(nb) + " soit " + str(f+1) + " diviseurs propres"
print(i)
print(strreponse)


