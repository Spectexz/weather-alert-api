import requests
import uvicorn
from fastapi import FastAPI
import os
from dotenv import load_dotenv
import schedule
from pytz import timezone


load_dotenv()
#WEATHER API
api_key = os.environ.get("WEATHER_KEY_API")
get_url = 'http://api.weatherapi.com/v1/current.json'

#TELEGRAM API
telegram_bot = os.environ.get("TELEGRAM_BOT_TOKEN")
telegram_chat = os.environ.get("TELEGRAM_CHAT_ID")


app = FastAPI()


def get_weather_data(city:str):
    params = {
    "key": api_key,
    "q": city}
    response = requests.get(get_url, params=params)
    data = response.json()
    location = data.get("location", {})
    current = data.get("current", {})
    show_data = {
        "Location": location.get("name"),
        "Temperature": current.get("temp_c"),
        "Condition": current.get("condition", {}).get("text"),
        "Humidity": current.get("humidity")
    }

    return show_data

@app.get("/weather")
async def readitem(city:str):
    get_weather_data(city)


def send_alert(text:str):
    tele_url = f'https://api.telegram.org/bot{telegram_bot}/sendMessage'
    params_telegram = {
        "chat_id": telegram_chat,
        "text": text,
        "parse_mode": "Markdown"         
    }
    response = requests.post(tele_url, data=params_telegram)
    return response.json()
