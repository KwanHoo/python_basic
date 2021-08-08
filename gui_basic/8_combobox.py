from tkinter import *
import tkinter.ttk as ttk     # 콤보박스는 여기서 사용

root = Tk()
root.title("hwankko GUI")  # 제목
root.geometry("640x480")  # 창크기: 가로 x 세로

values = [str(i) + "일" for i in range(1, 32)] # 1 ~ 31 까지의 숫자

combobox = ttk.Combobox(root, height= 5 , values = values )  # height : 목록 몇개 보이는지 갯수
combobox.pack()
combobox.set("요금 납부일") # 최초 목록 제목 설정 및 버튼 클릭을 통한 값 설정 가능

readonly_combobox = ttk.Combobox(root, height= 10 , values = values, state='readonly' )  # state : readonly 옵션으로 글 작성 막음
readonly_combobox.pack()
readonly_combobox.current(0) # 0 번째 인덱스 값 선택

def btncmd():
    print(combobox.get())  # 선택된 값 표시
    print(readonly_combobox.get())


btn = Button(root, text="선택",command = btncmd)
btn.pack()


root.mainloop()  # 창이 닫히지 않도록 해줌