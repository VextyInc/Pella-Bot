import os
from listeners.auto_responder import AutoResponder
from dotenv import load_dotenv

# Load environment variables from the .env file
load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

# Define the path to the words.txt file
WORDS_FILE = os.path.join('assets', 'words.txt')

# Initialize and run the bot
bot = AutoResponder(WORDS_FILE)
bot.run(TOKEN)
