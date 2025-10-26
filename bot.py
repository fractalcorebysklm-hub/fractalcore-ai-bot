from server import keep_alive
import discord
from discord.ext import commands
import os

keep_alive()

intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    print(f"✅ FractalCore AI connecté en tant que {bot.user}")

@bot.command()
async def analyse(ctx, *, question):
    await ctx.send(f"🧠 FractalCore AI réfléchit à : **{question}** …")
    await ctx.send("✨ Lecture fractale du marché en cours... (prototype en ligne)")

bot.run(os.getenv("DISCORD_TOKEN"))
