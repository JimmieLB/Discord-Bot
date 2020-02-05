import os
import csv
import discord
from discord.ext import commands
from dotenv import load_dotenv

load_dotenv()

token = 'NjcwODE0ODUyNTQwOTIzOTI1.XjcbmA.GxalyHDAf0Xw9cP2Ymr2TCAdr_k'
file = "currenct.csv"
client = commands.Bot(command_prefix = ".")

async def sendError(ctx):
    await ctx.send("An ERROR has Occured")

@client.event
async def on_ready():
    print('Ready')

@client.command()
async def load(ctx, extension):
    client.load_extension(f'cogs.{extension}')

@client.command()
async def unload(ctx,extension):
    client.unload_extension(f'cogs.{extension}')

@client.command()
async def close(ctx):
    try:
        global client
        await ctx.send("Closing...")
        await client.close()
    except:
        await sendError(ctx)


for filename in os.listdir("./cogs"):
    if filename.endswith('.py'):
        client.load_extension(f'cogs.{filename[:-3]}')

client.run(token)