import os

import discord
from discord.ext import commands
from dotenv import load_dotenv

load_dotenv()
token = 'NjcwODE0ODUyNTQwOTIzOTI1.Xiz7XQ.zI4b7OWMpXQIf9wnbeoFsaXdRK0'

client = commands.Bot(command_prefix = ".")

@client.event
async def on_ready():
    print('Ready')

@client.command()
async def close(ctx):
    await ctx.send("Closing...")
    await client.close()

@client.command()
async def ping(ctx):
    await ctx.send(f'{round(client.latency * 1000)}ms')

@client.command()
async def test(ctx):
    retStr = str("""```css\nThis is some colored Text```""")
    embed = discord.Embed(title=client.user.name)
    embed.add_field(name="Name field can't be colored as it seems",value=retStr)
    await ctx.send(embed=embed)

client.run(token)