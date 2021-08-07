from tkinter import *

root = Tk()
root.title("hwankko GUI")  # 제목
root.geometry("640x480")  # 창크기: 가로 x 세로


chkvar = IntVar()  # chkvar 에 int 형으로 값을 저장한다
chkbox = Checkbutton(root, text="탑갱 가주기", variable=chkvar) # 체크했을때의 값을
# chkbox.select() # 자동선택 처리
# chkbox.deselect() # 선택 해제 처리
chkbox.pack()

chkvar2 = IntVar()
chkbox2 = Checkbutton(root, text="바위개 먹기", variable=chkvar2)
chkbox2.pack()

def btncmd():
    print(chkvar.get()) # 0 : 체크 해제, 1 : 체크
    print(chkvar2.get())
btn = Button(root, text="클릭",command = btncmd)
btn.pack()


root.mainloop()  # 창이 닫히지 않도록 해줌
