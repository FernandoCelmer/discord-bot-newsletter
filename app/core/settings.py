from os import environ
from dotenv import load_dotenv


class Settings:

    def __init__(self) -> None:
        load_dotenv()

        self.api_url = self._get_api_url()
        self.discord_token = self._get_discord_token()
        self.discord_channel_id = self._get_discord_channel_id()
        self.database_url = self._get_database_url()

    def _get_api_url(self) -> str:
        return environ.get("API_URL")
    
    def _get_discord_token(self) -> str:
        return environ.get("DISCORD_TOKEN")
    
    def _get_discord_channel_id(self) -> str:
        return environ.get("DISCORD_CHANNEL_ID")

    def _get_database_url(self) -> str:
        return environ.get("DATABASE_URL", "sqlite:///./sql_app.db")
