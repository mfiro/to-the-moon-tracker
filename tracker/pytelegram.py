import requests

class TelegramAPI:
    def __init__(self, api_key, base_url):

        self.api_key = api_key
        self.base_url = base_url


    def send_message(self, channel_id, message, reply_markup=None):
        data = {
            "chat_id": channel_id,
            "text": message,
            "parse_mode": "Markdown",
        }
        if reply_markup:
            data["reply_markup"] = reply_markup

        response = requests.post(
            f"{self.base_url}{self.api_key }/sendMessage", data=data
        )

        return response
