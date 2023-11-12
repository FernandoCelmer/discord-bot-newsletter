import json
import discord

from typing import List
from requests import get
from datetime import date

from configurations import Config
from api.api_news import ApiNews
from api.api_channel import ApiChannel


class ClientNewsletter(discord.Client):

    async def on_ready(self):
        await self.send_newsletter()
        await self.close()

    async def send_newsletter(self):
        response_channels = ApiChannel().get(
            params={"status": 'true'}
        )
        response_news = ApiNews().get(
            scheduled=str(date.today())
        )

        for news in response_news.data:
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

            for channel in response_channels.data:
                driver = client.get_partial_messageable(channel.code)
                await driver.send(embed=embed)


if __name__ == '__main__':
    config = Config()
    intents = discord.Intents.default()
    intents.message_content = True

    client = ClientNewsletter(intents=intents)
    client.run(config.discord_token)
