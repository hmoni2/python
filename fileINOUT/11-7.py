outFp = None
outStr,fname = "",""

fName = input("파일명을 입력하세요 : ")
outFp = open("fName","w",encoding="UTF8")

while True :
    outStr = input("내용 입력 : ")
    if outStr != "" :
        outFp.writelines(outStr + "\n")
    else :
        break
outFp.close()
print("--- 파일에 정상적으로 써졌음---")

#내용 입력할 때 한글로 입력하면 정상적으로 출력이 안됨 -> 파일형식 확인해볼것 
#UTF-8 형식으로 되어있느나 앞으로 파일 오픈시에는 무조건 따로 encoding 형식 작성해야함