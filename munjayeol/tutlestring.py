import turtle
import random
import string
from tkinter.simpledialog import *


tSize,tX,tY = [0],[0],[0]
inputStr = ""
swidth, sheight = 500, 500

turtle.Turtle()


if(__name__ == "__main__"):

    # turtle main #
    turtle.title("임의의 위치에 글자를 쓰는 거북이")
    turtle.shape('turtle')
   
    turtle.setup(width = swidth + 50, height = sheight + 50)
    turtle.screensize(swidth,sheight)
    turtle.speed(1)

    

    while True : 
        turtle.clear()
        inputStr = askstring('문자열 입력','거북이 쓸 문자열을 입력')
    
        for i in inputStr :

            tX = random.randrange(-swidth/2 , swidth/2)        #X좌표
            tY = random.randrange(-sheight/2 , sheight/2)      #Y좌표
            tSize = random.randrange(4,56)                     #글자 크기
            r = random.random()    
            g = random.random()
            b = random.random()

            turtle.pencolor(r,g,b)
            
            turtle.penup()
            turtle.goto(tX,tY)
            turtle.write(i,move = True, align = 'center',font = ['HY견명조',tSize])
            
        
turtle.done()

