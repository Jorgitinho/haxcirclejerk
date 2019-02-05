#feito com carinho por jorginho e qtinho :3
import random
import time

class Haxboys:
    def __init__(self, filename = 'hb/haxboy.txt', avatar = 'hb/haxboy.png'):
        self.falas = []
        self.nickname = filename[3:-4]
        self.avatar = avatar
        with open(filename, 'r', encoding = 'latin-1') as fonte:
            hashtag = False
            contador = 0
            frase = ''
            for linha in fonte:
                for letra in linha:
                    if letra == '"':
                        hashtag = not hashtag
                        contador += 1
                    if hashtag:
                        if letra != '"':
                            frase += letra
                    if contador == 2:
                        self.falas.append(frase)
                        frase = ''
                        contador = 0
        self.falas_copia = self.falas[:]
    def __str__(self):
        if len(self.falas_copia) == 0:
            self.falas_copia = self.falas[:]
        mensagem = self.falas_copia.pop(random.randint(0, len(self.falas_copia) - 1))
        return mensagem

haxboys = []
with open('haxboys.txt', 'r', encoding = 'latin-1') as arquivo:
    for linha in arquivo:
        for autista in linha.split(sep=';'):
            haxboys.append(Haxboys(filename = 'hb/'+autista+'.txt', avatar = 'hb/'+autista+'.png'))
for i in haxboys:
    print(i.falas)
