import requests
import os
from datetime import datetime
import json

def get_weather_data(city="Ho Chi Minh City"):
    """Lấy thông tin thời tiết từ OpenWeatherMap API"""
    api_key = os.getenv('WEATHER_API_KEY')
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric&lang=vi"
    
    try:
        response = requests.get(url)
        data = response.json()
        
        if response.status_code == 200:
            return {
                'city': data['name'],
                'temperature': round(data['main']['temp']),
                'feels_like': round(data['main']['feels_like']),
                'humidity': data['main']['humidity'],
                'description': data['weather'][0]['description'],
                'wind_speed': data['wind']['speed'],
                'icon': data['weather'][0]['icon']
            }
        else:
            print(f"API Error: {data.get('message', 'Unknown error')}")
            return None
    except Exception as e:
        print(f"Error fetching weather: {e}")
        return None

def format_weather_message(weather_data):
    """Tạo message thời tiết đẹp cho Discord"""
    if not weather_data:
        return "❌ Không thể lấy thông tin thời tiết lúc này."
    
    # Emoji theo thời tiết
    weather_emoji = {
        'clear': '☀️',
        'clouds': '☁️',
        'rain': '🌧️',
        'drizzle': '🌦️',
        'thunderstorm': '⛈️',
        'snow': '❄️',
        'mist': '🌫️'
    }
    
    icon = weather_data['icon'][:2]  # Lấy 2 ký tự đầu của icon code
    emoji = weather_emoji.get(icon, '🌤️')
    
    message = f"""
🌤️ **THỜI TIẾT HÔM NAY - {datetime.now().strftime('%d/%m/%Y')}**

📍 **Thành phố:** {weather_data['city']}
{emoji} **Thời tiết:** {weather_data['description'].title()}
🌡️ **Nhiệt độ:** {weather_data['temperature']}°C (cảm giác như {weather_data['feels_like']}°C)
💧 **Độ ẩm:** {weather_data['humidity']}%
💨 **Tốc độ gió:** {weather_data['wind_speed']} m/s

Have a great day! 🌈
"""
    return message

def send_to_discord(message):
    """Gửi message tới Discord channel qua webhook"""
    webhook_url = os.getenv('DISCORD_WEBHOOK_URL')
    
    if not webhook_url:
        print("Discord webhook URL not found!")
        return False
    
    payload = {
        'content': message,
        'username': 'Weather Bot',
        'avatar_url': 'https://cdn-icons-png.flaticon.com/512/1163/1163661.png'
    }
    
    try:
        response = requests.post(webhook_url, json=payload)
        if response.status_code == 204:
            print("Weather message sent successfully!")
            return True
        else:
            print(f"Failed to send message: {response.status_code}")
            return False
    except Exception as e:
        print(f"Error sending to Discord: {e}")
        return False

def main():
    """Hàm chính - lấy thời tiết và gửi Discord"""
    print(f"Running weather bot at {datetime.now()}")
    
    # Lấy thông tin thời tiết
    weather = get_weather_data("Ho Chi Minh City")  # Có thể thay đổi thành phố
    
    # Tạo message
    message = format_weather_message(weather)
    
    # Gửi tới Discord
    success = send_to_discord(message)
    
    if success:
        print("✅ Weather update sent successfully!")
    else:
        print("❌ Failed to send weather update")

if __name__ == "__main__":
    main()