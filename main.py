import discord
from discord.ext import commands
import random
import os
import PyNaCl
from sensivel import *



client = discord.Client()
TOKEN = TOKEN

@client.event
async def on_ready():
    print(client.user.name)
    print("Bot online - Olá Mundo!")

@client.event
async def on_message(message):
    if message.content.startswith('!entrar'):
      try:
        canal = message.author.voice.channel.id
        canal_ = client.get_channel(canal)
        await canal_.connect()
      except discord.errors.InvalidArgument:
             await client.send_message(message.channel, "Você precisa esta conectado a um canal de voz!")

    if message.content.startswith('!sair'):
      try:
        canaldevoz = client.voice_client_in(message.server)
        await canaldevoz.disconnect()
      except AttributeError:
          await client.send_message(message.channel,"O bot não esta conectado em nenhum canal de voz!")


client.run(TOKEN)
