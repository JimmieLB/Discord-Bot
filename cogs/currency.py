import discord
from discord.ext import commands
from handler import Handler
class Currency(commands.Cog):

    def __init__(self,client):
        self.client = client
        self.handler = Handler("currency.csv")

    @commands.Cog.listener()
    async def on_ready(self):
        print("Currency system: Online")

    @commands.command()
    async def generate(self, ctx):
        await ctx.send(f'{round(self.client.latency * 1000)}ms')# @client.command()
    
    @commands.command()
    async def balance(self, ctx):
        # try:
        cash = 0
        name = ctx.author.name
        if self.handler.includes(name):
            cash = self.handler.balance(name)
        retStr = str(f'${cash}')
        embed = discord.Embed(title=ctx.author.name)
        embed.add_field(name="Balance: ",value=retStr)
        await ctx.send(embed=embed)
        # except:
        #     await ctx.send("An ERROR has Occured")

def setup(client):
    client.add_cog(Currency(client))