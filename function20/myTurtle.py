import random
from tkinter.simpledialog import *
import turtle

def getMain(swidth,sheight) :
    turtle.title("임의의 위치에 글자를 쓰는 거북이")
    turtle.shape('turtle')
    turtle.speed(1)
    turtle.setup(width = swidth + 50, height = sheight + 50)
    turtle.screensize(swidth,sheight)
    
def getStrings() :
    inputStr = ""
    inputStr = askstring('문자열 입력','거북이 쓸 문자열을 입력')
    return inputStr

def getXY(swidth,sheight) : 
    size,x,y = [0],[0],[0]
    x = random.randrange(-swidth/2 , swidth/2)        #X좌표
    y = random.randrange(-sheight/2 , sheight/2)      #Y좌표
    size = random.randrange(4,56)                     #글자 크기
    return [x,y,size]

def getRGB() :  
    r = random.random()    
    g = random.random()
    b = random.random()
    return [r,g,b]

            