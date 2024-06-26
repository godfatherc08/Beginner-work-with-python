import os

import discord
from discord import member


TOKEN = os.environ['Token']
GUILD = os.getenv('Bermuda')

bot = discord.Client()


@bot.event
async def on_ready():
    guild = discord.utils.get(bot.guilds, name = GUILD)

    print(f'{bot.user} has connected to Discord!')
    print(f'{bot.user} is for the sole purpose of conversing with members of this server, encouraging'
          f'them and promoting good vibes. Keeping the peace with a simple Hello')

@bot.event
async def on_member_join():
    await member.create_dm()
    await member.dm_channel.send(
        print(f'{member.name}, you are welcome to Bermuda')
    )

@bot.event
async def on_message():
    pass

bot.run(TOKEN)