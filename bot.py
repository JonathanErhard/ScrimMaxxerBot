import discord
import responses

async def send_message(message, user_message):
    try:
        response = responses.handle_response(user_message)
        #await message.response.send_message(content=user_message,ephemeral=True) if is_secret else await message.channel.send(user_message) #, ephemeral=True idk wieso das nicht existiert
        await message.author.send(response)
    except Exception as e:
        print(e)

def run_discord_bot():
    TOKEN = ''

    intents = discord.Intents.default()
    intents.message_content = True
    client = discord.Client(intents=intents)

    @client.event
    async def on_ready():
        print(f'{client.user} is now running')


    @client.event
    async def on_message(message):
        if message.author == client.user:
            return
        
        #username = str(message.author)
        user_message = str(message.content)
        #channel = str(message.channel)

        #if user_message[0] == '!':
        #    user_message = user_message[1:]
        #    await send_message(message, user_message, True)
        #else:
        #    if user_message[0] == '$':
        #        await send_message(message, user_message, False)
        await send_message(message,user_message)
    client.run(TOKEN)