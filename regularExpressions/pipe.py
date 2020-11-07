import re

batReg = re.compile(r'Bat(man|mobile|copter|bat)')
mo = batReg.search('Batmobile lost a wheel')
print(mo.group(1))
print(mo.group(0))
print(mo.groups())