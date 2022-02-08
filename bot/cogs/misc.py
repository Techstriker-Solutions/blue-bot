import nextcord
from nextcord.ext import commands

class misc(commands.Cog, name="Misc"):
    """Miscellaneous commands."""
    def __init__(self, client):
        self.client = client
    
    @nextcord.slash_command()
    async def ping(self,interaction: nextcord.Interaction):
        await interaction.response.send_message("Pong!")

def setup(client):
    client.add_cog(misc(client))