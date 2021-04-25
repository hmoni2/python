inFp = None
inStr = ""
count = 0
inFp = open("C:\\Users\\KYOUNGAH\\python\\hello.txt","rt",encoding = "UTF8")
'''
while True :
    inStr = inFp.readline()
    if inStr == "" :
        break
    print(inStr, end = "")
'''
inStr = inFp.readlines()
for inList in inStr :
    count += 1
    print(count,inList,end = "")

inFp.close()
