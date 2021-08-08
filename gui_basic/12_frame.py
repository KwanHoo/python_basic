from tkinter import *

root = Tk()
root.title("hwankko GUI")  # 제목
root.geometry("640x480")  # 창크기: 가로 x 세로


Label(root, text="메뉴를 선택해 주세요.").pack(side="top")

Button(root, text="주문하기").pack(side="bottom")

# 버거 메뉴 프레임
frame_burger = Frame(root, relief="solid", bd=1)
frame_burger.pack(side="left", fill="both", expand=True)

Button(frame_burger, text="콰트로치즈와퍼").pack()
Button(frame_burger, text="통베이컨와퍼").pack()
Button(frame_burger, text="트리플치즈와퍼").pack()


# 음료 메뉴 프레임
frame_drink = LabelFrame(root, text="음료")
frame_drink.pack(side="right",fill="both", expand=True)
Button(frame_drink, text="제로코크").pack()
Button(frame_drink, text="스프라이트").pack()


root.mainloop()  # 창이 닫히지 않도록 해줌