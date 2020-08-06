# Main.py Violent Thomas 12/2019 PyCharm avec Python 3.8.0
from random import randint

import discord

client = discord.Client()

# file with the exhaustive list of files with ascii art in them
PATH_FILE_LIST = "files.txt"

# folder name with all ascii files in it
PATH_FOLDER_ASCII = "ASCII"

# discord bot token id
PATH_TXT_TOKEN = "token.txt"


# Trigger when the bot is ready to work
@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))
    # ac = discord.custom_status(text="Test")
    ac = discord.Game(name=";h for help")
    await client.change_presence(activity=ac, status=discord.Status.online, afk=False)


# Trigger when there is a message to read
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
    except Exception as err:
        print(err)
        pass


# Show the help with the commands that you can type
# Input: message - Type: discord.Message (it's use to know where to put the message)
async def print_help(message):
    emb = discord.Embed()
    emb.title = ":thinking: Help"
    emb.colour = discord.Colour.blue()
    # emb.description = "description"
    emb.add_field(name=";h or ;help", value="Show this help (list of commands)", inline=False)
    emb.add_field(name=";a or ;ascii [name]", value="Print one ascii art thing, optionally, you set a name to search. If not found or not specified, a random file will be chosen",
                  inline=False)
    await message.channel.send(embed=emb)


# Print an "ASCII art" thing on discord chat
# Input: message - Type: discord.Message (it's use to know where to put the message)
#        name - Type:string
async def print_ascii_art(message, name=""):
    with open(PATH_JSON_ASCII) as json_file:
        data = json.load(json_file)
        if size < 1 or size > 3:
            size = randint(1, 3)

        if size == 1:
            drawing_size = "small"
        elif size == 2:
            drawing_size = "medium"
        elif size == 3:
            drawing_size = "large"

        number_of_elements = data["ascii"][drawing_size][0]["size"]
        rnd = randint(1, number_of_elements)

        await message.channel.send("**" + data["ascii"][drawing_size][rnd]["name"] + "**\n```" + data["ascii"][drawing_size][rnd]["content"] + "```")


# Load token file and then load the bot
with open(PATH_TXT_TOKEN) as token_file:
    client.run(token_file.read())
