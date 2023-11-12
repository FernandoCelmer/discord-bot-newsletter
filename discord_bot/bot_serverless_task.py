import json
import discord

from typing import List
from requests import get
from datetime import date

from configurations import Config
from api.api_news import ApiNews

config = Config()


class ClientNewsletter(discord.Client):

    async def on_ready(self):
        await self.send_newsletter()
        await self.close()

    async def send_newsletter(self):
        request = ApiNews()
        response = request.get(
            scheduled=str(date.today())
        )

        channel = client.get_partial_messageable(
            config.discord_channel_id
        )
        
        for news in response.data:
            embed = discord.Embed(
                title=news.title,
                description=news.description,
                url=news.url
            )
            embed.set_author(
                name="Newsletter",
                url="https://github.com/FernandoCelmer/discord-bot-newsletter"
            )     
            embed.set_thumbnail(url=news.thumbnail)
            embed.add_field(name='Category', value=news.category)
            embed.add_field(name='Date', value=news.scheduled)

            await channel.send(embed=embed)


if __name__ == '__main__':
    intents = discord.Intents.default()
    intents.message_content = True

    client = ClientNewsletter(intents=intents)
    client.run(config.discord_token)
