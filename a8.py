#Leia um número e: Mostre se ele é par positivo, par negativo, impar positivo, impar negativo ou neutro
n1 = int(input("Digite o seu número: "))
if (n1 > 0) and (n1 % 2 == 0):
    print("Ele é par positivo.")
elif (n1 < 0) and (n1 % 2 == 0):
    print("Ele é par negativo.")
elif (n1 > 0) and (n1 % 2 != 0):
    print("Ele é ímpar positivo.")
elif (n1 < 0) and (n1 % 2 != 0):
    print("Ele é ímpar negativo.")
else:
    print("Neutro")