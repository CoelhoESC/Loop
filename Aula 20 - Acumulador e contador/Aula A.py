"""
While/ Else
Contadores
Acumuladores
"""
contador = 0
acumulador = 1

while contador <= 100:
    print(contador, acumulador)
    acumulador = acumulador + contador
    contador = contador + 1
else:
    print('Cheguei no else. ')

    
while contador <= 10:
    print(contador)
    contador += 1
    if contador > 5:  # como o while ainda é TRUE, o Else não sera executado
        break
else:
    print('Isso não será executado')
print('Isso sera executado')
