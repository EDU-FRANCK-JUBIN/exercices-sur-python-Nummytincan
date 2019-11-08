import math
print("entrer la hauteur du cone")
h = int(input())
print("entrer le rayon de la base du cone")
r = int(input())
v = r*r*math.pi
print(v)
v /= 3
print(v)
v *= h
print(v)
