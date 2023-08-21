"""
For / Else me python
"""
variavel = ['Everton Coelho', 'Joãozinho', 'Maria']

comeca_com_J = False
for valor in variavel:
    if valor.upper().startswith('J'):  # startswith - checa se determinado valor começa com alguma letra!
        print('Começa com a letra "j"', valor)
        comeca_com_J = True
if comeca_com_J:
    print('Existe uma palavra que começa com "J"!')
else:
    print('Não existe uma palavra que começa com "J"!')
