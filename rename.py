import discord
import asyncio

client = discord.Client()

@client.event
async def on_ready():
    print(' ')
    print('\033[35m' + '|' + '\033[36m' + ' ready'+ '\033[39m')
    print('\033[35m' + '|' + '\033[33m' + ' Logged in as:',client.user.name)
    print('\033[35m' + '|' + '\033[33m' + ' UID:',client.user.id)
    print(' ')

@client.event
async def on_message(message):
    if message.author.id != "your id":
        return
    if message.content.startswith("-jon"):
        while True :
            await client.change_nickname(message.author, "jon x_x")
            await asyncio.sleep(.1)
            await client.change_nickname(message.author, "jon o_o")
            await asyncio.sleep(.1)
            await client.change_nickname(message.author, "jon f_f")
            await asyncio.sleep(.1)
            await client.change_nickname(message.author, "jon -_-")
            await asyncio.sleep(.1)
            await client.change_nickname(message.author, "jon ^~^")
            await asyncio.sleep(.1)
            await client.change_nickname(message.author, "jon O_o")
            await asyncio.sleep(.1)
            await client.change_nickname(message.author, "jon w_w")

client.run("token", bot=False)