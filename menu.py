def menu():
    print("1. Somar")
    print("2. Subtrair")
    print("3. Multiplicar")
    print("4. Dividir")
    print("0. Sair")
    opcao = int(input("Escolha uma opção: "))
    return opcao
 
 op = menu()
print("A opção que você escolheu foi:", op)
 
if op == 1:
    n1 = float(input("Número 1: "))
    n2 = float(input("Número 2: "))
    print(n1 + n2)
 
elif op == 2:
    n1 = float(input("Número 1: "))
    n2 = float(input("Número 2: "))
    print(n1 - n2)
 
elif op == 3:
    n1 = float(input("Número 1: "))
    n2 = float(input("Número 2: "))
    print(n1 * n2)

elif op == 4:
    n1 = float(input("Número 1: "))
    n2 = float(input("Número 2: "))
    print(n1 / n2)

elif op == 0:
    print("Saiu")
 
else:
    print("Opção inválida")

menu() 