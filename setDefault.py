import pprint
message = 'Hello there, How are u? It was a bright cold day in April, and the clocks were striking \
thirteen'
count = {}

for char in message:
    count.setdefault(char,0)
    count[char] +=1
pprint.pprint(count) #returns none
chara = pprint.pformat(count) #returns string value to store in a variable in prettified format
print(chara)