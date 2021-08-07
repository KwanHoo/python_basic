from tkinter import *

root = Tk()
root.title("hwankko GUI")  # 제목
root.geometry("640x480")  # 창크기: 가로 x 세로


Label(root, text="@@@@@@@@@메뉴를 선택하세욧!@@@@@@@").pack()

burger_var = IntVar()
btn_burger1 = Radiobutton(root, text="불고기버거", value=1, variable=burger_var)
btn_burger2 = Radiobutton(root, text="콰트로치즈와퍼", value=2, variable=burger_var)
btn_burger2.select()
btn_burger3 = Radiobutton(root, text="통베이컨와퍼", value=3, variable=burger_var)

btn_burger1.pack()
btn_burger2.pack()
btn_burger3.pack()

Label(root, text="@@@@@@@음료를 고르세욧!@@@@@@@@@").pack()

drink_var = StringVar()
btn_drink1 = Radiobutton(root, text="Coke", value="콜라", variable = drink_var)
btn_drink1.select()
btn_drink2 = Radiobutton(root, text="ZeroCoke", value="제로콜라", variable = drink_var)
btn_drink3 = Radiobutton(root, text="Sprite", value="스프라이트", variable = drink_var)

btn_drink1.pack()
btn_drink2.pack()
btn_drink3.pack()

def btncmd():
    print(burger_var.get()) # 버거 중에서 선택된 라이도 항목의 값(value)을 반환
    print(drink_var.get()) # 음료선택값 출력


btn = Button(root, text="주문",command = btncmd)
btn.pack()


root.mainloop()  # 창이 닫히지 않도록 해줌
