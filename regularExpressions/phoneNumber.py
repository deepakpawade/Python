import re

phoneNumRegex = re.compile(r'(\d\d\d)-(\d\d\d-\d\d\d\d)')
mo = phoneNumRegex.search("Number is 114-454-6969")
print(mo.group())
print(mo.groups())
print(mo.group(1))
print(mo.group(2))
