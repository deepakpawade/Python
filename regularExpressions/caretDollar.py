import re

beginsWithHello = re.compile(r'^Hello')
print(beginsWithHello.search('Hello, world!'))
print(beginsWithHello.search('world!'))

wholeStringIsNum = re.compile(r'^\d+$')
print(wholeStringIsNum.search('1234567890'))