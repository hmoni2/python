import turtle
import random

# 전역 변수 선언 #
myTurtle, tX, tY, tColor, tSize, tShape = [None] * 6
shapeList = []
playerTurtles = [] #거북이 2차원 리스트
swidth, sheight = 500, 500

# 메인 코드 #
if __name__ == "__main__" :  #이건 왜 선언을 하는거지? 인터프리터에서 직접 실행한 경우에만 if 문 코드 실행
    turtle.title('거북 리스트 활용')
    turtle.setup(width = swidth + 50, height = sheight + 50)
    turtle.screensize(swidth,sheight)

    shapeList = turtle.getshapes() # 모든 거북이 이름 목록 반환
    # getshapes() = ['arrow','blank','circle','classic','square','triangle','turtle]
    for i in range(0,5) : #tutle object 100개
        random.shuffle(shapeList)
        myTurtle = turtle.Turtle(shapeList[0])  # 맨 처음 화살표로 출발하기 위함
        tX = random.randrange(-swidth/2 , swidth/2)
        tY = random.randrange(-sheight/2 , sheight/2)
        r = random.random()
        g = random.random()
        b = random.random()
        
        tSize = random.randrange(1,3)       # 나오는 모양의 크기가 1~3이 되게 
        playerTurtles.append([myTurtle, tX, tY, tSize, r, g, b])

    for tList in playerTurtles : # playerTurtles 안에 tList만큼 반복?
        myTurtle = tList[0]
        myTurtle.color ((tList[4], tList[5], tList[6]))
        myTurtle.pencolor((tList[4],tList[5],tList[6]))
        myTurtle.turtlesize(tList[3])
        myTurtle.penup()
        myTurtle.setpos(tList[1], tList[2])
        myTurtle.pendown()
        myTurtle.goto(0,0)
        
    turtle.done()