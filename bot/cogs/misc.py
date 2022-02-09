import nextcord
from nextcord.ext import commands

class misc(commands.Cog, name="Misc"):
    """Miscellaneous commands."""
    def __init__(self, client):
        self.client = client
    
    @nextcord.slash_command(name="ping",description="Pong!")
    async def ping(self,interaction: nextcord.Interaction):
        """Pong!"""
        await interaction.response.send_message("Pong!")

    @nextcord.slash_command(name="echo",description="Echos the message.")
    async def echo(self,interaction: nextcord.Interaction):
        """Echos the message."""
        await interaction.response.send_message(interaction.message.content)
    
    @nextcord.slash_command(name="help",description="Shows help.")
    async def help(self,interaction: nextcord.Interaction):
        """Shows help."""
        await interaction.response.send_message("```\n/ping - Pong!\n/echo - Echo the message\n/help - This message\n/source - Source Code\n```")
    
    @nextcord.slash_command(name="source",description="Shows the source code.")
    async def source(self,interaction: nextcord.Interaction):
        """Shows the source code."""
        await interaction.response.send_message("https://github.com/Techstriker-Solutions/blue-bot")

def setup(client):
    client.add_cog(misc(client))
