import json
import discord
from typing import List

from requests import get
from datetime import date
from config import Config

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
                title=news['title'].rjust(50)[0:50],
                description=f"{news['description']}...",
                url=news.get('url')
            )
            embed.add_field(name='Category', value=news.get('category'))
            embed.add_field(name='Date', value=news.get('scheduled'))
            embed.set_thumbnail(url=news.get('thumbnail'))

            await channel.send(embed=embed)

    @staticmethod
    def get_newsletter() -> List[dict]:
        response = get(
            url=f'{config.api_url}/v1/news',
            params={'scheduled': str(date.today())}
        )
        if response.status_code == 200:
            return json.loads(response.text)
        return []


if __name__ == '__main__':
    intents = discord.Intents.default()
    intents.message_content = True

    client = ClientNewsletter(intents=intents)
    client.run(config.discord_token)
