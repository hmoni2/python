from tkinter import *
from tkinter import messagebox
from tkinter.simpledialog import *

#오픈, 닫기 함수 선언
def func_open() :
    value = askinteger("확대 배수", "주사위 숫자(1~6)을 입력하세요", minvalue = 1, maxvalue =6)
    label2.configure(text = str(value))

def func_close() :
    messagebox.showinfo("메뉴 선택","닫기 메뉴를 선택함")
    window.destroy()
    


window = Tk()
window.geometry("400x100")
#메뉴를 제작하기 위한 초기값 선언 #
mainMenu = Menu(window)
window.config(menu = mainMenu)
# 대화상자 생성을 위한 초기값 선언#
label1 = Label(window, text = "입력한 값 : ")
label1.pack()
label2 = Label(window, text = "")
label2.pack(side = "right",anchor = "se" )

fileMenu = Menu(mainMenu)
mainMenu.add_cascade(label = "파일",menu = fileMenu)
fileMenu.add_command(label = "열기",command = func_open)
fileMenu.add_separator()
fileMenu.add_command(label = "종료",command = func_close)

window.mainloop()
