def show_messages(text_messages):
    for text_message in text_messages:
        print(text_message)

def send_messages(text_messages, sent_messages):
    print("\nSending all messages")
    while text_messages:
        current_message = text_messages.pop()
        print(current_message)
        sent_messages.append(current_message)


text_messages = ['Hello there!', 'Pick me up some apples', 'Lets meet for dinner tonight.']
sent_messages = []
show_messages(text_messages)
send_messages(text_messages[:], sent_messages)
print(text_messages)
print(sent_messages)