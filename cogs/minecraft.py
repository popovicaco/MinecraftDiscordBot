import discord
from discord.ext import commands

class MinecraftCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def bedwars(self, ctx , arg1 = None , *,args = None):
        '''Generates a bedwars team! '''
        if arg1 not in ['2','3','4'] or len(args) == 0 or arg1 == None:
            await ctx.send("Invalid Argument! (try $bedwars (2/3/4) (player1) (player 2) ... (player n))")
        
        else:

            def teamrandomizer(gametype, teamstring):
                ''' randomizes a list of players into a bedwars team '''
                
                if gametype == 2: teammatrix = [['Empty','Empty'] for i in range(8)]
                elif gametype == 3: teammatrix = [['Empty','Empty','Empty'] for i in range(4)]
                elif gametype == 4: teammatrix = [['Empty','Empty','Empty','Empty'] for i in range(4)]

                import random

                playerlist = teamstring.split()

                for i in range(0,len(teammatrix)):
                    for j in range(0,len(teammatrix[0])):
                        if len(playerlist) != 1:
                            n = random.randint(0,len(playerlist)-1)
                            player = playerlist.pop(n)
                            teammatrix[i][j] = player
                        elif len(playerlist) == 1:
                            teammatrix[i][j] = playerlist[0]
                            return teammatrix

            playermatrix = teamrandomizer(int(arg1), args)

            embed=discord.Embed(title="Minecraft Bedwars Teams", color=0xf6d0d0)
            embed.set_author(name="Aco's Slave", icon_url="https://www.canteach.ca/minecraft-pe/images/bed.gif")

            embedstring = ''
            for i in range(0,len(playermatrix)):
                for item in playermatrix[i]:
                    if item != 'Empty': embedstring += item + ' '

                if embedstring != '':
                    team = 'Team ' + str(i+1)
                    embed.add_field(name=team, value=embedstring, inline=False)
                    embedstring = ''

            await ctx.send(embed=embed)


            

            





def setup(bot):
    bot.add_cog(MinecraftCog(bot))





    
