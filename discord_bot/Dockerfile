ARG APP_PATH=/usr/src

FROM python:3.11-alpine

ARG APP_PATH

COPY . $APP_PATH

WORKDIR $APP_PATH

RUN pip install -r discord_bot/requirements.txt --no-cache-dir

CMD ["python", "discord_bot/bot_background_task.py"]