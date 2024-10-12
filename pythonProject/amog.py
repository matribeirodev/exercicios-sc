from random import randint
from time import sleep
Jogadores = []
print("                              ❤️Among Us❤️                              ")
print("")
amongs = ["Azul🩵", "Vermelho❤️", "Verde💚", "Amarelo💛", "Laranja🧡", "Roxo💜", "Rosa🩷"]
tarefas = ["fios", "lixo", "cartão", "download"]
escolhadetarefas = []
morreram = []
ativo = True
while True:
    escolher = input(f"Qual jogador você quer ser?\nEstas são as opções: {amongs}\nOu X para parar.\n")
    if escolher.upper() == "X":
        break
    else:
        Jogadores.append(escolher)

print("Se você é Impostor, tem como função matar os jogadores sem ser descoberto")
print("Se você é Inocente, tem como função descobrir o impostor e fazer as tarefas ")
Tamanho = len(Jogadores) - 1
Impostor = randint(0,Tamanho)
posicao = 0
posjogador = 0
fazerTarefas = True
while ativo:
    while posicao < len(tarefas):
        print(f"{posicao}- {tarefas[posicao]}")
        posicao = posicao + 1
    while posjogador < len(Jogadores):
        if Jogadores[posjogador] not in morreram:
            print(f"É a vez do jogador {Jogadores[posjogador]}")
            escolha = input("Qual o numero da sua tarefa?")
            escolhadetarefas.append(escolha)
            #continuar = input("Deseja continuar ou X para parar")
        posjogador = posjogador + 1
    posjogador = 0
    impostorMorreu = False
    fazerTarefas = True
    while impostorMorreu == False and fazerTarefas == True:
        while posjogador < len(Jogadores):
            if Jogadores[posjogador] not in morreram:
                if posjogador == Impostor:
                    print(f"Tarefa concluida pelo jogador {Jogadores[posjogador]}")
                elif escolhadetarefas[posjogador] == escolhadetarefas[Impostor]:
                    print(f"💀 O jogador {Jogadores[posjogador]} morreu 💀")
                    morreram.append(Jogadores[posjogador])
                else:
                    print(f"Tarefa concluida pelo jogador {Jogadores[posjogador]}")
            posjogador = posjogador + 1

        quem = input("Quem é o impostor?")
        if quem == Jogadores[Impostor]:
            impostorMorreu = True
            ativo = False
            print("Parabéns, encontrou o Impostor🤩😃🥳")
        else:
            fazerTarefas = False
            print("Errou! Este jogador não é o impostor☹️, o jogo continua")

        posjogador = 0

    posicao = 0
    escolhadetarefas = []
