import requests


def get_weather(city):
    api_key = "220ec67bd42c8c55fec2d4f5a003d45e"  
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"

    try:
        response = requests.get(url)
        response.raise_for_status()
        data = response.json()

        print("\n🌤 Weather Report")
        print(f"City: {data['name']}")
        print(f"Temperature: {data['main']['temp']}°C")
        print(f"Weather: {data['weather'][0]['description'].title()}")
        print(f"Humidity: {data['main']['humidity']}%")
        print(f"Wind Speed: {data['wind']['speed']} m/s")

    except requests.exceptions.RequestException as e:
        print("❌ Error fetching weather data:", e)
    except KeyError:
        print("❌ Invalid response. Check city name or API key.")

def get_crypto_price(coin="bitcoin"):
    url = f"https://api.coingecko.com/api/v3/simple/price?ids={coin}&vs_currencies=usd"

    try:
        response = requests.get(url)
        response.raise_for_status()
        data = response.json()

        print("\n💰 Crypto Price")
        print(f"{coin.capitalize()} Price: ${data[coin]['usd']}")

    except requests.exceptions.RequestException as e:
        print("❌ Error fetching crypto data:", e)
    except KeyError:
        print("❌ Invalid response. Check coin name.")

# Main Menu
def main():
    print("=== Codveda Internship Project ===")
    print("1. Get Weather Report")
    print("2. Get Crypto Price")
    choice = input("Enter choice (1/2): ")

    if choice == "1":
        city = input("Enter city name: ")
        get_weather(city)
    elif choice == "2":
        coin = input("Enter cryptocurrency name (e.g., bitcoin, ethereum): ")
        get_crypto_price(coin)
    else:
        print("❌ Invalid choice. Please select 1 or 2.")

if __name__ == "__main__":
    main()
