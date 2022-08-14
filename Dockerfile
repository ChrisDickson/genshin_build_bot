FROM python:3
FROM gorialis/discord.py
ENV PYTHONUNBUFFERED=1
RUN mkdir -p /code
WORKDIR /code/
COPY requirements.txt /code/
RUN pip install -r requirements.txt
COPY . .

CMD [ "python3", "genshin_bot.py" ]