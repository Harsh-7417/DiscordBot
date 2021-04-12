import discord
import botUtlilities # module having all services or utilities
import os

client = discord.Client()


@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))


@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.lower().startswith('!hey'):
        welcome_note = botUtlilities.welcome_user(str(message.author))
        await message.channel.send(welcome_note)

    if message.content.startswith('!google'):
        search_filter = message.content.split("!google")[-1]  # to get text to be searched on google
        search_result = botUtlilities.google_search(search_filter)
        botUtlilities.add_history(user_id=str(message.author),
                                  search_filter=search_filter)  # add search text in mongo DB
        await message.channel.send(search_result)

    if message.content.startswith('!recent'):
        search_filter = message.content.split("!recent")[-1]  # to get text to be searched for history
        search_result = botUtlilities.recent_search(user_id=str(message.author), search_filter=search_filter)
        await message.channel.send(search_result)


client.run(os.getenv('TOKEN'))
