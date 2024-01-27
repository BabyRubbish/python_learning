messges = []
messges.append("Hello world!")
messges.append("I love python!")
messges_sent = []


def show_message(messges):
    for messge in messges:
        print(messge)


show_message(messges=messges)


def send_message(origin_messages, aim_messages):
    while origin_messages:
        messge = origin_messages.pop()
        aim_messages.append(messge)


send_message(messges[:], messges_sent)
print(f"Origin message: {messges}")
print(f"Aim message: {messges_sent}")
