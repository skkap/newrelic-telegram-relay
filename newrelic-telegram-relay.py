from flask import Flask, request
from flask_restful import Resource, Api
from telegram import send_telegram_message
import json

app = Flask(__name__)
api = Api(app)


with open('config/telegram.json') as f:
    telegram_config = json.load(f)

token = telegram_config['botToken']
chat_ids = telegram_config['receiverChatIds']


class WebHook(Resource):
    def post(self):
        payload = request.json
        print('Received webhook.')
        print(payload)
        for chat_id in chat_ids:
            print('Sending message to telegram chat: ' + chat_id)
            state = payload['current_state']
            if state == 'open':
                state_title = '🚨 ' + \
                    payload['event_type'] + ' ' + state
            else:
                state_title = '✅ ' + \
                    payload['event_type'] + ' ' + state
            message = "*" + state_title + '*\n' \
                '*Policy*: ' + payload['policy_name'] + '\n' \
                '*Details*: ' + payload['details'] + '\n' \
                '*Time*: ' + payload['timestamp_utc_string'] + '\n' \
                '[Chart](' + payload['violation_chart_url'] + ')'
            send_telegram_message(token, chat_id, message)
        return 'OK'


api.add_resource(WebHook, '/webhook')

if __name__ == '__main__':
    app.run(debug=False, port=5000, host='0.0.0.0')
