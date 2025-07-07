import discord
from discord.ext import commands
import os

intents = discord.Intents.default()
intents.message_content = True
intents.guilds = True
intents.members = True

bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    print(f"Logged in as {bot.user}!")
    try:
        synced = await bot.tree.sync()
        print(f"Synced {len(synced)} commands")
    except Exception as e:
        print(e)

async def setup_cogs():
    await bot.load_extension("cogs.infractions")

@bot.event
async def on_connect():
    await setup_cogs()

bot.run(os.getenv("DISCORD_TOKEN"))
