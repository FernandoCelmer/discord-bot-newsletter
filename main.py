import os
import json
import discord

from datetime import date, datetime
from dotenv import load_dotenv

load_dotenv()

def load_news(limit: str = 10):
    return json.loads(
        open(file="newsletter.json", mode="r").read()
    )[0:limit]

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

        for news in load_news():
            if datetime.strptime(news.get("date"), "%m-%d-%Y").date() == date.today():
                await channel.send(MESSAGE.format(**news))

    async def on_message(self, message):
        if message.author == self.user:
            return

        if message.content == 'ping':
            await message.channel.send(message.channel.id)


if __name__ == '__main__':
    intents = discord.Intents.default()
    intents.message_content = True

    client = ClientNewsletter(intents=intents)
    client.run(DISCORD_TOKEN)
