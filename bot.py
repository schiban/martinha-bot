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
    "vai para a puta que te pariu!",
    "és um filho da puta!",
    "vai-te foder!",
    "és um cabrão de merda!",
    "vai levar no cu!",
    "és um monte de merda!",
    "és um atrasado mental!",
    "és uma aberração!",
    "és um nojento de merda!",
    "Não vales um caralho!",
    "vai-te encher de moscas!",
    "és um pedaço de merda ambulante!",
    "és um chulo de merda!",
    "és um grande filho da mãe!",
    "és um cagalhão!",
    "vai mamar na quinta pata do cavalo!",
    "és um sacana!",
    "és um anormal do caralho!",
    "vai apanhar no cu!",
    "és um verme rastejante!",
    "és um aborto mal feito!",
    "és um atrasado de merda!",
    "és um estupor!",
    "és um grandessíssimo cabrão!",
    "vai levar no pacote!",
    "és um grande conas!",
    "és uma puta barata!",
    "és um escroto humano!",
    "és um cancro ambulante!",
    "és um pedaço de bosta!",
    "és um inútil do caralho!",
    "és um grande sacana!",
    "és uma merda seca!",
    "és um chulo filho da puta!",
    "vai morrer longe!",
    "és um verme insignificante!",
    "és um farrapo humano!",
    "és um cabrão de primeira!",
    "és uma desgraça ambulante!",
    "vai cagar à mata!",
    "és um puto de merda!",
    "és um conas de sabão!",
    "és um otário de merda!",
    "és um aborto da sociedade!",
    "vai-te lixar, cabrão!",
    "és uma besta do caralho!",
    "és um monte de esterco!",
    "és um nojento filho da puta!",
    "és uma aberração da natureza!",
    "acho que hoje alguém vai dormir no sofá.",
    "????????????????",
    "deves ser meio burro.",
    "não abuses....",
    "?!",
    ":rage: :rage: :rage:",
    "deixa de ser palhaço.",
    "és mesmo engraçadinho, vês?",
    "9 years, eh? Wow. 9 years ago you were autistic. exactly 9 years ago I looked at you and I was like: wow, what a fucking spastic, chromossome lacking fucking herrera lookin ass motherfucker. 9 years later i still think that tbh. it's been 9 years of me being your friend and to this day, I still don't know why. hopefully soon you'll realize how much of a cumsock you are, and finally begin your steps towards changing into a man. here's to 9 years more, brother kkonacool"
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
    # Check if the bot is mentioned
    if client.user.mentioned_in(message):

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
