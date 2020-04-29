#feito com carinho por jorginho e qtinho :3
import discord
import random
import asyncio
import time
import io

ids = []
with open('./id.txt', 'r') as id:
    for line in id:
        if not line.startswith('#'):
            ids.append(line.strip())
BOT = ids[0]
AMIGOSTM = ids[1]
BOTECO = ids[2]
BOTNAME = 'HaxBot 🤖'
ESPERA = 10*60 #tempo base de espera entre as msg (em seg)

class Haxboys:
    def __init__(self, filename = 'hb/haxboy.txt', avatar = 'hb/haxboy.png'):
        self.falas = []
        self.nickname = filename[3:-4]
        self.avatar = avatar
        with io.open(filename, 'r', encoding="utf8") as fonte:
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

client = discord.Client() #Represents a client connection that connects to Discord. This class is used to interact with the Discord WebSocket and API
#server = discord.Server(id='447168484124655647')
haxboys = []
with io.open('haxboys.txt', 'r', encoding="utf8") as arquivo:
    for linha in arquivo:
        for autista in linha.split(sep=';'):
            haxboys.append(Haxboys(filename = 'hb/'+autista+'.txt', avatar = 'hb/'+autista+'.png'))

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))
    amigostm = await client.fetch_guild(AMIGOSTM)
    bot = None
    async for member in amigostm.fetch_members(limit=150):
        if BOTNAME in member.name:
            bot = member
    boteco = await client.fetch_channel(BOTECO)
    bot_avatar = client.user

    tempo_inicial = time.time() - float('inf')
    tempo_espera = ESPERA + abs(random.gauss(0, 1*60))
    canal = boteco
    mensagens = 1

    while True:
        if time.time() - tempo_inicial > tempo_espera:
            try:
                escolhido = random.choice(haxboys)
                await bot.edit(nick=escolhido.nickname)
                print(1)
                with open(escolhido.avatar, 'rb') as foto:
                    await bot_avatar.edit(avatar = foto.read())
                print(2)
                print(escolhido.nickname+'@boteco')
                tempo_inicial = time.time()
                tempo_espera = ESPERA + abs(random.gauss(0, 1*60))
                mensagens = 1
            except Exception as e:
                print(e)
        if 1/mensagens >= random.random():
            msg = str(escolhido)
            print(escolhido.nickname+'@boteco: '+msg)
            print(mensagens, time.time() - tempo_inicial)
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
        await asyncio.sleep((2*ESPERA/60) + abs (3*random.gauss(0, ESPERA/60)))

ree = ''
with open('token.txt', 'r') as token:
    client.run(token.read())
