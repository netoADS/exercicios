i = float(input("Valor inicial: "))
tj = 0.005
m = 12

for c in range(13):
    montante = i * (1+tj)**c
    print(f"Mês {c}: R${montante}")
