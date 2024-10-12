numeros = [1, 2, 3, 4, 5, 8]
i = len(numeros) - 1 # 5
inverso = []


while i >= 0:
    inverso.append(numeros[i]) # i = 5, 4, 3, 2, 1, 0
    # numeros[i] = 8, 5, 4, 3, 2, 1
    i -= 1 # i = i - 1

print("A lista invertida é:", inverso)