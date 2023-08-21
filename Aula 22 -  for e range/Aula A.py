"""
For in em Python
Iterando com str com FOR
função RANGE(start = 0, stop, step = 1)
"""
texto = 'python'

for num, letra in enumerate(texto):  # Para letra em texto
    print(num, letra)                   # mostre na tela letra

print('########')

for numero in range(0, 100, 5):
    print(numero)  #I   F   P

print('#######')

for numero2 in range(20, 9, -1):  # Contando ao contrario
    print(numero2)

print('#########')

nova_str = ''  # Trocando as letras
for letra in texto:
    if letra == 't':
        nova_str += letra.upper()
    elif letra == 'h':
        nova_str += letra.upper()
    else:
        nova_str += letra
print(nova_str)

