uni = u"Hi, \u2119\u01b4\u2602\u210c\xf8\u1f24"
print(uni)

utf = uni.encode('utf-8')
print(utf)

print(utf.decode('utf-8'))