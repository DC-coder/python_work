dinner_guests = ['einstein', 'oppenheimer', 'truman']
print(len(dinner_guests))
message1 = f"Hello, {dinner_guests[0].title()} you are invited to my dinner."
message2 = f"Hello, {dinner_guests[1].title()} you are invited to my dinner."
message3 = f"Hello, {dinner_guests[2].title()} you are invited to my dinner."
print(message1)
print(message2)
print(message3)
print(f"{dinner_guests[0].title()} can't make the dinner.")
del dinner_guests[0]
print(dinner_guests)
dinner_guests.insert(0,'obama')
newguest = dinner_guests[0].title()
print(f"Hello, {newguest} you are invited to my dinner.")
print(message2)
print(message3)
print('I found a bigger table.')
dinner_guests.insert(0, 'trump')
dinner_guests.insert(3, 'bush')
dinner_guests.append('clinton')
print(dinner_guests)
message0 = f"Hello, {dinner_guests[0].title()} you are invited to my dinner."
message1 = f"Hello, {dinner_guests[1].title()} you are invited to my dinner."
message2 = f"Hello, {dinner_guests[2].title()} you are invited to my dinner."
message3 = f"Hello, {dinner_guests[3].title()} you are invited to my dinner."
message4 = f"Hello, {dinner_guests[4].title()} you are invited to my dinner."
message5 = f"Hello, {dinner_guests[5].title()} you are invited to my dinner."
print(message0)
print(message1)
print(message2)
print(message3)
print(message4)
print(message5)
print('Sorry for the mixup: I can now only invite 2 people to dinner.')
delguest0 = dinner_guests.pop()
print(f"Sorry, {delguest0.title()}, we don't have space for you.")
delguest1 = dinner_guests.pop()
print(f"Sorry, {delguest1.title()}, we don't have space for you.")
delguest2 = dinner_guests.pop()
print(f"Sorry, {delguest2.title()}, we don't have space for you.")
delguest3 = dinner_guests.pop()
print(f"Sorry, {delguest3.title()}, we don't have space for you.")
print(f"{dinner_guests[0].title()}, you're stil linvited.")
print(f"{dinner_guests[1].title()}, you're stil linvited.")
del dinner_guests[0]
del dinner_guests[0]
print(dinner_guests)

