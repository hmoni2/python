ss = "파이썬최고"
print(ss[0])
print(ss[1:3])
print(ss[3:])

ss = '파이썬' + '최고'
ss
ss = '파이썬' * 3
ss

ss = '파이썬abcd'
sslen = len(ss)
for i in range(0,sslen) :
    print(ss[i] + '$', end = '')
    