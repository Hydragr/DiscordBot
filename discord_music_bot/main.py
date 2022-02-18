import discord
from discord.ext import commands
import music

cogs = [music]

client = commands.Bot(command_prefix = '!', intents = discord.Intents.all())

for i in range(len(cogs)):
  cogs[i].setup(client)


client.run("ODk1MzI0ODI1ODk0MTMzODEx.YV26OA.zMHUOF-g1Fnltz4OiHibzZW4dmQ")