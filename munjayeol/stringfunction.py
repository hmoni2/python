'''
ss = 'python is easy. so programming is very fun'
print(ss.upper())
print(ss.lower())
print(ss.swapcase())
print(ss.title())

print(ss.count('s'))
print(ss.find('is'))
print(ss.rfind('is'))
print(ss.index('is'))
print(ss.startswith('python'))
print(ss.endswith('programming'))
'''
'''
ss = '----파----이----썬----'
print(ss.strip('-'))
ss = '<<<<파 <<<이>> 썬 >>>>'
print(ss.strip('<>'))
'''
'''
inStr = "   한글 Python 프로그래밍   "
outStr = ""

for i in range(0,len(inStr)) :
    if inStr[i] != '\0' : 
        outStr += inStr[i]

print('[' + inStr + ']')
print(outStr)
'''
import re
ss = 'Python is Easy&Simple.'
sslist =re.split('[ ,&]',ss)

before = ['2019','12','31']
after = list(map(int,before))
