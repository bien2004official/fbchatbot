from fbchat import log, Client
from fbchat.models import *

def main(email, password):
# Subclass fbchat.Client and override required methods
    class EchoBot(Client):
        def onMessage(self, author_id, message_object, thread_id, thread_type, **kwargs):
            self.markAsDelivered(thread_id, message_object.uid)
            # Only reply if message was from another user
            if author_id != self.uid:
                if thread_type != ThreadType.GROUP: # If message was from a user, reply with a message
                    message_id = client.send(Message(text='a'), thread_id=author_id, thread_type=ThreadType.USER)
                    client.reactToMessage(message_id, MessageReaction.LIKE)
            # If message was from a group, check if it was a tag or not,
            # only reply if it is a tag
            # elif thread_type == ThreadType.GROUP:

    client = EchoBot(email, password)
    client.listen()
