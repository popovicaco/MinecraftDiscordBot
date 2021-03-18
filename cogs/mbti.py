import discord
import json
from discord.ext import commands
import os

class mbtiCog(commands.Cog):

    def __init__(self, bot):
        self.bot = bot
        self.questions = json.load(open(f"{os.path.split(os.getcwd())[0]}/{os.path.split(os.getcwd())[1]}" + "/valuableinfo/mbtiquestions.json"))
        self.answerdict = {}

    @commands.command()
    async def mbti(self, ctx):
        '''Myers-Briggs Personality Type Test '''

        def embedmaker(n):
            embed = discord.Embed(title="MBTI Test", description=self.questions[n] + '    (' + str(n+1) + '/32)',  color=0xf6d0d0)
            embed.set_author(name="Personality Test", icon_url="https://i.pinimg.com/originals/d8/a4/4f/d8a44fba200d17685c8520faf223e36a.gif")
            embed.set_footer(text="1️⃣ - Agree 2️⃣ - Somewhat Agree 3️⃣ - Neither 4️⃣ - Somewhat Disagree 5️⃣ - Disagree ")
            return embed

        message = await ctx.send(embed = embedmaker(0))

        for emoji in ['1️⃣','2️⃣','3️⃣','4️⃣','5️⃣','❌']:
            await message.add_reaction(emoji)

        self.answerdict[(message.id,ctx.message.author.id)] = []

    @commands.Cog.listener()
    async def on_reaction_add(self, reaction, user):

        # if the key exists in the dictionary
        if (reaction.message.id,user.id) in self.answerdict.keys():
            if reaction.emoji in ('1️⃣','2️⃣','3️⃣','4️⃣','5️⃣'):

                answerlist = self.answerdict[(reaction.message.id,user.id)]


                def embedmaker(n):
                    embed = discord.Embed(title="MBTI Test", description=self.questions[n] + '    (' + str(n+1) + '/32)',  color=0xf6d0d0)
                    embed.set_author(name="Personality Test", icon_url="https://i.pinimg.com/originals/d8/a4/4f/d8a44fba200d17685c8520faf223e36a.gif")
                    embed.set_footer(text="1️⃣ - Agree 2️⃣ - Somewhat Agree 3️⃣ - Neither 4️⃣ - Somewhat Disagree 5️⃣ - Disagree ")
                    return embed

                if (len(answerlist) + 1 < 31):
                    await reaction.message.edit(embed = embedmaker(len(answerlist) + 1))
                    self.answerdict[(reaction.message.id,user.id)].append(reaction.emoji)
                    await reaction.message.remove_reaction(reaction.emoji,user)
                
                else:

                    ptype = ""

                    # mbtisum
                    eiscore = 0
                    snscore = 0
                    tfscore = 0
                    jpscore = 0
                    
                    def score(emoji):
                        if emoji == '1️⃣': return 5
                        elif emoji == '2️⃣': return 2
                        elif emoji == '3️⃣': return 0
                        elif emoji == '4️⃣': return -2
                        elif emoji == '5️⃣': return -5

                    for i in range(0,len(answerlist)):
                        if (i <= 7):
                            #EXTROVERSION VS INTROVERSION every second on is an introversion q
                            if (i%2 == 0):
                                eiscore += score(answerlist[i])
                            else:
                                eiscore -= score(answerlist[i])
                        elif (8 <= i <= 15):
                            #SENSING VS INTUITION every second on is an intuition q
                            if (i%2 == 0):
                                snscore += score(answerlist[i])
                            else:
                                snscore -= score(answerlist[i])
                        elif (16 <= i <= 23):
                            #THINKING VS FEELING every second on is an feeling q
                            if (i%2 == 0):
                                tfscore += score(answerlist[i])
                            else:
                                tfscore -= score(answerlist[i])
                        else:
                            #JUDGJING VS PERCEIVING every second one is a perceiving q
                            if (i%2 == 0):
                                jpscore += score(answerlist[i])
                            else:
                                jpscore -= score(answerlist[i])

                    if (eiscore > 0): ptype += "E"
                    elif (eiscore < 0): ptype += "I"
                    else: ptype += "X"

                    if (snscore > 0): ptype += 'S'
                    elif (snscore < 0): ptype += 'N'
                    else: ptype += 'X'

                    if (tfscore > 0): ptype += 'T'
                    elif (tfscore < 0): ptype += 'F'
                    else: ptype += 'X'

                    if (jpscore > 0): ptype += 'J'
                    elif (jpscore < 0): ptype += 'P'
                    else: ptype += 'X'

                    await reaction.message.channel.send(f"{user.mention}'s MBTI Type is: {ptype}")
                    del self.answerdict[(reaction.message.id,user.id)]
                    await reaction.message.delete()


            elif (reaction.emoji == '❌'):
                del self.answerdict[(reaction.message.id,user.id)]
                await reaction.message.delete()


def setup(bot):
    bot.add_cog(mbtiCog(bot))