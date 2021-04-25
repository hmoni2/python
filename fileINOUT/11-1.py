inFp = None
inStr = ""

inFp = open("c:\\Users\\KYOUNGAH\\python\\hello.txt","rt",encoding="UTF8")

inStr = inFp.readline()
print(inStr, end = "")

inStr = inFp.readline()
print(inStr, end = "")

inStr = inFp.readline()
print(inStr, end = "")

inFp.close()
