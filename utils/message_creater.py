def create_single_text_message(message):
    if message == '開発者':
        message = 'mi8150jo'
    test_message = [
        {
            'type': 'text',
            'text': message
        }
    ]
    return test_message