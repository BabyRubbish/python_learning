names = ["lufi", "jhon wick", "ikun"]

message = ", I'd like to invite you to have dinner with me."
greeting = "Hi, "
print(f"{greeting}{names[0].title()}{message}")
print(f"{greeting}{names[1].title()}{message}")
print(f"{greeting}{names[2].title()}{message}")

print(f"What a pity! {names[0].title()} can't come and have dinner with us.")

names.remove("lufi")
names.append("Logic")

print(f"{greeting}{names[0].title()}{message}")
print(f"{greeting}{names[1].title()}{message}")
print(f"{greeting}{names[2].title()}{message}")

print("Wonderful! I find a bigger table for us.")
names.insert(0, "tom")
names.insert(2, "mike")
names.append("jamy")
print(names)

print(f"{greeting}{names[0].title()}{message}")
print(f"{greeting}{names[1].title()}{message}")
print(f"{greeting}{names[2].title()}{message}")
print(f"{greeting}{names[3].title()}{message}")
print(f"{greeting}{names[4].title()}{message}")
print(f"{greeting}{names[5].title()}{message}")

print("I'm so sorry that I can only have dinner with two of you.")

apology = "Sorry, "
message_ = ", I can't have dinner with you any more."
message__ = ", I'm glad to have dinner with you."

poped_person = names.pop()
print(f"{apology}{poped_person.title()}{message_}")
poped_person = names.pop()
print(f"{apology}{poped_person.title()}{message_}")
poped_person = names.pop()
print(f"{apology}{poped_person.title()}{message_}")
poped_person = names.pop()
print(f"{apology}{poped_person.title()}{message_}")

len(names)
print(f"I have invite {len(names)} people to have dinner with me.")

poped_person = names.pop()
print(f"{greeting}{poped_person.title()}{message__}")
poped_person = names.pop()
print(f"{greeting}{poped_person.title()}{message__}")

print(names)
