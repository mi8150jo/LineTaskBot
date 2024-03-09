from dateutil import parser

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