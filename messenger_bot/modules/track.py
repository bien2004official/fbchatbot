from modules import afk
from fbchat import log, Client
from fbchat.models import *

def main(email, password):
    isAFK = False
    class TrackBot(Client):
        def onMessage(self, author_id, message_object, thread_id, thread_type, **kwargs):
            self.markAsDelivered(thread_id, message_object.uid)
            if author_id == self.uid:
                messages = client.fetchThreadMessages(thread_id=thread_id, limit=1)
                global isAFK
                for message in messages:
                    content = message.text
                    if content == '.afk':
                        isAFK = True
                        client.unsend(message_object.uid)
                        client.send(Message(text="I'm now AFK!"), thread_id=thread_id, thread_type=ThreadType.USER)
                        afk.main(email, password)
                    # elif content == '.unafk' and isAFK:
                        # isAFK = False
                        # client.unsend(message_object.uid)
                        # client.send(Message(text="I'm no longer AFK"), thread_id=thread_id, thread_type=ThreadType.USER)
    client = TrackBot(email, password)
    client.listen()
