import discord
import os
from dotenv import load_dotenv
import botUtlilities

project_folder = os.path.expanduser('~/DiscordBOT')  # adjust as appropriate
load_dotenv(os.path.join(project_folder, '.env'))

client = discord.Client()

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('hey'):
        welcome_note=botUtlilities.welcome_user(message.author)
        await message.channel.send(welcome_note)

    if message.content.startswith('!google'):
        search_result=botUtlilities.google_search(message.content.split("!google")[-1])
        await message.channel.send(search_result)

client.run(os.getenv('TOKEN'))
