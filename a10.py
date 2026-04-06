#Leia um valor e: verifique se eles está entre 0 e 100, caso o número esteja fora do intervalo, mostre na tela o valor
n1 = int(input("Digite o valor: "))
if (n1 >= 0) and (n1 <= 100):
    print("Está no intervalo.")
else:
    print(f"Seu número {n1} não está no intervalo!")