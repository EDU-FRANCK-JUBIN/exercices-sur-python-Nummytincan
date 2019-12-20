n = int(input("entrer la taille du sapin"))
s = 2*n - 1
for i in range(1, n*2, 2):
    print(' '*s+i*'^')
    s=s-1