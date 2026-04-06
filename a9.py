#Leia dois números e: Verifique se são iguais ou diferentes. Sendo diferentes mostre a diferença entre eles
n1 = int(input("Digite o primeiro valor: "))
n2 = int(input("Digite o segundo valor: "))
if (n1 == n2):
    print("Os números são iguais.")
elif (n1 != n2):
    print("Os números são diferentes.")
    if n1 > n2:
        print("Diferença é: ", n1 - n2)
    else:
        print("Diferença é: ", n2 - n1)