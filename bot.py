import discord
import random
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Accessing the bot token from an environmental variable
bot_token = os.getenv('BOT_TOKEN')
user_id = int(os.getenv('USER_ID'))

# Replace 'SPECIFIC_USER_ID' with the ID of the user you want to insult
SPECIFIC_USER_ID = user_id  # example ID

# List of insults
insults = [
    "acho que hoje alguém vai dormir no sofá.",
    "????????????????",
    "deves ser meio burro.",
    "não abuses....",
    "?!",
    "hoje vais comer sopa.",
    ":rage: :rage: :rage:",
    "deixa de ser palhaço.",
    "és mesmo engraçadinho, vês?",
    "achantra mas é."
]

# Create an instance of a client with intents
intents = discord.Intents.default()
intents.message_content = True  # This is required to read message content
intents.members = True  # This is required to access member information

client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f'We have logged in as {client.user}')

@client.event
async def on_message(message):
    # Debug: Print the content of the message
    print(f"Message from {message.author}: {message.content}")

    # Check if the bot is mentioned
    if client.user.mentioned_in(message):
        print(f"Bot was mentioned in a message: {message.content}")

        # Debug: Print all members of the guild
        for member in message.guild.members:
            print(f"Member: {member.name} - ID: {member.id}")

        # Find the specific user by ID
        specific_user = message.guild.get_member(SPECIFIC_USER_ID)
        if specific_user:
            print(f"Found specific user: {specific_user.name}")
            insult = random.choice(insults)
            await message.channel.send(f"{specific_user.mention} {insult}")
        else:
            print("Specific user not found.")

# Run the bot with the token
client.run(bot_token)
