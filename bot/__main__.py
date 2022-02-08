import nextcord, os
from nextcord.ext import commands
from dotenv import load_dotenv

load_dotenv()
        
async def run():
    client = commands.Bot(command_prefix="/")

    @client.event
    async def on_ready():
        print("Bot is ready!")
        
    for filename in os.listdir('./bot/cogs'):
        if filename.endswith('.py'):
            client.load_extension(f'cogs.{filename[:-3]}')
    client.run(os.getenv('TOKEN'))

run()
