import os
import discord
import time
import ctx
import random

from discord.ext import commands
from discord.ext.commands import bot
import asyncio
import datetime as dt

x = 0

client = discord.Client()

@client.event
async def on_ready():
    print("Ready")

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith("-hello"):
        await message.channel.send("darkness my old friend ive come to talk with you again")
        await message.channel.send("I've come to talk with you again")
        await message.channel.send("Because a vision softly creeping")
        await message.channel.send("Left its seeds while I was sleeping")
        await message.channel.send("And the vision that was planted in my brain")
        await message.channel.send("Still remains")
        await message.channel.send("Within the sound of silence")

        await message.channel.send("In restless dreams I walked alone")
        await message.channel.send("Narrow streets of cobblestone")
        await message.channel.send("'Neath the halo of a street lamp")
        await message.channel.send("I turned my collar to the cold and damp")
        await message.channel.send("When my eyes were stabbed by the flash of a neon light")
        await message.channel.send("That split the night")
        await message.channel.send("And touched the sound of silence")

        await message.channel.send("And in the naked light, I saw")
        await message.channel.send("Ten thousand people, maybe more")
        await message.channel.send("People talking without speaking")
        await message.channel.send("People hearing without listening")
        await message.channel.send("People writing songs that voices never share")
        await message.channel.send("And no one dared")
        await message.channel.send("Disturb the sound of silence")

        await message.channel.send("Fools, said I, You do not know")
        await message.channel.send("Silence like a cancer grows")
        await message.channel.send("Hear my words that I might teach you")
        await message.channel.send("Take my arms that I might reach you")
        await message.channel.send("But my words, like silent raindrops fell")
        await message.channel.send("And echoed")
        await message.channel.send("In the wells of silence")

        await message.channel.send("And the people bowed and prayed")
        await message.channel.send("To the neon god they made")
        await message.channel.send("And the sign flashed out its warning")
        await message.channel.send("In the words that it was forming")
        await message.channel.send("And the sign said, The words of the prophets are written on the subway walls")
        await message.channel.send("And tenement halls")
        await message.channel.send("And whispered in the sound of silence")

    if message.content.startswith("-hi") or message.content.startswith("-moin"):
        await message.channel.send("geh weg")

    if message.content.startswith("-enzo"):

        await message.channel.send(file=discord.File('hallo.jpeg'))

        time.sleep(2)
        await message.channel.send("und jetzt verzieh dich")
        print("done")

    if message.content.startswith("-help"):
        await message.channel.send("-help            das hier")
        await message.channel.send("-enzo            kein plan was das ist")
        await message.channel.send("-hello           lyrics")
        await message.channel.send("-hi und -moin    geh weg")

    if message.content.startswith("-image"):
        os.system("rm")
        os.system("raspistill -o image.png")
        await message.channel.send(file=discord.File('image.png'))



    if message.content.startswith("-katze") or message.content.startswith("-kadse"):
        x = random.randrange(1,6)
        if x == 1:
            await message.channel.send(file=discordFile('1.jpg'))
        if x == 2:
            await message.channel.send(file=discordFile('2.jpg'))
        if x == 3:
            await message.channel.send(file=discordFile('3.jpg'))
        if x == 4:
            await message.channel.send(file=discordFile('4.jpg'))
        if x == 5:
            await message.channel.send(file=discordFile('5.jpg'))
        if x == 6:
            await message.channel.send(file=discordFile('6.jpg'))

        x = 0

client.run("TOKEN")
