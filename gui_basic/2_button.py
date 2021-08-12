from tkinter import *

root = Tk()
root.title("hwankko GUI")  # 제목

btn1 = Button(root, text="버튼1")
btn1.pack()  # pack을 호출해줘야만 메인 윈도우에 포함됨

# 여백으로 버튼크기 조절
btn2 = Button(root, padx=50, pady=30, text = "버튼2222222222222222222")  
btn2.pack() 
btn3 = Button(root, padx=25, pady=15, text = "버튼3333")
btn3.pack()
# 버튼 고정된 사이즈
btn4 = Button(root, width=10, height=3, text="버튼444444444444")  
btn4.pack()

btn5 = Button(root, fg="red", bg="green", text="버튼5")
btn5.pack()


# 이미지 통해서 버튼 만들기
photo = PhotoImage(file="img.png") # 이미지 불러옴
btn6 = Button(root, image=photo)  
btn6.pack()


#버튼 동작
def btncmd():
    print("버튼이 클릭 되었습니다")
btn7 = Button(root, text="동작하는 버튼", command=btncmd)
btn7.pack()


root.mainloop()  # 창이 닫히지 않도록 해줌