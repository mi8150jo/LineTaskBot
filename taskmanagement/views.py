from django.shortcuts import render
from django.http import HttpResponse
import json
from django.views.decorators.csrf import csrf_exempt
from utils import message_creater
from line_bot_tutorial.line_massage import LineMessage
from dateutil import parser

remind_flag = False
date_flag = False
task_content = ''
task_date = ''

def send_line_message(text, reply_token):
    line_message = LineMessage(message_creater.create_single_text_message(text))
    line_message.reply(reply_token)

def parse_date(text):
    try:
        # dateutilを使用して日付を解析
        parsed_date = parser.parse(text, fuzzy=True)
        return parsed_date
    except ValueError:
        # 解析できない場合はNoneを返す
        return None

@csrf_exempt
def index(request):

    global remind_flag, date_flag, task_content, task_date

    # メッセージを受け取った時
    if request.method == 'POST':
        # JSONの抽出
        request = json.loads(request.body.decode('utf-8'))
        data = request['events'][0]
        message = data['message']
        reply_token = data['replyToken']
        user_ID = data['source']['userId']

        # タスクの日付
        if date_flag == True:
            task_date = parse_date(message['text'])

            if task_date:
                formatted_date = task_date.strftime("%Y-%m-%d %H:%M:%S")
                send_line_message('じゃあ「' + formatted_date + '」に教えるね！', reply_token)
            else:
                send_line_message('日付の形式が不正です。もう一度教えてください。', reply_token)
                
            
            remind_flag = False
            date_flag = False
            return HttpResponse()

        # タスク内容を取得
        if remind_flag == True:
            task_content = message['text']
            date_flag = True
            # いつ思い出したいか質問
            send_line_message(("「" + task_content + "」だね！\n" + "いつ思い出したいか教えて！\n例：yyyy-mm-dd"), reply_token)
            return HttpResponse()

        # リマインドを受け取った時
        if message['text'] == 'リマインド':
            remind_flag = True
            # 思い出したいことを質問
            send_line_message('後で思い出したいことを教えてください！', reply_token)
            return HttpResponse()

        #オウム返し
        if remind_flag == False:
            send_line_message(message['text'], reply_token)
            return HttpResponse()

        # print(task_content)
        # print(task_date)
        # print(request)
        # print(request_remind)
        # print(request)
        # print('-----------------------------')
        # print(data)
        # print('-----------------------------')
        # print(message)

    return HttpResponse("ok")
