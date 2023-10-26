import os
import json
import discord

from datetime import date, datetime
from dotenv import load_dotenv

load_dotenv()

DISCORD_TOKEN = os.getenv("DISCORD_TOKEN")
DISCORD_CHANNEL_ID = os.getenv("DISCORD_CHANNEL_ID")
MESSAGE = """_____
> **{title}**
Type: {type}
Link: {link}
"""

class ClientNewsletter(discord.Client):

    async def on_ready(self):
        await self.send_newsletter()
        await self.close()

    async def send_newsletter(self):
        channel = client.get_partial_messageable(DISCORD_CHANNEL_ID)
        newsletter = json.loads(
            open(file="newsletter.json", mode="r").read())[0:50]

        for news in newsletter:
            if datetime.strptime(news.get("date"), "%m-%d-%Y").date() == date.today():
                await channel.send(MESSAGE.format(**news))


if __name__ == '__main__':
    intents = discord.Intents.default()
    intents.message_content = True

    client = ClientNewsletter(intents=intents)
    client.run(DISCORD_TOKEN)
