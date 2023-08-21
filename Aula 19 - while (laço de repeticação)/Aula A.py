"""
while
utilizado para realizar ações enquanto uma
condição for verdadeira!
Requisito: emtender codições e operadores!
"""
"""while True:  # Loop infinito
    nome = input('Qual é o seu nome?')
    print(f'Olá {nome}!')"""

x = 0
while x < 100:
    print(x)
    x += 1  # x = X + 1, modificando o valor de x, para que não seja sempre menor que 100, assim a condição fica falsa!
print('Acabou')  # Só sera executado quando while for falso

while x < 10:
    if x == 3:
        print(x)
        x = + 1
        continue  # Pula para o proximo laço. A condição ainda esta ocorrendo, pq 3 é menor que 10!
    print(x)
    x = + 1
