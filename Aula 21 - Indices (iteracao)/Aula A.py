"""
Indices
         0123456789.......................33
"""
frase = 'O rato roeu a roupa do rei de roma'  # Valores iteravel
tamanho_frase = len(frase)
nova_string = ''  # str vazia

contador = 0

# while contador < tamanho_frase:
#     #print(frase[contador], contador)
#     nova_string += frase[contador]  # Esta copiando a string
#     contador += 1
#     print(nova_string)
# print(nova_string)

#iteração
while contador < tamanho_frase:
    letra = frase[contador]
    if letra == 'r':
        nova_string += 'R'  # Se tiver r na frase, vai substituir por R
    else:
        nova_string += letra
    contador += 1
    print(nova_string)
print(nova_string)
