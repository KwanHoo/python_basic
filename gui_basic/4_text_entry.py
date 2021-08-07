from tkinter import *

root = Tk()
root.title("hwankko GUI")  # 제목
root.geometry("640x480")  # 창크기: 가로 x 세로

# 글자 입력할 수 있는 텍스트박스
txt = Text(root, width=30, height=5)  # Text 여러줄 입력할때 사용
txt.pack()

# 안내 메시지 삽입
txt.insert(END, "글자를 입력하세욧!")

e= Entry(root, width=30) # Entry 요기서는 enter가 사용이 안됨
e.pack()
e.insert(0, " 한 줄만 입력해욧!")

def btncmd():
    # 내용 출력
    print(txt.get("1.0", END))  # 라인위치(1 : 첫번째 라인).컬럼위치(0 : 0번째 컬럼위치) , 전부다 가져와
    print(e.get())

    # 내용 삭제
    txt.delete("1.0", END)
    e.delete(0,END)

btn = Button(root, text="클릭",command = btncmd)
btn.pack()


root.mainloop()  # 창이 닫히지 않도록 해줌
