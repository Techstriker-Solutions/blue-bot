import nextcord
from nextcord.ext import commands

class misc(commands.Cog, name="Misc"):
    """Miscellaneous commands."""
    def __init__(self, client):
        self.client = client
    
    @nextcord.slash_command()
    async def ping(self,interaction: nextcord.Interaction):
        await interaction.response.send_message("Pong!")

    @nextcord.slash_command()
    async def echo(self,interaction: nextcord.Interaction):
        await interaction.response.send_message(interaction.message.content)
    
    @nextcord.slash_command()
    async def help(self,interaction: nextcord.Interaction):
        await interaction.response.send_message("```\n/ping - Pong!\n/echo - Echo the message\n/help - This message\n```")
    
    @nextcord.slash_command()
    async def source(self,interaction: nextcord.Interaction):
        await interaction.response.send_message("https://github.com/Techstriker-Solutions/blue-bot")

def setup(client):
    client.add_cog(misc(client))