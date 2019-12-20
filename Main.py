# Main.py Violent Thomas 12/2019 PyCharm avec Python 3.8.0

import discord
import json

client = discord.Client()

# nom du fichier contenant les dessins en ascii
PATH_JSON_ASCII = "ascii.json"

# nom du fichier contenant le token du bot
PATH_TXT_TOKEN = "token.txt"


@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))
    # ac = discord.custom_status(text="Test")
    ac = discord.Game(name=";h for help")
    await client.change_presence(activity=ac, status=discord.Status.online, afk=False)


@client.event
async def on_message(message):
    try:
        if message.author == client.user:
            return

        if message.content.startswith(';help'):
            await print_help(message)

        if message.content.startswith(';h'):
            await print_help(message)
    except Exception:
        pass


# Affiche l'aide du bot avec les commandes disponibles
# Entrée: message - objet de type discord.Message (sert pour envoyer le message sur le bon salon)
async def print_help(message):
    emb = discord.Embed()
    emb.title = ":thinking: Help"
    emb.colour = discord.Colour.blue()
    # emb.description = "description"
    emb.add_field(name=";h or ;help", value="Show this help (list of commands)", inline=False)
    emb.add_field(name=";a or ;ascii [s(mall)|m(edium)|l(arge)]",
                  value="Print one ascii art thing, optionally, you can set the size of the print. If not mentioned, a random size will be chosen",
                  inline=False)
    await message.channel.send(embed=emb)


# écrit un "ascii art" dans le chat discord.
# Entrées: message - objet de type discord.Message (sert pour envoyer le message sur le bon salon)
#          size - integer - taille du dessin (0: non spécifié (random)
#                                             1: petit
#                                             2: moyen
#                                             3: grand)
async def print_ascii_art(message, size):
    with open(PATH_JSON_ASCII) as json_file:
        data = json.load(json_file)

with open(PATH_TXT_TOKEN) as token_file:
    client.run(token_file.read())
