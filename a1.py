#Leia um número e: Se for par e positivo → “Par positivo”; Se for par e negativo → “Par negativo”; Caso contrário → “Ímpar”
valor = int(input("Digite o primeiro valor: "))
if (valor > 0) and (valor % 2 == 0):
    print("O resultado é Par Positivo.")
elif (valor < 0) and (valor % 2 == 0):
    print("O resultado é Par Negativo")
else:
    print("Ímpar")