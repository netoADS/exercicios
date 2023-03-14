v1 = int(input('Entre com o primeiro valor: '))
v2 = int(input('Entre com o segundo valor: '))

if(v1 < v2):
    while (v1 <= v2):
        print(v1)
        v1 = v1+1
else:
    while (v1>=v2):
        print(v1)
        v1 = v1-1
#sub