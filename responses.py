import random

def get_response(message: str) -> str:
    p_message = message.lower()

    if p_message == 'hello':
        return 'Hi'
    
    if p_message == 'repeat after me':
        return 'repeat after me'

    if p_message == 'roll':
        return str(random.randint(1, 6))
    
    if p_message == '!test':
        return 'TESTING DO YOU READ???'

    if p_message == '!help':
        return '`This is a help message (needs to be modified).`'
    
    return 'I didn\'t understand what you wrote. If you need some ideas try "!help".'