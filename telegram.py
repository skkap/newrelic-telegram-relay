import requests
import json

def send_telegram_message(token, chat_id, message):
    host = 'https://api.telegram.org/bot' + token + '/sendMessage'
    headers = {'Content-Type': 'application/json'}

    payload = {
        "chat_id": chat_id, 
        "text": message, 
        "disable_notification": False,
        "parse_mode": "Markdown"
    }

    requests.post(host, headers=headers, data=json.dumps(payload))
