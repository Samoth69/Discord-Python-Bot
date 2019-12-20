# Main.py Violent Thomas 12/2019 PyCharm avec Python 3.8.0
from random import randint

import discord
import json

client = discord.Client()

# name of the file with ascii drawing in it
PATH_JSON_ASCII = "ascii.json"

# discord bot token id
PATH_TXT_TOKEN = "token.txt"


# Trigger when the bot is ready to work
@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))
    # ac = discord.custom_status(text="Test")
    ac = discord.Game(name=";h for help")
    await client.change_presence(activity=ac, status=discord.Status.online, afk=False)


# Trigger when their is a message to read
@client.event
async def on_message(message):
    try:
        if message.author == client.user:
            return

        if message.content.startswith(';help'):
            await print_help(message)

        if message.content.startswith(';h'):
            await print_help(message)

        if message.content.startswith(';a'):
            await print_ascii_art(message, 1)
    except Exception:
        pass


# Show the help with the commands that you can type
# Input: message - Type: discord.Message (it's use to know where to put the message)
async def print_help(message):
    emb = discord.Embed()
    emb.title = ":thinking: Help"
    emb.colour = discord.Colour.blue()
    # emb.description = "description"
    emb.add_field(name=";h or ;help", value="Show this help (list of commands)", inline=False)
    emb.add_field(name=";a or ;ascii [s(mall)|m(edium)|l(arge)]", value="Print one ascii art thing, optionally, you can set the size of the print. If not mentioned, a random size will be chosen",
                  inline=False)
    await message.channel.send(embed=emb)


# Print an "ASCII art" thing on discord chat
# Input: message - Type: discord.Message (it's use to know where to put the message)
#        size - integer - size of the drawing (in term of height) (0: not specified (random), 1: small, 2: medium, 3: large)
async def print_ascii_art(message, size):
    with open(PATH_JSON_ASCII) as json_file:
        data = json.load(json_file)
        if size == 1:
            drawing_size = "small"
            number_of_elements = data["ascii"][drawing_size][0]["size"]
        rnd = randint(1, number_of_elements)

        await message.channel.send("**" + data["ascii"][drawing_size][rnd]["name"] + "**\n```" + data["ascii"][drawing_size][rnd]["content"] + "```")

# Load token file and then load the bot
with open(PATH_TXT_TOKEN) as token_file:
    client.run(token_file.read())
