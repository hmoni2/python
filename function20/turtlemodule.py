import turtle
import string
from myTurtle import *


turtle.Turtle()
swidth, sheight = 500, 500

if(__name__ == "__main__"):

    # turtle main #
   
    getMain(swidth,sheight)


    while True : 
        turtle.clear()
        inStr = getStrings()
    
        for i in inStr :
            tX, tY, tSize = getXY(swidth,sheight)
            turtle.pencolor(getRGB())
            turtle.penup()
            turtle.goto(tX,tY)
            turtle.write(i,move = True, align = 'center',font = ['HY견명조',tSize])
            
        
turtle.done()

