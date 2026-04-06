#Leia um valor e: Mostre o tipo; Se for numérico (após conversão) → mostre o quadrado
n1 = (input("Digite o valor: "))
print("O tipo do valor é: ",type(n1))

if n1.isdigit():
    numero = int(n1)
    print("O quadrado é: ", numero ** 2)
else: 
    print("Não é número")
