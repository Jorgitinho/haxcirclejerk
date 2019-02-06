import random
class Haxboys:
    def __init__(self, filename = 'hb/haxboy.txt', avatar = 'hb/haxboy.png'):
        self.falas = []
        self.nickname = filename[3:-4]
        self.avatar = avatar
        with open(filename, 'r') as fonte:
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
            try:
                haxboys.append(Haxboys(filename = 'hb/'+autista+'.txt', avatar = 'hb/'+autista+'.png'))
            except Exception as e:
                print(e)

for hb in haxboys:
    print(hb.nickname, end=': ')
    print(hb)
