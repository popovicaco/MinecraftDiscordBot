import discord
from discord.ext import commands

class OwnerCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name= 'gay')
    async def gay(self, ctx):
        await ctx.send(f'{ctx.author.mention} is gay')
        
def setup(bot):
    bot.add_cog(OwnerCog(bot))
