from pyDatalog import pyDatalog
pyDatalog.clear()

pyDatalog.create_terms('ordre', 'triangle', 'triangleisocele', 'coteegaux', 'trianglerectangle','angledroit','triangleeqquilateraux','X','Y')

#triangle
triangle(X) <= ordre(X,Y) & Y==3
trianglerectangle(X) <= triangle(X) & angledroit(X)
triangleisocele(X) <= triangle(X) & coteegaux(X,Y) & Y==2
triangleequilateraux(X) <= triangle(X) & coteegaux(X,Y) & Y==3

#TODO ajout des regles pour les polygone d'ordre 4

#TODO déclaration des polygones
#TODO print les résultat