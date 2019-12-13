from pyDatalog import pyDatalog
pyDatalog.clear()

pyDatalog.create_terms('ordre', 'triangle', 'triangleisocele', 'coteegaux', 'trianglerectangle','angledroit','triangleequilateraux','X','Y')

#triangle
triangle(X) <= ordre(X,Y) & (Y==3)
trianglerectangle(X) <= triangle(X) & angledroit(X)
triangleisocele(X) <= triangle(X) & coteegaux(X,Y) & (Y==2)
triangleequilateraux(X) <= triangle(X) & coteegaux(X,Y) & (Y==3)

#déclaration de polygones
+ordre('polygone_1',3)
+angledroit('polygone_1')
+triangle('polygone_2')
+coteegaux('polygone_2',2)
+triangle('polygone_3')
+coteegaux('polygone_3',3)

print(pyDatalog.ask('trianglerectangle(X)'))
print(pyDatalog.ask('triangleisocele(X)'))
print(pyDatalog.ask('triangleequilateraux(X)'))
print(pyDatalog.ask('trianglerectangle("polygone_1")'))
print(pyDatalog.ask('triangleisocele("polygone_1")'))
print(pyDatalog.ask('triangleequilateraux("polygone_1")'))