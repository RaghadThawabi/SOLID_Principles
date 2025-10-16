from abc import ABC, abstractmethod

class MessageSender(ABC):
    @abstractmethod
    def send(self, message):
        pass

class EmailSender(MessageSender):
    def send(self, message):
        print("Email message : " + message)

class SMSSender(MessageSender):
    def send(self, message):
        print("SMS message : " + message)

class Notification:
    def __init__(self, sender: MessageSender):
        self.sender = sender

    def send_msg(self, message):
        self.sender.send(message)

def main():
   sender=SMSSender()
   notify=Notification(sender)
   notify.send_msg("Hello World")
   sender2=EmailSender()
   notify2=Notification(sender2)
   notify2.send_msg("Hello World")


if __name__ == "__main__":
    main()
