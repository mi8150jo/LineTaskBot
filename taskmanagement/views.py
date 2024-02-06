from django.shortcuts import render
from django.http import HttpResponse
import json
from django.views.decorators.csrf import csrf_exempt
from utils import message_creater
from line_bot_tutorial.line_massage import LineMessage

remind_flag = False
date_flag = False

@csrf_exempt
def index(request):

    global remind_flag, date_flag

    # メッセージを受け取った時
    if request.method == 'POST':
        
        # JSONの抽出
        request = json.loads(request.body.decode('utf-8'))
        data = request['events'][0]
        message = data['message']
        reply_token = data['replyToken']
        user_ID = data['source']['userId']

        # リマインドを受け取った時
        if message['text'] == 'リマインド':
            remind_flag = True
            # 思い出したいことを質問
            reply_question = LineMessage(message_creater.create_single_text_message('後で思い出したいことを教えてください！'))
            reply_question.reply(reply_token)
            return HttpResponse()

        if remind_flag == False:
            line_message = LineMessage(message_creater.create_single_text_message(message['text']))
            line_message.reply(reply_token)
            return HttpResponse()

        if remind_flag == True:
            date_flag = True
            # いつ思い出したいか質問
            reply_date_question = LineMessage(message_creater.create_single_text_message('いつ思い出したいか教えて！例：yyyy-mm-dd'))
            reply_date_question.reply(reply_token)
            return HttpResponse()

        if date_flag == True:
            return HttpResponse()



                    


        # print(request)
        # print(request_remind)
        # print(request)
        # print('-----------------------------')
        # print(data)
        # print('-----------------------------')
        # print(message)

    return HttpResponse("ok")
