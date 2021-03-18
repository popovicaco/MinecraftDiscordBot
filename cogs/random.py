import discord
from discord.ext import commands

class RandomCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def invitelink(self, ctx):
        '''produces a discord link'''
        embed = discord.Embed(color=0xf5d1d1)
        embed.add_field(name='Invite Link', value = '[Click here to invite Bedwars Bot to your server!](https://discord.com/oauth2/authorize?client_id=783524832310329394&permissions=391232&scope=bot)')
        embed.set_thumbnail(url='https://luckynetwork.net/static/media/bedwars.135b3e56.png')
        embed.add_field(name='--------------------------------------------------', value='[Source Code](https://github.com/popovicaco/MinecraftDiscordBot) |  [Discord](https://discord.gg/9tGrGHRFMJ)  |  **created by aco#1225**', inline=False)
        await ctx.send(embed=embed)

def setup(bot):
    bot.add_cog(RandomCog(bot))

