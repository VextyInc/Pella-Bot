import discord
from discord.ext import commands
from config import DISCORD_TOKEN, TARGET_CHANNEL_ID
from data_handler import load_data, find_best_answer
from nsfw_filter import is_nsfw

import os
from datetime import datetime

# Load datasets
dataset1 = load_data('data/PellaData1.json')
dataset2 = load_data('data/PellaData2.json')
datasets = [dataset1, dataset2]

# Create a bot instance
intents = discord.Intents.default()
intents.messages = True
bot = commands.Bot(command_prefix='!', intents=intents)

# Log file setup in the 'data' folder
log_file_path = 'data/message_logs.txt'

# Ensure the 'data' folder exists
os.makedirs(os.path.dirname(log_file_path), exist_ok=True)

def log_message_to_file(message):
    """Logs messages to a file with a timestamp and username."""
    with open(log_file_path, 'a') as log_file:
        log_entry = f"[{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}] {message.author.name}: {message.content}\n"
        log_file.write(log_entry)

@bot.event
async def on_ready():
    print(f'Logged in as {bot.user}!')

@bot.event
async def on_message(message):
    # Check if the message is from the target channel
    if message.channel.id == TARGET_CHANNEL_ID:
        if not message.author.bot:  # Ignore messages from the bot itself
            # Log the message to the file
            log_message_to_file(message)
            
            # Check for NSFW content
            if is_nsfw(message.content):
                await message.channel.send("NSFW content detected and blocked.")
                return
            
            # Process the question-answer logic
            question = message.content
            answer = find_best_answer(question, datasets)

            if answer:
                await message.channel.send(answer)
            else:
                await message.channel.send("Could you give me more context so I can help answer your question?")

    await bot.process_commands(message)

# Run the bot
bot.run(DISCORD_TOKEN)
