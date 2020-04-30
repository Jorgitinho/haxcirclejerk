import random
import io

class Haxboys:
    def __init__(self, filename = 'hb/haxboy.txt', avatar = 'hb/haxboy.png', delimitador='"'):
        self.falas = []
        self.nickname = filename[3:-4]
        self.avatar = avatar
        with io.open(filename, 'r', encoding="utf8") as fonte:
            for linha in fonte:
                frase = ''
                for letra in linha.strip():
                    if letra != delimitador:
                        frase += letra
                self.falas.append(frase)
        self.falas_copia = self.falas[:]
        random.shuffle(self.falas_copia)
    def __str__(self):
        if len(self.falas_copia) == 0:
            self.falas_copia = self.falas[:]
            random.shuffle(self.falas_copia)
        mensagem = self.falas_copia.pop()
        return mensagem

haxboys = []
with open('haxboys.txt', 'r') as arquivo:
    for linha in arquivo:
        for autista in linha.split(sep=';'):
            haxboys.append(Haxboys(filename = 'hb/'+autista+'.txt', avatar = 'hb/'+autista+'.png'))

for hb in haxboys:
    print(hb.nickname, end=': ')
    print(hb)
