import settings
import discord
from discord import app_commands
from discord.ext import commands

logger = settings.logging.getLogger("bot")


def run_discord_bot():
    intents = discord.Intents.all()

    bot = commands.Bot(command_prefix='!', intents=intents)

    @bot.event
    async def on_ready():
        logger.info(f"{bot.user.name} is now running!")

        bot.tree.copy_global_to(guild=settings.GUILD_ID)
        await bot.tree.sync(guild=settings.GUILD_ID)

    @bot.tree.command()
    @app_commands.describe(text_to_send="Simon says...")
    @app_commands.rename(text_to_send="message")
    async def say(interaction: discord.Interaction, text_to_send: str):
        await interaction.response.send_message(f"{text_to_send}", ephemeral=True) # noqa

    bot.run(settings.TOKEN, root_logger=True)

