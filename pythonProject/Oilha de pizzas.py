from random import randint
from time import sleep
prontas = [] # lista vazia

while True:
    pizza = input("Qual o sabor entregue ao Robô? ")

    prontas.append(pizza) # colocamos o que a pessoa digitou dentro da lista de pizzas prontas

    continuar = input("Pressione ENTER para continuar ou N para parar ")

    if continuar.upper() == "N":
        break # ele para o loop (while)

print(prontas)

ultimaPos = len(prontas) - 1
while ultimaPos >= 0: # enquanto a ultimaPos é maior ou igual 0, faz o código abaixo
    pizzaEntregue = prontas[ultimaPos]
    tempoEntrega = randint(1,5)
    sleep(tempoEntrega)

    print("\n-----------------------------------------------\n")
    print(f"🍕 > Pizza {pizzaEntregue} entregue com sucesso! 🍕")
    print("\n-----------------------------------------------\n")
    sleep(1)

    if ultimaPos == 0:
        print("🤖 O robô está a voltar!")
    else:
        print("🤖 O Robô está indo descançar")