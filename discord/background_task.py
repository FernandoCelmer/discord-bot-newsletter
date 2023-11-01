import json
import discord
from typing import List

from requests import get
from datetime import date

from schema import SchemaNews
from discord.configurations import Config

config = Config()


class ClientNewsletter(discord.Client):

    async def on_ready(self):
        await self.send_newsletter()
        await self.close()

    async def send_newsletter(self):
        channel = client.get_partial_messageable(
            config.discord_channel_id
        )

        for news in self.get_newsletter():
            embed = discord.Embed(
                title=news.title,
                description=news.description,
                url=news.url
            )
            embed.add_field(name='Category', value=news.category)
            embed.add_field(name='Date', value=news.scheduled)
            embed.set_thumbnail(url=news.thumbnail)

            await channel.send(embed=embed)

    @staticmethod
    def get_newsletter() -> List[SchemaNews]:
        response = get(
            url=f'{config.api_url}/v1/news',
            params={'scheduled': str(date.today())}
        )
        if response.status_code == 200:
            data = json.loads(response.text)
            return [SchemaNews(**news) for news in data]
        return []


if __name__ == '__main__':
    intents = discord.Intents.default()
    intents.message_content = True

    client = ClientNewsletter(intents=intents)
    client.run(config.discord_token)
