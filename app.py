from random import sample
alfabeto = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','Ñ','O','P','Q','R','S','T','U','V','W','X','Y','Z']
# valores = [3,17,22,9,23,18,24,20,4,6,16,10,19,5,25,14,2,21,1,26,8,15,0,11,13,12,7]
texto_plano_num = [] #Arreglo para guardar los numeros que le corresponden
num_clave = []
cifrado_suma = []
modulo = []
texto_cifrado = []
es_modulo = []
cifrado_resta = []

texto_plano = 'HELLOWORLD'
clave = 'FACULTADDEINFORMATICA'

valores = sample(range(0,27), 27)

def encriptar():
    for i in range(len(texto_plano)):
        indice = alfabeto.index(texto_plano[i])
        texto_plano_num.append(valores[indice])
        indice = alfabeto.index(clave[i])
        num_clave.append(valores[indice])

    for i in range(len(texto_plano)):
        cifrado_suma.append(texto_plano_num[i]+num_clave[i])
        if cifrado_suma[i] >= 27:
            modulo.append(cifrado_suma[i] % 27)
            es_modulo.append(True)
        else:
            modulo.append(cifrado_suma[i])
            es_modulo.append(False)
        ind = valores.index(modulo[i])
        texto_cifrado.append(alfabeto[ind])
    print("".join(texto_cifrado))

def desencriptar():
    palabra = []
    for i in range(len(texto_cifrado)):
        if(es_modulo[i]):
            aux = modulo[i]
            modulo[i] = 27 + aux
        cifrado_resta.append(modulo[i] - num_clave[i])
        ind = valores.index(cifrado_resta[i])
        palabra.append(alfabeto[ind])
    print("".join(palabra))

encriptar()
desencriptar()



