x = int(input("Digite um número inteiro positivo: "))

while x < 0:
    x = int(input("Número inválido. Digite um número inteiro **positivo**: "))

while x >= 0:
    print(x)
    x -= 1