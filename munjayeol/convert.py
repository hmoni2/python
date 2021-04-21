# 문자열 입력받아 반대로 출력#
outStr = ""
length = 0

inStr = input("문자열 입력 : ")
length = len(inStr)
print("현재 문자열 길이 --> %2d " % length)

for i in range(0,length) :
    count = length - (i+1)
    outStr += inStr[count]

print("문자열 반대로 출력 --> %s" % outStr)
    