<<<<<<< HEAD
import base64

def converter(password):
    base64_message = password
    base64_bytes = base64_message.encode('ascii')
    message_bytes = base64.b64decode(base64_bytes)
    password = message_bytes.decode('ascii')
    return password;
=======
import base64

def converter(password):
    base64_message = password
    base64_bytes = base64_message.encode('ascii')
    message_bytes = base64.b64decode(base64_bytes)
    password = message_bytes.decode('ascii')
    return password;
>>>>>>> 6b6d7adb40c0e610ca6a76cde42f6fd29bfc6b45
