print("""Os candidatos são:
1.  Candidato Jair Rodrigues 
2.  Candidato Carlos Luz
3.  Candidato Neves Rocha
4.  Nulo
5.  Branco
""")

a = 6
e1 = 0
e2 = 0
e3 = 0
e4 = 0
e5 = 0

for e in range(a):
    voto = int(input("insira o n° do candidato: "))
    if voto == 1:
        e1 = e1 + 1
    elif voto == 2:
        e2 = e2 + 1
    elif voto == 3:
        e3 = e3 + 1        
    elif voto == 5:
        e5 = e5 + 1
    else:
        e4 = e4 + 1
        
print("numero de votos do candidato Jair Rodrigues:", e1)
print("numero de votos do candidato Carlos Luz:", e2)
print("numero de votos do candidato Neves Rocha:", e3)
print("numero de votos Nulos:", e4)
print("numero de votos em Branco:", e5)
