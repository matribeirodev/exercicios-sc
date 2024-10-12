nome = input("Qual seu nome?")
pergunta = float(input(f"{nome} qual é a sua temperatura?"))
temperatura = pergunta

if temperatura <= 37.4:
    print(f"{nome} está com a temperatura normal")

if temperatura >= 37.5 and temperatura < 37.7:
    print(f"{nome} está com uma febre baixa")

if temperatura >= 37.7:
    print(f"{nome} está com uma febre alta")

if temperatura < 37.5:
    print(f"{nome} está com uma febre muito baixa")

