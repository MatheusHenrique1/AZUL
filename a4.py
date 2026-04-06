#Leia um valor e: Converta para inteiro; Se for múltiplo de 3 → “Múltiplo de 3”; Senão → “Não é múltiplo"
valor = int(input("Digite o seu valor: "))
if (valor % 3 == 0):
    print("O valor é múltiplo de 3.")
else: 
    print("O valor não é multiplo.")