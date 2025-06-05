# Discord Weather Bot 🌤️

Một bot Discord tự động gửi thông tin thời tiết hàng ngày lúc 7:00 AM.

## Tính năng
- 🕰️ Gửi thời tiết tự động mỗi ngày lúc 7:00 AM
- 🌡️ Hiển thị nhiệt độ, độ ẩm, tốc độ gió
- 🌧️ Mô tả thời tiết bằng tiếng Việt
- 📍 Có thể thay đổi thành phố

## Công nghệ sử dụng
- **Python 3.9+**
- **OpenWeatherMap API** (miễn phí)
- **Discord Webhooks**
- **GitHub Actions** (scheduling)

## Cài đặt

### 1. Clone repository
```bash
git clone https://github.com/yourusername/discord-weather-bot
cd discord-weather-bot
```

### 2. Cài đặt dependencies
```bash
pip install -r requirements.txt
```

### 3. Lấy API Keys
- **OpenWeatherMap**: Đăng ký tại https://openweathermap.org/api
- **Discord Webhook**: Tạo webhook trong Discord server

### 4. Setup GitHub Secrets
Trong GitHub repository → Settings → Secrets:
- `WEATHER_API_KEY`: API key từ OpenWeatherMap
- `DISCORD_WEBHOOK_URL`: Webhook URL từ Discord

### 5. Chạy thử
```bash
python main.py
```

## Tùy chỉnh

### Thay đổi thành phố
Sửa dòng trong `main.py`:
```python
weather = get_weather_data("Ho Chi Minh City")  # Thay đổi tên thành phố
```

### Thay đổi thời gian
Sửa cron expression trong `.github/workflows/weather-bot.yml`:
```yaml
- cron: '0 0 * * *'  # 7:00 AM UTC+7 = 0:00 AM UTC
```

## Demo
![Weather Bot Demo](demo.png)

## Đóng góp
Mọi đóng góp đều được chào đón! Hãy tạo Pull Request hoặc Issue.

## License
MIT License

## Liên hệ
- GitHub: [@yourusername](https://github.com/yourusername)
- Discord: yourdiscord#1234