import discord
from discord.ext import commands
import time
import os


if __name__ == "__main__":

    try:
        token = os.getenv("BOTTOKEN")
    except:
        from dotenv import load_dotenv
        load_dotenv()
        token = os.environ.get("BOTTOKEN")

    bot = commands.Bot(command_prefix='.')
    bot.filepath = f"{os.path.split(os.getcwd())[0]}/{os.path.split(os.getcwd())[1]}"

    initial_extensions = ['cogs.minecraft','cogs.random','cogs.mbti']
    print('----------------------')
    for extension in initial_extensions:
        bot.load_extension(extension)
        print(f'{extension} has been loaded')
    print('----------------------')

    @bot.event
    async def on_ready():
        print('We have logged in as {0.user}'.format(bot))
        await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.listening, name=".help to get started"))


    #shutdown command
    @bot.command(name= 'shutdown')
    @commands.is_owner()
    async def shutdown(ctx):
        embed=discord.Embed(title="Bye Bye!", color=0xf6d0d0)
        embed.set_author(name="Aco's Slave", icon_url="https://images-wixmp-ed30a86b8c4ca887773594c2.wixmp.com/f/55660762-c858-4a1b-9239-4e143f216fa4/ddwnzx6-5314b6a6-42bd-42cb-aea1-2f5454fefa60.gif?token=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJzdWIiOiJ1cm46YXBwOiIsImlzcyI6InVybjphcHA6Iiwib2JqIjpbW3sicGF0aCI6IlwvZlwvNTU2NjA3NjItYzg1OC00YTFiLTkyMzktNGUxNDNmMjE2ZmE0XC9kZHdueng2LTUzMTRiNmE2LTQyYmQtNDJjYi1hZWExLTJmNTQ1NGZlZmE2MC5naWYifV1dLCJhdWQiOlsidXJuOnNlcnZpY2U6ZmlsZS5kb3dubG9hZCJdfQ.xwXBhOz1dkd7hpBYabmvJp1YQaIDIokNT0TqPhKTww4")
        embed.add_field(name="Current Time", value=time.strftime("%a, %d %b %Y %H:%M:%S"), inline=False)
        embed.add_field(name='-----------------------------------------------------', value='[Source Code](https://github.com/popovicaco/MinecraftDiscordBot) |  [Discord](https://discord.gg/9tGrGHRFMJ)  |  **created by aco#1225**', inline=False)
        await ctx.send(embed = embed)
        await bot.logout()

    #reload comamnd
    @bot.command()
    @commands.is_owner()
    async def reload(ctx, cog):
        try:
            bot.reload_extension(f"cogs.{cog}")
            await ctx.send(f"The extension cogs.{cog} was reloaded")
        except:
            await ctx.send(f"The extension cogs.{cog} could not be reloaded or does not exist")

    #shows loaded cogs
    @bot.command()
    @commands.is_owner()
    async def listcogs(ctx):
        embed = discord.Embed(title='Loaded Extensions', color=0xf6d0d0)
        embed.set_thumbnail(url = "https://bestanimations.com/media/gears/1789323762silver-gear-cogs-animation-5.gif")
        for extension in initial_extensions:
            embed.add_field(name=f'{extension} is loaded', value=time.strftime("%a, %d %b %Y %H:%M:%S"), inline=False)
        await ctx.send(embed = embed)

    @bot.command()
    @commands.is_owner()
    async def servers(ctx):
        servers = list(bot.guilds)
        embed = discord.Embed(title="Server List", color=0xf6d0d0)
        embed.set_thumbnail(url = "https://bestanimations.com/media/gears/1789323762silver-gear-cogs-animation-5.gif")

        for server in servers:
            embed.add_field(name=f'{server.name}', value=f'{server.id}', inline=False)

        await ctx.send(embed = embed)

    bot.run(token)