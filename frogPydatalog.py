from pyDatalog import pyDatalog
pyDatalog.clear()
# Creation des faits
pyDatalog.create_terms('croaks', 'eatflies', 'green', 'yellow', 'frog', 'sings', 'canary', 'chirps', 'X')
+croaks("fritz")
+eatflies("fritz")

#creation des faits
frog(X) <= croaks(X) & eatflies(X)
canary(X) <= chirps(X) & sings(X)
green(X) <= frog(X)
yellow(X) <= canary(X)

#print(pyDatalog.ask('frog("fritz")'))
print(frog("xyz"))