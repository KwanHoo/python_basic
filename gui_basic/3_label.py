from tkinter import *

root = Tk()
root.title("hwankko GUI")  # 제목
root.geometry("640x480")  # 창크기: 가로 x 세로

# 레이블은 글자랑 이미지를 보여줌

label1 = Label(root, text="안녕하세요") 
label1.pack()

photo = PhotoImage(file="gui_basic/img.png")
label2 = Label(root, image=photo)
label2.pack()

def change():
    label1.config(text="또 만나요")  # 버튼눌리면 글자 바뀜
 
    global photo2   # 전역변수로 선언
    photo2 = PhotoImage(file="gui_basic/img2.png")
    label2.config(image=photo2)


btn = Button(root, text="클릭", command=change)
btn.pack()
root.mainloop()  # 창이 닫히지 않도록 해줌