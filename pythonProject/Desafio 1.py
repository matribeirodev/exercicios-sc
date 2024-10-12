listaTimesA = []
listaTimesB = []
listaGolsTimeA = []
listaGolsTimeB = []

while True:
    timeA = input("Qual o time A ou X para parar? ")

    if timeA.lower() == "x":
        break

    timeB = input("Qual o time B? ")
    golsTimeA = int(input(f"Quantos gols o {timeA} fez?"))
    golsTimeB = int(input(f"Quantos gols o {timeB} fez?"))

    listaTimesA.append(timeA)
    listaTimesB.append(timeB)
    listaGolsTimeA.append(golsTimeA)
    listaGolsTimeB.append(golsTimeB)

maior = 0
TimeMaisGols = ""
# listaTimesA = ["Benfica","Porto", "Real Madrid", "Baarcelona", "Manchester City"]
# listaTimesB = ["Real Madrid", "Barcelona", "Manchester City", "Porto"]
# listaGolsTimeA = [0, 3, 6, 4, 5]
# listaGolsTimeB = [0, 7, 6, 4, 5]
posicao = 0
while posicao < len(listaGolsTimeA):
    if listaGolsTimeA[posicao] > maior:
        maior = listaGolsTimeA[posicao]
        TimeMaisGols = listaTimesA[posicao]

    if listaGolsTimeB[posicao] > maior:
        maior = listaGolsTimeB[posicao]
        timeMaisGols = listaTimesB[posicao]
        timeLevouMaisGols = listaGolsTimeA[posicao]
    posicao = posicao + 1

print(f"⚽ O maior nº de gols foi: \n"
      f"{maior} feito por {timeMaisGols} contra {timeLevouMaisGols} ")