import nextcord
from nextcord.ext import commands
import TokenHider

bot = commands.Bot(command_prefix=".")

@bot.command()
async def hello(ctx):
    await ctx.reply("Hello!")

bot.run(TokenHider.discordToken())