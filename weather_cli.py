import argparse
import os
import requests
from dotenv import load_dotenv

load_dotenv()  # reads .env file, loads variables into environment

API_KEY = os.getenv("OPENWEATHER_API_KEY")
BASE_URL = "https://api.openweathermap.org/data/2.5/weather"

def get_weather(city):
    if not API_KEY:
        print("Error: OPENWEATHER_API_KEY not found. Check your .env file.")
        return

    params = {"q": city, "appid": API_KEY, "units": "metric"}
    response = requests.get(BASE_URL, params=params)

    if response.status_code == 200:
        data = response.json()
        temp = data["main"]["temp"]
        condition = data["weather"][0]["description"]
        print(f"{city}: {temp}°C, {condition}")
    elif response.status_code == 404:
        print(f"City '{city}' not found.")
    else:
        print(f"Error {response.status_code}: {response.json().get('message', 'unknown error')}")

def main():
    parser = argparse.ArgumentParser(description="Weather CLI")
    parser.add_argument("--city", required=True)
    args = parser.parse_args()
    get_weather(args.city)

if __name__ == "__main__":
    main()