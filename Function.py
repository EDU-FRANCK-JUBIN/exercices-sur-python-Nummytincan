def max(a, b):
    if a < b:
        return "b est supérieur"
    if a > b:
        return "a est supérieur"
    if a == b:
        return "ils sont égaux"


print(max(1, 2))
print(max(2, 1))
print(max(2, 2))
