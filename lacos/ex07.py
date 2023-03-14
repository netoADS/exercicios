#n = numero
#r = resultado
#c = conta

n = int(input("Fatorial de: ") )

r=1
c=1

while c <= n:
    r *= c
    c += 1

print(r)
#sub