from dateutil import parser

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