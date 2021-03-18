import discord
from discord.ext import commands

class MinecraftCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def bedwars(self, ctx , arg1 = None , *,args = None):
        '''Generates a bedwars team! '''

        if ctx.message.guild.id in [622619448339071006]:
            await ctx.send("idk the way you guys are acting in such a fake way is something I can't vibe with")
            return 0

        def teamrandomizer(gametype, teamstring):
            ''' randomizes a list of players into a bedwars team '''
            import random
            playerlist = teamstring.split()

            if gametype == 2 and len(playerlist) <= 16: teammatrix = [['Empty','Empty'] for i in range(8)]
            elif gametype == 3 and len(playerlist) <= 12: teammatrix = [['Empty','Empty','Empty'] for i in range(4)]
            elif gametype == 4 and len(playerlist) <= 16: teammatrix = [['Empty','Empty','Empty','Empty'] for i in range(4)]
            else: raise ValueError

            for i in range(0,len(teammatrix)):
                for j in range(0,len(teammatrix[0])):
                    if len(playerlist) != 1:
                        n = random.randint(0,len(playerlist)-1)
                        teammatrix[i][j] = playerlist.pop(n)
                    elif len(playerlist) == 1:
                        teammatrix[i][j] = playerlist[0]
                        return teammatrix

        try: 
            playermatrix = teamrandomizer(int(arg1), args)
            embed=discord.Embed(title="Minecraft Bedwars Teams", color=0xf6d0d0)
            embed.set_thumbnail(url='https://luckynetwork.net/static/media/bedwars.135b3e56.png')
            embedstring = ''
            for i in range(0,len(playermatrix)):
                for item in playermatrix[i]:
                    if item != 'Empty': embedstring += item + ' '

                if embedstring != '':
                    team = 'Team ' + str(i+1)
                    embed.add_field(name=team, value=embedstring, inline=False)
                    embedstring = ''
            
            embed.add_field(name='-----------------------------------------------------', value='[Source Code](https://github.com/popovicaco/MinecraftDiscordBot) |  [Discord](https://discord.gg/9tGrGHRFMJ)  |  **created by aco#1225**', inline=False)
            await ctx.send(embed=embed)


            
        except:
            embed = discord.Embed(title='ERROR! INVALID ARGUEMENT', description='```Try >bedwars 2/3/4 Player1 Player2 ...```', color=0xf5d1d1)
            embed.set_thumbnail(url='https://luckynetwork.net/static/media/bedwars.135b3e56.png')
            embed.add_field(name='Team Combinations', value='``` Doubles & Fours: Max 16 ``` ``` Triples: Max 12 ```' , inline=False)
            embed.add_field(name='-----------------------------------------------------', value='[Source Code](https://github.com/popovicaco/MinecraftDiscordBot) |  [Discord](https://discord.gg/9tGrGHRFMJ)  |  **created by aco#1225**', inline=False)
            await ctx.send(embed=embed)

def setup(bot):
    bot.add_cog(MinecraftCog(bot))

    
