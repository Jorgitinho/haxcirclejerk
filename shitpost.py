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
MU = 0 #parametro pra random.gauss
SIGMA = 600 #parametro pra random.gauss

class Haxboys:
    '''Classe contendo o nome, avatar e as falas do autista escolhido'''
    def __init__(self, filename = DIRETORIO+'haxboy'+EXT_TXT,
            avatar = DIRETORIO+'haxboy'+EXT_IMG, delimitador='"'):
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

'''Preenche a lista HAXBOYS com o nome dos usuários
    (pegos dos arquivos *EXT_TXT em DIRETORIO) e cria
    uma lista auxiliar (de ordem aleatoria) haxboys'''
HAXBOYS = []
for elemento in os.listdir(DIRETORIO):
    if EXT_TXT in elemento:
        HAXBOYS.append(elemento[:-len(EXT_TXT)])
haxboys = random.shuffle(HAXBOYS[:])

client = discord.Client()
@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))
    amigostm = await client.fetch_guild(SERVIDOR)
    bot = None
    #cria o membro bot (referente ao bot)
    async for member in amigostm.fetch_members():
        if BOTNAME in member.name:
            bot = member
    canal = await client.fetch_channel(CANAL)
    bot_user = client.user
    #define o tempo entre troca de personagem
    #começa como -inf pra dar primeiro condicional ser satisfeito
    tempo_inicial = time.time() - float('inf')
    tempo_espera = ESPERA + abs(random.gauss(MU, SIGMA)) #espera de no min ESPERA seg
    mensagens = 1 #contador de mensagens

    while True:
        #Seleciona (e remove) um haxboy
        if len(haxboys) == 0:
            haxboys = random.shuffle(HAXBOYS[:])
        if time.time() - tempo_inicial > tempo_espera:
            try:
                escolhido = haxboys.pop()
                await bot.edit(nick=escolhido.nickname)
                with open(escolhido.avatar, 'rb') as foto:
                    await bot_user.edit(avatar = foto.read())

                print(escolhido.nickname+'@boteco')
                tempo_inicial = time.time()
                tempo_espera = ESPERA + abs(random.gauss(MU, SIGMA))
                mensagens = 1
            except Exception as e:
                print(e)

        #envia a mensagem se 1/n >= um numero aleatorio entre 0 e 1
        if 1/mensagens >= random.random():
            msg = str(escolhido)
            delta = time.time() - tempo_inicial
            print(escolhido.nickname+'@boteco: '+msg+' ({}) ({}m {}s)'.format(
                mensagens, delta // 60, delta % 60))
            #insere imagem, se contida na mensagem
            if '#img' == msg[:4]:
                msg = msg[4:]
                img_path = ''
                letra = msg[0]
                while len(msg) > 1 and letra != ';':
                    if letra not in ['{', '}']:
                        img_path += letra
                    msg = msg[1:]
                    letra = msg[0]
                with open('img/'+img_path, 'rb') as imagem:
                    await canal.send(file=discord.File(imagem), content = msg[1:])
            else:
                await canal.send(content = msg)
            mensagens += 1
        await asyncio.sleep(abs(random.gauss(MU, SIGMA)))

with open('token.txt', 'r') as token:
    client.run(token.read())
