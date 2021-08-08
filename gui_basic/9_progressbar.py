import time

from tkinter import *
import tkinter.ttk as ttk     # 프로그레스바 여기서 사용

root = Tk()
root.title("hwankko GUI")  # 제목
root.geometry("640x480")  # 창크기: 가로 x 세로

# 프로그레스 바 : 퍼센트로 얼마정도 진행되는지 보여줌

progressbar = ttk.Progressbar(root, maximum=100, mode="indeterminate") # mode : indeterminate(결정되지 않음,언제끝날지 모름)
progressbar.start(10)  # 10 ms 마다 움직임
progressbar.pack()

progressbar1 = ttk.Progressbar(root, maximum=100, mode="determinate") # mode : determinate(처음부터 끝까지참,언제끝날지 모름)
progressbar1.start(10)  # start:프로그레스바 움직임,10 ms 마다 움직임
progressbar1.pack()

def btncmd():
    progressbar.stop() # 작동 중지


btn = Button(root, text="중지",command = btncmd)
btn.pack()

p_var2 = DoubleVar()  # 실수값
progressbar2 = ttk.Progressbar(root, maximum=100, length=150, variable=p_var2)
progressbar2.pack()

def btncmd2():
    for i in range(1, 101):
        time.sleep(0.01) # 0.01초 대기

        p_var2.set(i)           # 프로그레스 바 의 값 설정
        progressbar2.update()   # gui상 시각적으로 보여주기 위해 값을 업뎃
        print(p_var2.get())

btn2 = Button(root, text="시작",command = btncmd2)
btn2.pack()


root.mainloop()  # 창이 닫히지 않도록 해줌