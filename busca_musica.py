import discord
from sensivel import *


client = discord.Client()
TOKEN = secreto.seu_token()

@client.event
async def on_ready():
    print(client.user.name)
    print("Bot online - Olá Mundo!")

@client.event
async def on_message(message):
    if message.content.startswith('!entrar'):
      try:
        canal = message.author.voice.voice_channel
        await client.join_voice_channel(canal)
      except discord.errors.InvalidArgument:
             await client.send_message(message.channel, "Você precisa esta conectado a um canal de voz!")

    if message.content.startswith('!sair'):
      try:
        canaldevoz = client.voice_client_in(message.server)
        await canaldevoz.disconnect()
      except AttributeError:
          await client.send_message(message.channel,"O bot não esta conectado em nenhum canal de voz!")


client.run(TOKEN)