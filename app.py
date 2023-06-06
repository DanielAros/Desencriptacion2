alfabeto = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','Ñ','O','P','Q','R','S','T','U','V','W','X','Y','Z']
texto_plano_num = []
num_clave = []
cifrado_suma = []
modulo = []
texto_cifrado = []
es_modulo = []
cifrado_resta = []

texto_plano = 'HELLOWORLD'
clave = 'FACULTADDEINFORMATICA'

#Encriptar texto
for i in range(len(texto_plano)):
    texto_plano_num.append(alfabeto.index(texto_plano[i]))
    num_clave.append(alfabeto.index(clave[i]))


for i in range(len(texto_plano)):
    cifrado_suma.append(texto_plano_num[i]+num_clave[i])
    if cifrado_suma[i] >= 27:
        modulo.append(cifrado_suma[i] % 27)
        es_modulo.append(True)
    else:
        modulo.append(cifrado_suma[i])
        es_modulo.append(False)
    texto_cifrado.append(alfabeto[modulo[i]])

print("".join(texto_cifrado))
print(texto_cifrado)


palabra = []
#Desencriptacion
for i in range(len(texto_cifrado)):
    if(es_modulo[i]):
        aux = modulo[i]
        modulo[i] = 27 + aux
    cifrado_resta.append(modulo[i] - num_clave[i])
    # index_letra = texto_plano_num.index(cifrado_resta[i])
    palabra.append(alfabeto[cifrado_resta[i]])

# print(texto_plano_num)
print(cifrado_resta)
print(palabra)






