import base64

def converter(password):
    base64_message = password
    base64_bytes = base64_message.encode('ascii')
    message_bytes = base64.b64decode(base64_bytes)
    password = message_bytes.decode('ascii')
    return password;
