p = 1.
for i in range(1, 10000):
    t = (4*i*i)/(4*i*i-1)
    p = p*t
R = 2*p
print(R)
