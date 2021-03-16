import discord
from discord.ext import commands
import random
from collections import defaultdict
from math import floor


class MinecraftCog(commands.Cog):

    def __init__(self,bot):
        self.bot = bot
        self.colors = ['red', 'blue', 'green', 'yellow', 'aqua', 'white', 'pink', 'grey']
        self.players = None
        self.number_of_teams = 0

    @commands.command()
    def bedwars(self, ctx, arg1, args):
        '''Generates a bedwars team! '''
        # Changed list to set so that it's a constant lookup
        if arg1 not in ('2','3','4') or len(args) == 0 or arg1 == None:
            await ctx.send("Invalid Argument! (try $bedwars (2/3/4) (player1) (player 2) ... (player n))")
        
        else:
            player_dict = self.teamrandomizer(int(arg1), args)
            if not player_dict:
                await ctx.send("There are too many players")
                return
            
            self.players = args
            self.number_of_teams = arg1

            embed=discord.Embed(title="Minecraft Bedwars Teams", color=0xf6d0d0)
            embed.set_author(name="Aco's Slave", icon_url="https://www.canteach.ca/minecraft-pe/images/bed.gif")

            embedstring = ' '
            for key, values in player_dict.items():
                team = key
                embedstring.join(values)
                embed.add_field(name=team, value=embedstring, inline=False)

            await ctx.send(embed=embed)



    def teamrandomizer(self, gametype, teamstring):
        ''' randomizes a list of players into a bedwars team '''

        # Making a list for max number of players is wasteful if you don't reach the quota
        # Use default dictionary to be more effecient and allows you to assign colors to the teams

        playerlist = teamstring.split(',')
        self.players = playerlist
        team_generation = defaultdict(list)
        too_many_players = False
        if gametype == 2:
            # Use all colors to make teams
            team_colors = self.colors[:]
            if len(playerlist) > 16:
                too_many_players = True
                
        else:
            # Take only the 4 possible colors and spread teams evenly to them
            team_colors= self.colors[0:4]
            if (gametype == 3 and len(playerlist) > 12) or (gametype == 4 and len(playerlist) > 16):
                too_many_players = True

        if too_many_players:
            return None
                
        # Shuffle both the playerlist and teams colors to just add them to the list
        random.shuffle(playerlist)
        random.shuffle(team_colors)
        # Generate only as many teams as possible/ needed
        max_teams = ceil(len(playerlist)/gametype)        

        for i, x in enumerate(playerlist):
            team_generation[team_colors[i % max_teams]].append(x)

        return team_generation

    @commands.command()
    async def reroll(self, ctx, new_number_of_teams=None):
        if(new_number_of_teams is None):
            self.bedwars(self.number_of_teams, self.players)
        else:
            self.bedwars(new_number_of_teams, self.players)




def setup(bot):
    bot.add_cog(MinecraftCog(bot))





    
