from django.shortcuts import render
from django.http import HttpResponse
import json
from django.views.decorators.csrf import csrf_exempt
from utils import message_creater
from .line_message import LineMessage
from dateutil import parser
from datetime import datetime, timedelta
from .models import Task

remind_flag = False
date_flag = False
startTime_flag = False
endTime_flag = False
task_content = ''
task_date = ''
task_startTime = ''
task_endTime = ''

def send_line_message(text, reply_token):
    line_message = LineMessage(message_creater.create_single_text_message(text))
    line_message.reply(reply_token)

def convert_to_date(text):
    try:
         # parseメソッドを使用して文字列を解釈し、datetimeオブジェクトを取得
        datetime_object = parser.parse(text)

        # datetimeオブジェクトからdateオブジェクトを抽出
        date_object = datetime_object.date()

        return date_object
    except ValueError:
        # 解析できない場合はNoneを返す
        return None

def convert_to_time(text):
    try:
        # parseメソッドを使用して文字列を解釈し、datetimeオブジェクトを取得
        datetime_object = parser.parse(text)
        
        # datetimeオブジェクトからtimeオブジェクトを抽出
        time_object = datetime_object.time()
        
        return time_object
    except ValueError:
        # 解析できない場合はNoneを返す
        return None

@csrf_exempt
def index(request):

    global remind_flag, date_flag, task_content, task_date, startTime_flag, endTime_flag, task_startTime, task_endTime

    # メッセージを受け取った時
    if request.method == 'POST':

        # 受け取ったメッセージのJSONの抽出
        request = json.loads(request.body.decode('utf-8'))
        data = request['events'][0]
        message = data['message']
        reply_token = data['replyToken']
        user_ID = data['source']['userId']


        # キャンセルの処理
        if message['text'] == 'キャンセル':
            send_line_message('キャンセルしたよ！', reply_token)
            # グローバル変数の初期化
            remind_flag = False
            date_flag = False
            startTime_flag = False
            endTime_flag = False
            task_content = ''
            task_date = ''
            task_startTime = ''
            task_endTime = ''


        # タスクの終了時間
        if endTime_flag == True:
            task_endTime = convert_to_time(message['text'])

            if task_endTime:
                # リマインドする日を一日前にする
                remind_date = task_date - timedelta(days=1)
                # 文字列に変換
                task_date, task_startTime, task_endTime, remind_date = map(str, (task_date, task_startTime, task_endTime, remind_date))
                # タスク内容の確認メッセージを送信
                send_line_message(("「" + task_content + "」\n" + "日付：" + task_date + "\n" + task_startTime + "〜" + task_endTime + "\n" + "上記の内容で登録しました！"), reply_token)
                # データベースにタスクを追加
                Task.objects.create(user_ID=user_ID, content=task_content, date=task_date, startTime=task_startTime, endTime=task_endTime, remind_date=remind_date)
                print("!!!データベースに追加しました!!!")

                # グローバル変数の初期化
                remind_flag = False
                date_flag = False
                startTime_flag = False
                endTime_flag = False
                task_content = ''
                task_date = ''
                task_startTime = ''
                task_endTime = ''

            else:       
                send_line_message('日付の形式が不正です。もう一度教えてください。', reply_token)
                
            return HttpResponse()


        # タスクの開始時間を取得
        if startTime_flag == True:
            task_startTime = convert_to_time(message['text'])
            if task_startTime:
                endTime_flag = True
                # タスクの終了時間を質問
                send_line_message(("終了時間を教えて！"), reply_token)
            else:
                send_line_message('日付の形式が不正です。もう一度教えてください。', reply_token)
            return HttpResponse()

        # タスクの日付を取得
        if date_flag == True:
            # メッセージの日付を解析
            task_date = convert_to_date(message['text'])
            # 今日の日付を取得しdate形式に変換
            today = datetime.now().date()

            # 過去の日付と不正な日付が入力された場合
            if task_date > today:
                startTime_flag = True

                # タスクの開始時間を質問
                send_line_message(("開始時間を教えて！"), reply_token)
            else:
                send_line_message('日付の形式が不正です。もう一度教えてください。', reply_token)
                
            return HttpResponse()

        # タスク内容を取得
        if remind_flag == True:
            task_content = message['text']
            date_flag = True

            # タスクの日付を質問
            send_line_message(("「" + task_content + "」だね！\n" + "日付を教えて！\n例：12/25"), reply_token)
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

    return HttpResponse("ok")
