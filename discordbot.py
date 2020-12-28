import discord
from discord.ext import commands
import time


initial_extensions = ['cogs.minecraft','cogs.owner']

bot = commands.Bot(command_prefix='>')

if __name__ == "__main__":
    print('----------------------')
    for extension in initial_extensions:
        bot.load_extension(extension)
        print(f'{extension} has been loaded')
    print('----------------------')

@bot.event
async def on_ready():
    print('We have logged in as {0.user}'.format(bot))
    await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.listening, name=">help to get started <3"))

    #sending message to bot channel
    channel = bot.get_channel(784316590945992728)
    embed=discord.Embed(title="Ready to go!", color=0xf6d0d0)
    embed.set_author(name="Aco's Bedwar's Bot", icon_url="https://static.tumblr.com/43d1074d00a23ab81b4c3d482f68214c/v2phbe6/rBLmhx4ea/tumblr_static_tumblr_m3jaqxw3af1rspji7o1_500.gif")
    embed.add_field(name="Current Time", value=time.strftime("%a, %d %b %Y %H:%M:%S"), inline=False)
    await channel.send(embed = embed)

#shutdown command
@bot.command(name= 'shutdown')
@commands.is_owner()
async def shutdown(ctx):
    embed=discord.Embed(title="Bye Bye!", color=0xf6d0d0)
    embed.set_author(name="Aco's Bedwar's Bot", icon_url="https://images-wixmp-ed30a86b8c4ca887773594c2.wixmp.com/f/55660762-c858-4a1b-9239-4e143f216fa4/ddwnzx6-5314b6a6-42bd-42cb-aea1-2f5454fefa60.gif?token=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJzdWIiOiJ1cm46YXBwOiIsImlzcyI6InVybjphcHA6Iiwib2JqIjpbW3sicGF0aCI6IlwvZlwvNTU2NjA3NjItYzg1OC00YTFiLTkyMzktNGUxNDNmMjE2ZmE0XC9kZHdueng2LTUzMTRiNmE2LTQyYmQtNDJjYi1hZWExLTJmNTQ1NGZlZmE2MC5naWYifV1dLCJhdWQiOlsidXJuOnNlcnZpY2U6ZmlsZS5kb3dubG9hZCJdfQ.xwXBhOz1dkd7hpBYabmvJp1YQaIDIokNT0TqPhKTww4")
    embed.add_field(name="Current Time", value=time.strftime("%a, %d %b %Y %H:%M:%S"), inline=False)
    await ctx.send(embed = embed)
    await bot.logout()
    
bot.run('BOTTOKEN GOES HERE')