predio = 20
i = 0
print("Total de andares:", predio)
for i in range(predio):
    if (i + 1) != 13: print(i + 1)
print("----------------------------------------------------------")
andar = 20
contador = 1
while contador <= 20:
    if contador != 13: print("Andar:", contador)
    contador = contador + 1
print("-------------------descedente---------------------")

for i in range(predio, 0, -1):
    if i != 13: print(i)