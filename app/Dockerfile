ARG APP_PATH=/usr/src

FROM python:3.11
ARG APP_PATH

COPY . $APP_PATH

WORKDIR $APP_PATH
EXPOSE 8000

RUN pip install -r $APP_PATH/app/requirements.txt --no-cache-dir

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]