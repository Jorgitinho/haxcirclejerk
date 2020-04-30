import discord
import random
import asyncio
import time
import io
import os

IDENTIFIER = [] #números de identificação do bot/servidor/canal
with open('./id.txt', 'r') as id:
    for line in id:
        if not line.startswith('#'):
            IDENTIFIER.append(line.strip())
DIRETORIO = 'hb/'
EXT_TXT = '.txt'
EXT_IMG = '.png'
BOT = IDENTIFIER[0]
SERVIDOR = IDENTIFIER[1]
CANAL = IDENTIFIER[2]
BOTNAME = 'HaxBot 🤖'
ESPERA = 10*60 #tempo base de espera entre troca de avatar em seg

class Haxboys:
    '''Classe contendo o nome, avatar e as falas do autista escolhido'''
    def __init__(self, filename = DIRETORIO+'haxboy'+EXT_TXT, avatar = DIRETORIO+'haxboy'+EXT_IMG, delimitador='"'):
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
for elemento in os.listdir(DIRETORIO):
    if EXT_TXT in elemento:
        haxboys.append(elemento[:-len(EXT_TXT)])
print(haxboys)

client = discord.Client()

#@client.event
#async def on_ready():
#    print('We have logged in as {0.user}'.format(client))
#    amigostm = await client.fetch_guild(SERVIDOR)
#    bot = None
#    async for member in amigostm.fetch_members(limit=150):
#        if BOTNAME in member.name:
#            bot = member
#    boteco = await client.fetch_channel(CANAL)
#    bot_avatar = client.user
#
#    tempo_inicial = time.time() - float('inf')
#    tempo_espera = ESPERA + abs(random.gauss(0, 1*60))
#    canal = boteco
#    mensagens = 1
#
#    while True:
#        if time.time() - tempo_inicial > tempo_espera:
#            try:
#                escolhido = random.choice(haxboys)
#                await bot.edit(nick=escolhido.nickname)
#                print(1)
#                with open(escolhido.avatar, 'rb') as foto:
#                    await bot_avatar.edit(avatar = foto.read())
#                print(2)
#                print(escolhido.nickname+'@boteco')
#                tempo_inicial = time.time()
#                tempo_espera = ESPERA + abs(random.gauss(0, 1*60))
#                mensagens = 1
#            except Exception as e:
#                print(e)
#        if 1/mensagens >= random.random():
#            msg = str(escolhido)
#            print(escolhido.nickname+'@boteco: '+msg)
#            print(mensagens, time.time() - tempo_inicial)
#            if '#img' == msg[:4]:
#                msg = msg[4:]
#                img_path = ''
#                letra = msg[0]
#                while len(msg) > 1 and letra != ';':
#                    if letra not in ['{', '}']:
#                        img_path += letra
#                    msg = msg[1:]
#                    letra = msg[0]
#                with open('img/'+img_path, 'rb') as imagem:
#                    await canal.send(file=discord.File(imagem), content = msg[1:])
#            else:
#                await canal.send(content = msg)
#            mensagens += 1
#        await asyncio.sleep((2*ESPERA/60) + abs (3*random.gauss(0, ESPERA/60)))
#
#ree = ''
#with open('token.txt', 'r') as token:
#    client.run(token.read())
