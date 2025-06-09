import requests
from utils.config import TELEGRAM_BOT_TOKEN, TELEGRAM_CHAT_ID

def send_alert(image_path):
    url = f"https://api.telegram.org/bot{TELEGRAM_BOT_TOKEN}/sendPhoto"
    with open(image_path, 'rb') as img:
        files = {'photo': img}
        data = {
            'chat_id': TELEGRAM_CHAT_ID,
            'caption': '⚠️ Motion detected!'
        }
        response = requests.post(url, files=files, data=data)
        if not response.ok:
            print("❌ Telegram alert failed:", response.text)
        return response.ok
