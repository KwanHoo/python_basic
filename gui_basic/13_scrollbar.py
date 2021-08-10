from tkinter import *

root = Tk()
root.title("hwankko GUI")  # 제목
root.geometry("640x480")  # 창크기: 가로 x 세로


frame = Frame(root)
frame.pack()

scrollbar = Scrollbar(frame)
scrollbar.pack(side="right", fill="y") # 스크롤바 오른쪽으로 , y방향으로 스크롤 채움

# set이 없으면 스크롤을 내려도 다시 올라옴
listbox = Listbox(frame, selectmode="extended", height="10", yscrollcommand=scrollbar.set)


for i in range(1, 32): # 1 ~ 31일
    listbox.insert(END, str(i) + "일") # 1일, 2일, ...
listbox.pack(side="left") # 리스트박스는 왼쪽으로

scrollbar.config(command=listbox.yview) # 스크롤에 따라 리스트박스 상하 움직이는거 처리해줌

root.mainloop()  # 창이 닫히지 않도록 해줌