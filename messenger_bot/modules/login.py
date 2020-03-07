import json
import fbchat

def main(email, password):
	cookies = {}
	try:
    # Load the session cookies
	    with open('session.json', 'r') as f:
	        cookies = json.load(f)
	except:
    # If it fails, never mind, we'll just login again
	    pass

# Attempt a login with the session, and if it fails, just use the email & password
	client = fbchat.Client(email, password, session_cookies=cookies)

# ... Do stuff with the client here

# Save the session again
	with open('session.json', 'w') as f:
	    json.dump(client.getSession(), f)
	return cookies
