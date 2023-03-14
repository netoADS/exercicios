t = int(input("insira o numero da tabuada que deseja: "))

for c in range(10):
    print("%d x %d = %d" % (t, c+1, t*(c+1)) )
    