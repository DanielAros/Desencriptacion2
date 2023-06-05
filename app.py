alfabeto = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','Ñ','O','P','Q','R','S','T','U','V','W','X','Y','Z']

dictionario_alfabeto_clave = {}

for i in range(len(alfabeto)):
    dictionario_alfabeto_clave[alfabeto[i]] = i

texto_plano = 'HELLOWORLD'
clave = 'FACULTADDEINFORMATICA'

num_texto_plano = []
num_clave = []

for i in range(len(texto_plano)):
    num_texto_plano.append(dictionario_alfabeto_clave[texto_plano[i]])
    num_clave.append(dictionario_alfabeto_clave[clave[i]])

cifrado_suma = []

for i in range(len(texto_plano)):
    cifrado_suma.append(num_texto_plano[i]+num_clave[i])

modulo = []
# modulo
for i in range(len(cifrado_suma)):
    if cifrado_suma[i] >= 27:
        modulo.append(cifrado_suma[i] % 27)
    else:
        modulo.append(cifrado_suma[i])

texto_cifrado = []
valores = []

for i in range(len(modulo)):
    valores.append(alfabeto[modulo[i]])

print("".join(valores))
