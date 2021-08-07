from tkinter import *

root = Tk()
root.title("hwankko GUI")  # 제목
root.geometry("640x480")  # 창크기: 가로 x 세로
# root.geometry("640x480+100+300")  # 창크기: 가로 x 세로 + x좌표 + y좌표

root.resizable(False, False) # x(너비), y(높이) 값 변경 불가 (창 크기 변경 불가)

root.mainloop()  # 창이 닫히지 않도록 해줌
