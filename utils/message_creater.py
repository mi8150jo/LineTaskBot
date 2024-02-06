def create_single_text_message(message):
    if message == 'こんにちは':
        message = 'どういたしまして'
    test_message = [
        {
            'type': 'text',
            'text': message
        }
    ]
    return test_message