from tkinter import N


Numero1 = int(input("numero 1 ="))              # insere para o usuario por numero
Numero2 = int(input("numero 2 ="))               # insere para o usuario por numero
N = int(input(" Digite o numero da tabuada="))    # insere para o usuario por numero da tabuada

Soma = Numero1 + Numero2                         
mult = Numero1 * Numero2

print("Soma é ", Soma)
print("Multiplicação é", mult)
X= 1

while X <= 10:
    numeros = N * X   
    print(N,"x",X,"=",numeros)
    X = X+1


