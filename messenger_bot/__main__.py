from modules import afk, base64_converter
# import email and password from email.txt and password.txt
f=open('email.txt', 'r')
if f.mode == 'r':
    email = f.read()
f.close()
f=open('password.txt', 'r')
if f.mode == 'r':
    password = base64_converter.converter(f.read())
f.close()

# main program
afk.main(email, password)
