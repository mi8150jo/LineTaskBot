from dateutil import parser

def convert_to_time(time_string):
    try:
        # parseメソッドを使用して文字列を解釈し、datetimeオブジェクトを取得
        datetime_object = parser.parse(time_string)
        
        # datetimeオブジェクトからtimeオブジェクトを抽出
        time_object = datetime_object.time()
        
        return time_object
    except ValueError:
        print("無効な時刻形式です。正しい形式で入力してください。")
        return None

# テスト用
time_str1 = "12:30"
time_str2 = "3:00"
time_str3 = "23:00"

converted_time1 = convert_to_time(time_str1)
converted_time2 = convert_to_time(time_str2)
converted_time3 = convert_to_time(time_str3)

if converted_time1:
    print(f"変換された時刻1: {converted_time1}")

if converted_time2:
    print(f"変換された時刻2: {converted_time2}")

if converted_time3:
    print(f"変換された時刻3: {converted_time3}")
