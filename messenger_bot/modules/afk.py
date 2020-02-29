from fbchat import log, Client
from fbchat.models import *
from messenger_bot.modules import track

def main(email, password):
    class EchoBot(Client):
        def onMessage(self, author_id, message_object, thread_id, thread_type, **kwargs):
            # self.markAsDelivered(thread_id, message_object.uid)
            messages = client.fetchThreadMessages(thread_id=thread_id, limit=1)
            if author_id != self.uid and thread_type == ThreadType.USER:
                client.send(Message(text="I'm AFK"), thread_id=author_id, thread_type=ThreadType.USER)
            elif author_id != self.uid and thread_type == ThreadType.GROUP:
                print("Found message in a group, but I was unable to check if there is a tag or not, because it's throwing errors")    
            else:
                for message in messages:
                    if message.text == '.unafk':
                        client.unsend(message_object.uid)
                        client.send(Message(text="I'm no longer AFK"), thread_id=thread_id, thread_type=thread_type)
                        track.main(email, password)
                
    client = EchoBot(email, password)
    client.listen()
