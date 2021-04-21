
for i in range(0,3,1) :
    print("안녕하세요")

for i in range(2,-1,-1) :
    print("안녕하세요")

hap = 1 + 2 + 3 + 4 + 5 + 6 + 7 + 8 + 9 + 10
print("%d"%hap)

hap = 0
for i in range(1,11,1) :
    hap = hap+ i

num = int(input("값을 입력하세요 : "))
for i in range(1,num,1) :
    hap = hap + i

for i in range(1,6,1) :
    print("%d" %i, end = " ")

i = 0 
while i< 6 :
    print("%d" %i , end = " ")
    i = i + 1 #증가하는 부분이 없어서 표현 해줘야됨

while True :
    print("test")
    if(True):
        break
