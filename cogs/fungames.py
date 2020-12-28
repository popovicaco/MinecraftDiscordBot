import discord
from discord.ext import commands


#NOT YET IMPLEMENTED PERSONALITY TEST

class FunGamesCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    n = 0
    answerlist = []
    inuse = False
    
    @commands.command()
    async def mbti(self, ctx):
        '''Myers-Briggs Personality Type Test '''
        
        global inuse

        if inuse: await ctx.send('The MBTI Test is in use!')

        else:
            inuse = True
            def embedmaker(n):
                QuestionBank = [
                #EXTROVERSION VS INTROVERSION every second on is an introversion q
                'You enjoy enviroments with lots of people.',
                'You prefer to work alone rather than in teams.',
                'After a long week, you enjoy going out with friends.',
                "At a party, you're likely to stick with close friends rather than talk to new people.",
                'You find yourself carrying conversations with others.',
                'You enjoy quiet, intimate spaces.',
                'You enjoy having a wide circle of aquaintences.',
                'You find it difficult to talk to strangers.',

                #SENSING VS INTUITION every second on is an intuition q
                "You'd rather learn applications of subjects than learn the theory.",
                "You find yourself focusing on what-ifs rather than present reality.",
                "You focus on details rather than the big picture.",
                "You find yourself wondering about other worlds and realities.",
                "You enjoy non-fiction pieces.",
                "You explain concepts though analogies and metaphors rather than examples and facts.",
                "You'd rather stick to  routine procedure then experiment with new procedure.",
                "Your work flow comes in bursts of energy.",
                
                #THINKING VS FEELING every second q is a feeling q
                "You value justice and fairness",
                "You describe yourself as a warm and empathetic individual.",
                "You make descisions based on logic rather than feeling.",
                "When making a descision, you value how your action will affect others.",
                "In a group, the task at hand is more important than the journey to complete that task",
                "You enjoy working in a team to acheive a common goal.",
                "You try to be fair and just in descisions, regardless of personal connections.",
                "Your relationships with others are vital to your experience in the world.",

                #JUDGING VS PERCEIVING every second q is a feeling q
                "You believe rules are to be upheld and enforced.",
                "You prefer to improvise rather than plan your approach.",
                "On a trip, you're most likely to make a thoughtful itinerary of your events.",
                "You work best under pressure.",
                "You have a very methodical approach to life.",
                "The plans you make are flexible and open to change.",
                "You start tasks early and your efforts are sustained till deadline.",
                "You dislike being stuck to a plan and enjoy freedom.",
                ]

                embed = discord.Embed(title="MBTI Test", description=QuestionBank[n] + '    (' + str(n+1) + '/32)',  color=0xf6d0d0)
                embed.set_author(name="Personality Test", icon_url="https://i.pinimg.com/originals/d8/a4/4f/d8a44fba200d17685c8520faf223e36a.gif")
                embed.set_footer(text="1️⃣ - Agree 2️⃣ - Somewhat Agree 3️⃣ - Neither 4️⃣ - Somewhat Disagree 5️⃣ - Disagree ")
                return embed

            message = await ctx.send(embed = embedmaker(n))

            for emoji in ['1️⃣','2️⃣','3️⃣','4️⃣','5️⃣','❌']:
                await message.add_reaction(emoji)

            message_id = message.id
            author_id = ctx.message.author.id

            # defining a bot event to check for if the user adds a desired reaction
            @commands.Cog.listener()
            async def on_reaction_add(reaction, user):
                if reaction.message.id == message_id and user.id == author_id:
                    if reaction.emoji in ['1️⃣','2️⃣','3️⃣','4️⃣','5️⃣']:
                        global n
                        global answerlist
                        global inuse

                        if n == 31:
                            
                            
                            def mbtisum(nestedemojimatrix):
                                ''' returns MBTI TYPE'''
                                # score > 0 is the left personality, otherwise right
                                EISCORE = 0
                                SISCORE = 0
                                TFSCORE = 0
                                JPSCORE = 0

                                def score(emoji):
                                    if emoji == '1️⃣': return 5
                                    elif emoji == '2️⃣': return 2
                                    elif emoji == '3️⃣': return 0
                                    elif emoji == '4️⃣': return -2
                                    elif emoji == '5️⃣': return -5
                                
                                for i in range(0,len(nestedemojimatrix)):

                                    if i <= 7:
                                        #EXTROVERSION VS INTROVERSION every second on is an introversion q
                                        if i in [0,2,4,6]:
                                            EISCORE += score(nestedemojimatrix[i])
                                        else:
                                            EISCORE -= score(nestedemojimatrix[i])
                                    elif i >= 8 and i <= 15:
                                        #SENSING VS INTUITION every second on is an intuition q
                                        if i in [8,10,12,14]:
                                            SISCORE += score(nestedemojimatrix[i])
                                        else:
                                            SISCORE -= score(nestedemojimatrix[i])
                                    elif i >= 16 and i <= 23:
                                        #THINKING VS FEELING every second q is a feeling q
                                        if i in [16,18,20,22]:
                                            TFSCORE += score(nestedemojimatrix[i])
                                        else:
                                            TFSCORE -= score(nestedemojimatrix[i])
                                    else:
                                        #JUDGING VS PERCEIVING every second q is a feeling q
                                        if i in [24,26,28,30]:
                                            JPSCORE += score(nestedemojimatrix[i])
                                        else:
                                            JPSCORE -= score(nestedemojimatrix[i])

                                type = ''

                                if EISCORE > 0: type += 'E'
                                elif EISCORE < 0: type += 'I'
                                else: type += 'X'

                                if SISCORE > 0: type += 'S'
                                elif SISCORE < 0: type += 'N'
                                else: type += 'X'

                                if TFSCORE > 0: type += 'T'
                                elif TFSCORE < 0: type += 'F'
                                else: type += 'X'

                                if JPSCORE > 0: type += 'J'
                                elif JPSCORE < 0: type += 'P'
                                else: type += 'X'

                                return type

                            await ctx.send(f"{ctx.author.mention}'s MBTI Type is: {mbtisum(answerlist)}")
                            await message.delete()
                            answerlist = []
                            n = 0

                            inuse = False

                        else:
                            n += 1
                            await message.edit(embed=embedmaker(n))
                            answerlist.append(reaction.emoji)
                            await message.remove_reaction(reaction.emoji,user)

                    elif reaction.emoji == '❌':
                        await message.delete()
                        
                        inuse = False

def setup(bot):
    bot.add_cog(FunGamesCog(bot))