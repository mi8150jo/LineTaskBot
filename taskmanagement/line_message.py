from django.http import HttpResponse
import urllib.request
import json
import environ 
from line_bot.settings import REPLY_ENDPOINT_URL, ACCESSTOKEN

print(f"REPLY_ENDPOINT_URL: {REPLY_ENDPOINT_URL}")
print(f"ACCESSTOKEN: {ACCESSTOKEN}")

HEADER = {
    'Content-Type': 'application/json',
    'Authorization': 'Bearer ' + ACCESSTOKEN
}

#メッセージの送信
class LineMessage():
    def __init__(self, messages):
        self.messages = messages

    def reply(self, reply_token):
        body = {
            'replyToken': reply_token,
            'messages': self.messages
        }
        # print(body)
        req = urllib.request.Request(REPLY_ENDPOINT_URL, json.dumps(body).encode(), HEADER)
        try:
            with urllib.request.urlopen(req) as res:
                body = res.read()
        except urllib.error.HTTPError as err:
            print(err)
        except urllib.error.URLError as err:
            print(err.reason)