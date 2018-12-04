import discord
import os
from keep_alive import keep_alive

client = discord.Client()   # Object to communicate with discord server

# Pieces of code are run in response to events
@client.event
async def on_ready(): # When bot joins server
    print("I'm in")
    print(client.user)

@client.event
async def on_message(message): # When a new message is received
    if message.author != client.user:
        await client.send_message(message.channel, message.content[::-1])

keep_alive() 
token = os.environ.get("DISCORD_BOT_SECRET")
client.run(token) # Tells bot to start up 