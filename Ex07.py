def calcfonction(fct, borneinf, bornesup, pas):
    if borneinf < bornesup:
        for i in range(borneinf, bornesup, pas):
            print(fct(i))
    else:
        print("il faut que la Borne Inférieur soit strictement inférieur à la barne supérieur")

def fct(x):
    f = 2*x**3+x-5
    return f
calcfonction(fct, 0, 20, 2)