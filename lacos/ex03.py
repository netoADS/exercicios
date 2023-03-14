# leia o valor de n
n = int(input("Digite o valor de n: "))

# inicialize a soma
soma = 0

# calcule a soma
i = 1
while i <= n:
    soma = soma + i
    i = i + 1

# imprima a soma
print("A soma dos", n, "primeiros inteiros positivos é", soma)
#sub