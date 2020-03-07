from messenger_bot.modules import afk
from fbchat import log, Client
from fbchat.models import *

def main(cookies):
    class TrackBot(Client):
        def onMessage(self, author_id, message_object, thread_id, thread_type, **kwargs):
            self.markAsDelivered(thread_id, message_object.uid)
            if author_id == self.uid:
                messages = client.fetchThreadMessages(thread_id=thread_id, limit=1)
                for message in messages:
                    content = message.text
                    if content == '.afk':
                        client.unsend(message_object.uid)
                        client.send(Message(text="I'm now AFK!"), thread_id=thread_id, thread_type=ThreadType.USER)
                        client.logout()
                        afk.main(email, password)

    client = TrackBot(session_cookies=cookies)
    client.listen()
