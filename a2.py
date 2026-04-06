#Leia dois números e: Mostre a soma; Mostre qual é maior ou se são iguais
a1 = int(input("Digite o primeiro numero: "))
a2 = int(input("Digite o segundo numero: "))
soma = a1 + a2

print("A soma é: ",soma)

if (a1 > a2):
    print("O primeiro número é maior.")
elif (a2 > a1):
    print("O segundo número é maior.")
else:
    print("Os números são iguais!!")