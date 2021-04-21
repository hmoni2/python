from tkinter import *
from tkinter import messagebox

window = Tk()

## 이 부분에서 화면을 구성하고 처리 ## 

def checkFunc() :
    if chk.get() == 0 :
        messagebox.showinfo("","체크버튼이 꺼졌어요.")
    else :
        messagebox.showinfo("","체크버튼이 켜졌어요.")

def radioFunc() :
    if var.get() == 1 :
        label1.configure(text = "파이썬")
    elif var.get() == 2 :
        label1.configure(text = "C++")
    else :
        label1.configure(text = "JAVA")

window.title("윈도 창 연습")
window.geometry("400x400")
window.resizable(width = FALSE, height = FALSE)

chk = IntVar()
cb1 = Checkbutton(window, text = "클릭하세요", variable = chk, command = checkFunc)
cb1.pack()
button1 = Button(window, text = "파이썬 종료", fg = "red", command = quit)
button1.pack()

var = IntVar()
rb1 = Radiobutton(window, text = "파이썬", variable = var, value = 1, command = radioFunc)
rb2 = Radiobutton(window, text = "C++", variable = var, value = 2, command = radioFunc)
rb3 = Radiobutton(window, text = "JAVA", variable = var, value = 3, command = radioFunc)

label1 = Label(window, text="선택한 언어 : ", fg = "red")
rb1.pack()
rb2.pack()
rb3.pack()
window.mainloop()