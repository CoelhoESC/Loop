print('Calculadora')
while True:
    num1 = input('Digite um n°: ')
    num2 = input('Digite outro n°: ')
    operador = input('Digite um operador (+, -, /, *): ')
    sair = input('Deseja sair?').strip().upper()[0]

    if sair in 'S':
        break

    if not num1.isnumeric() or not num2.isnumeric():  # Verificando se digitou um número!
        print('Você precisa digitar um número!')
        continue  # volta pra o while!

    num1 = int(num1)
    num2 = int(num2)

    if operador == '+':
        print(num1 + num2)
    elif operador == '-':
        print(num1 - num2)
    elif operador == '/':
        print(num1 / num2)
    elif operador == '*':
        print(num1 * num2)
    else:
        print('Operador invalido')
