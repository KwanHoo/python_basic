from tkinter import *


root = Tk()
root.title("hwankko GUI")  # 제목
root.geometry("640x480")  # 창크기: 가로 x 세로

def create_new_file():
    print("새 파일을 만듭니다.")


menu = Menu(root)


# File 메뉴
menu_file = Menu(menu, tearoff=0)
menu_file.add_command(label="New file", command=create_new_file)
menu_file.add_command(label="New window")
menu_file.add_separator()                   # 구분선
menu_file.add_command(label="Open File...")
menu_file.add_separator()                   # 구분선
menu_file.add_command(label="Save ALL", state="disable") # 비활성화
menu_file.add_separator()
menu_file.add_command(label="Exit", command=root.quit)   # root.quit 창 닫음

menu.add_cascade(label ="File", menu=menu_file)


# Edit 메뉴
menu.add_cascade(label="Edit")

# Language 메뉴 (radio 버튼 통해서 택1)
menu_lang = Menu(menu, tearoff=0)
menu_lang.add_radiobutton(label="Python")
menu_lang.add_radiobutton(label="Jave")
menu_lang.add_radiobutton(label="C++")
menu.add_cascade(label="Language", menu=menu_lang)

# View 메뉴 (check box 사용해서)
menu_view = Menu(menu, tearoff=0)
menu_view.add_checkbutton(label="show minimape")
menu.add_cascade(label="View", menu=menu_view)

root.config(menu=menu)
root.mainloop()  # 창이 닫히지 않도록 해줌