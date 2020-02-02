import discord
from discord.ext import commands
class Misc(commands.Cog):

    def __init__(self,client):
        self.client = client

    @commands.Cog.listener()
    async def on_ready(self):
        print("Bot is online")

    @commands.command()
    async def ping(self, ctx):
        await ctx.send(f'{round(self.client.latency * 1000)}ms')# @client.command()
    
    @commands.command()
    async def test(self, ctx):
        try:
            retStr = str("""```css\nThis is some colored Text```""")
            embed = discord.Embed(title=ctx.author.name)
            embed.add_field(name="Big",value=retStr)
            await ctx.send(embed=embed)
        except:
            await ctx.send("An ERROR has Occured")

def setup(client):
    client.add_cog(Misc(client))