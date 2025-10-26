from server import keep_alive
import discord
from discord.ext import commands
import os

# Lancer le serveur Flask pour le keep_alive (utile sur Render)
keep_alive()

# 🔧 Intentions Discord (lecture du contenu des messages)
intents = discord.Intents.default()
intents.message_content = True

# Création du bot avec un préfixe
bot = commands.Bot(command_prefix="!", intents=intents)

# 🧠 Événement au démarrage du bot
@bot.event
async def on_ready():
    print(f"✅ FractalCore AI connecté en tant que {bot.user}")

# 🧩 Commande principale d’analyse
@bot.command()
async def analyse(ctx, *, question):
    await ctx.send(f"🧠 FractalCore AI réfléchit à : **{question}** …")
    await ctx.send("✨ Lecture fractale du marché en cours... (prototype en ligne)")

# 🔍 Vérification du token avant exécution
discord_token = os.getenv("DISCORD_TOKEN")

if discord_token:
    print("🔍 DISCORD_TOKEN chargé : True")
    try:
        bot.run(discord_token)
    except Exception as e:
        print(f"❌ Erreur lors du lancement du bot : {e}")
else:
    print("⚠️ DISCORD_TOKEN manquant ou non chargé. Vérifie les variables d'environnement Render.")
