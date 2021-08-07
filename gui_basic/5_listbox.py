from tkinter import *

root = Tk()
root.title("hwankko GUI")  # 제목
root.geometry("640x480")  # 창크기: 가로 x 세로

# listbox : 목록을 관리하는 위젯
listbox = Listbox(root, selectmod="extended", height=0)  
# selectmod : 싱글(한개선택), 익스텐드(한개or 여러개 선택가능)
# height : 0은 전부다 보여줌, 나머지 숫자들어올시 지정된 갯수만큼 리스트 보여줌
listbox.insert(0, "피오라")
listbox.insert(1, "이렐리아")
listbox.insert(2, "일라오이")
listbox.insert(END, "리 신")
listbox.insert(END, "헤카림")
listbox.pack()


def btncmd():
    # 삭제
    listbox.delete(END) # 리스트 맨 뒤 항목을 삭제

    # 갯수 확인
    print("리스트에는", listbox.size(),"개가 있어용!!")

    # 항목 확인 (시작 index, 끝 index)
    print("1번째 부터 3번째까지의 항목: ", listbox.get(0, 2))

    # 선택된 항목 확인 (위치로 반환)
    print("선택된 항목: ", listbox.curselection())

btn = Button(root, text="클릭",command = btncmd)
btn.pack()


root.mainloop()  # 창이 닫히지 않도록 해줌
