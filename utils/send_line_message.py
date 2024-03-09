from .line_message import LineMessage
from .message_creater import create_single_text_message

def send_line_message(text, reply_token):
    line_message = LineMessage(create_single_text_message(text))
    line_message.reply(reply_token)