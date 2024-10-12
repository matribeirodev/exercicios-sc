from random import randint
from time import sleep
Jogadores = []
print("                              ❤️Among Us❤️                              ")
print("")
amongs = ["Azul🩵", "Vermelho❤️", "Verde💚", "Amarelo💛"]
tarefas = ["fios", "lixo", "cartão", "download"]
escolhadetarefas = []
while True:
    escolher = input(f"Qual jogador você quer ser? Estas são as opções: {amongs} ou X para parar")
    if escolher.upper() == "X":
        break
    else:
        Jogadores.append(escolher)

print("Se você é Impostor, tem como função matar os jogadores sem ser descoberto")
print("Se você é Inoncente, tem como função descobrir o impostor e fazer as tarefas ")
Tamanho = len(Jogadores) - 1
Impostor = randint(0,Tamanho)
print(f"O Impostor é {Jogadores[Impostor]}")
posicao = 0
posjogador = 0
while True :
    while posicao < len(tarefas):
        print(f"{posicao}- {tarefas[posicao]}")
        posicao = posicao + 1
    while  posjogador < len(Jogadores):
        print(f"É a vez do jogador {Jogadores[posjogador]}")
        escolha = input("Qual o numero da sua tarefa?")
        escolhadetarefas.append(escolha)
        #continuar = input("Deseja continuar ou X para parar")
        posjogador = posjogador + 1
    posjogador = 0
    while posjogador < len(Jogadores):
        if posjogador == Impostor:
            print(f"Tarefa concluida pelo jogador {Jogadores[posjogador]}")
        elif escolhadetarefas[posjogador] == escolhadetarefas[Impostor]:
            print(f"O jogador {Jogadores[posjogador]} morreu")
            Jogadores.remove(Jogadores[posjogador])
        else:
            print(f"Tarefa concluida pelo jogador {Jogadores[posjogador]}")
        posjogador = posjogador + 1
    posjogador = 0
    posicao = 0
    escolhadetarefas = []