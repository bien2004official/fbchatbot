from fbchat import log, Client
from fbchat.models import *

def main(email, password):
    class EchoBot(Client):
        def onMessage(self, author_id, message_object, thread_id, thread_type, **kwargs):
            self.markAsDelivered(thread_id, message_object.uid)
            messages = client.fetchThreadMessages(thread_id=thread_id, limit=1)
            if author_id != self.uid and thread_type != ThreadType.GROUP:
                client.send(Message(text='Test AFK message'), thread_id=author_id, thread_type=ThreadType.USER)
            # elif author_id == self.uid:
                # for message in messages:
                    # if message == '.unafk':
                        # isAFK = False
                        # client.unsend(message_object.uid)
                        # client.send(Message(text="I'm no longer AFK"), thread_id=author_id, thread_type=thread_type)
                        # exit()
            # If message was from a group, check if it was a tag or not,
            # only reply if it is a tag
            # elif thread_type == ThreadType.GROUP:
            # don't know what to do next here

    client = EchoBot(email, password)
    client.listen()
