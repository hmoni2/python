from tkinter import *
from tkinter import messagebox
from time import *

fnameList = ["jeju1.gif", "jeju2.gif", "jeju3.gif", "jeju4.gif", "jeju5.gif", "jeju6.gif", "jeju7.gif", "jeju8.gif", "jeju9.gif"]
photoList = [None] * 9
num = 0 

def clickMouse(event) :
    txt = ""
    global num
    if event.num == 1 :
        txt += "마우스 왼쪽 버튼이 ("
        num += 1
        if num > 8 :
            num = 0
        photo = PhotoImage(file = "gif/" + fnameList[num])
        pLabel.configure(image = photo)
        pLabel.image = photo

    elif event.num == 3 :
        txt += "마우스 오른쪽 버튼이 ("
        num -= 1
        if num < 0 :
            num = 8
        photo = PhotoImage(file = "gif/" + fnameList[num])
        pLabel.configure(image = photo)
        pLabel.image = photo
    
    txt += str(event.y) + "," + str(event.x) + ")에서 클릭됨"
    txt += str(event.y_root) + "," + str(event.x_root) + ")에서 클릭됨"
    label1.configure(text = txt)

#MAIN#
window = Tk()
window.geometry("700x500")
window.title("사진 앨범 보기")

btnPrev = Button(window, text = "<< 이전 ", command = clickMouse)
btnNext = Button(window, text = "다음 >>", command = clickMouse)

photo = PhotoImage(file = "gif/" + fnameList[0])
pLabel = Label(window, image = photo)

btnPrev.place(x = 250, y = 10)
btnNext.place(x = 400, y = 10)
pLabel.place(x = 15, y = 50)

window.bind("<Button>", clickMouse)

label1 = Label(window, text = "이곳이 바뀜")
label1.pack(expand = 1, anchor = CENTER)

window.mainloop()
