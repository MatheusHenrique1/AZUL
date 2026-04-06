#Leia um número e: Se for maior que 100 → mostre metade; Senão → mostre o dobro
n1 = int(input("Digite o seu número: "))
if (n1 > 100):
    metade = n1 / 2
    print("O número é maior que 100, a metade é: ",metade)
elif (n1 < 100):
    dobro = n1 * 2
    print("O número é menor que 100, o dobro é: ",dobro)