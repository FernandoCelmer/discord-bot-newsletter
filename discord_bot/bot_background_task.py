import discord
from discord.ext import commands

from api.api_channel import ApiChannel
from api.schema import SchemaChannel
from api.base import is_ok

from configurations import Config

intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix="/", intents=intents)


@bot.tree.command(name="subscribe", description="Subscribe Channel")
async def subscribe(interaction:discord.Interaction):
    request = ApiChannel()

    response = request.post(
        name=interaction.channel.name,
        code=str(interaction.channel_id)
    )

    if is_ok(response=response):
        await interaction.response.send_message(
            "**Subscription completed.**"
        )

    if not is_ok(response=response):
        if response.status_code == 409:
            await interaction.response.send_message(
                "**Channel subscribed again.**"
            )
            response = request.patch(
                code=str(interaction.channel_id),
                status=True
            )


@bot.tree.command(name="unsubscribe", description="Unsubscribe Channel")
async def unsubscribe(interaction:discord.Interaction):
    request = ApiChannel()

    response = request.patch(
        code=str(interaction.channel_id)
    )

    if is_ok(response=response):
        await interaction.response.send_message(
            "**Unsubscribe Channel.**"
        )
    
    if not is_ok(response=response):
        if response.status_code == 404:
            await interaction.response.send_message(
                "**Channel not found.**"
            )


@bot.event
async def on_ready():
    await bot.tree.sync()


config = Config()
bot.run(config.discord_token)
