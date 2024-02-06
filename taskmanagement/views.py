from django.shortcuts import render
from django.http import HttpResponse
import json
from django.views.decorators.csrf import csrf_exempt

from utils import message_creater
from line_bot_tutorial.line_massage import LineMessage

@csrf_exempt
def index(request):
    # メッセージを受け取った時
    if request.method == 'POST':
        # JSONの抽出
        request = json.loads(request.body.decode('utf-8'))
        data = request['events'][0]
        message = data['message']
        reply_token = data['replyToken']
        # リマインドを受け取った時
        if message['text'] == 'リマインド':
            reply_question = LineMessage(message_creater.create_single_text_message('後で思い出したいことを教えてください！'))
            reply_question.reply(reply_token)
            
            if request.method == 'POST':
                # JSONの抽出
                request = json.loads(request.body.decode('utf-8'))
                data = request['events'][0]
                message = data['message']
                reply_token = data['replyToken']
                

        line_message = LineMessage(message_creater.create_single_text_message(message['text']))
        line_message.reply(reply_token)
        user_ID = data['source']['userId']


        print(request)
        print('-----------------------------')
        print(data)
        print('-----------------------------')
        print(message)

    return HttpResponse("ok")
