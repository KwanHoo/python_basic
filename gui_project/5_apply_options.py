import os
from tkinter import * # __all__ 에 저장된 모듈 임포트됨
import tkinter.ttk as ttk
from tkinter import filedialog # 파일 불로오는 기능 (서브 모듈이라 *로 안불러와짐)
import tkinter.messagebox as msgbox  # 메세지 박스 사용시 불러옴
from PIL import Image # 이미지 관련 모듈


root = Tk()
root.title("hwankko GUI")  # 제목

# 파일 추가 (선택한 파일 모두)
def add_file():          # 복수개의 파일 선택
    files =  filedialog.askopenfilenames(title="이미지 파일을 선택하세요", \
         filetypes=(("PNG 파일", "*.png"), ("모든 파일", "*.*")), \
              initialdir = "D:/python_basic")  # 최초에 뛰어줄 디렉토리 명시(최초에 D:/경로)
                            # r"C:\Users\블라블라"  : r을 앞에 써주게되면 로우 스트링임, 이스케이프 문자상관없이 상관없이 그대로 쓴다는거

    
    # 사용자가 선택한 파일 목록
    for file in files:
        # print(file)
        list_file.insert(END, file) # 리스트 파일 프레임에 추가


# 선택 파일 목록에서 삭제
def del_file():
    #print(list_file.curselection()) # 현재 인덱스 번호 출력

    for index in reversed(list_file.curselection()): # reversed : 거꾸로 반환해줌 (인덱스의 경우 뒤에서부터 재껴야됨)
        list_file.delete(index)


# 저장 경로 (폴더)
def brows_dest_path():
    folder_selected = filedialog.askdirectory() # 폴더 선택
    if folder_selected == '': #사용자가 취소를 누를 때
        print('폴더 선택 취소')
        return
    # print(folder_selected)
    txt_dest_path.delete(0, END)  # 먼저 저장되어있는거 삭제
    txt_dest_path.insert(0, folder_selected) # 경로란에 들어가짐

###########
# 이미지 통합
def merge_image():

    try:  # 예외처리, 버그(저장 문제)
            
        ############# 옵션처리---------
        # 가로넓이
        img_width = cmb_width.get()
        if img_width == "원본유지":
            img_width = -1 # -1 일때는 원본 기준으로 통합
        else:
            img_width = int(img_width)
        
        # 간격
        img_space = cmb_space.get()
        if img_space == "좁게":
            img_space = 30
        elif img_space == "보통":
            img_space = 60
        elif img_space == "넓게":
            img_space = 90
        else:  # "없음"
            img_space = 0

        # 포맷
        img_format = cmb_format.get().lower() # 확장자 값 받아와서 소문자로 변경
        ##########################----- 

        #print(list_file.get(0, END)) # 모든 파일 목록을 가지고 오기
        images = [Image.open(x) for x in list_file.get(0, END)]

        # 가로넓이 옵션 --- 이미지 사이즈 리스트에 넣어서 하나씩 처리
        image_sizes = [] #(width1, height1),(wi2, hi2),(wi3, hi3),...
        if img_width > -1 :
            # width 값 변경
            image_sizes =[(int(img_width),int(img_width * x.size[1] / x.size[0])) for x in images]
        else:
            # 원본 사이즈 사용
            image_sizes = [(x.size[0], x.size[1]) for x in  images]

        # +) 계산식
        # ex) (100 * 60)img가 있음, -> width를 80으로 줄이면 height 는?
        # (원본 w) : (원본 h) = (변경 w) : (변경 h)
        #     x    :    y     =    x'    :   y'
        #  xy' = yx'
        #  y' = x'y / x  = 80 x 60 / 100 = 48

        # 우리 코드에 대입하면?
        # x = width = size[0]
        # y = height = size[1]
        # x' = img_width # 변경값 해야함
        # y' = x'y / x = img_width * size[1] / size[0]

        widths, heigths = zip(*(image_sizes))

        max_width, total_height = max(widths), sum(heigths) # 최대 넓이와, 전체 높이



        # 스케치북

        if img_space > 0:  # 이미지 간격 옵션 조정
            total_height += (img_space * (len(images) -1))

        result_img = Image.new("RGB", (max_width, total_height), (255,255,255)) # 배경 흰색
        y_offset = 0   # x는 그대로 인데 y 좌표 기준으로 하나씩 늘려가면서 붙이는 작업을 위한 변수 / y 위치
    
        # 프로그레스 바 추가
        for idx, img in enumerate(images): # enumerate 이용하여 index 반환
            # width가 원본유지가 아닐때에는 이미지 크기 조정
            if img_width > -1:
                img = img.resize(image_sizes[idx])

            result_img.paste(img, (0,y_offset))
            y_offset += (img.size[1] + img_space)# height 값 + 사용자가 지정한 간격

            progress = (idx + 1) / len(images) * 100 # 실제 퍼센트 정보를 계산
            p_var.set(progress)
            progress_bar.update()

        # 포맷 옵션 처리
        file_name = "merge_photo_R." + img_format
        dest_path = os.path.join(txt_dest_path.get(), file_name)  # 저장경로 설정
        result_img.save(dest_path)  # 이미지 저장
        msgbox.showinfo("알림", "작업이 완료되었습니다.")
    except Exception as err: # 예외처리
        msgbox.showerror("에러", err)

# 시작
def start():
    # 각 옵션 값들 확인
    print("가로넓이 : ", cmb_width.get())
    print("간격 : ", cmb_space.get())
    print("포맷 : ", cmb_format.get())

    # 파일 목록 확인
    if list_file.size() == 0:  # 파일 선택 없을시 경고메세지
        msgbox.showwarning("경고", "이미지 파일을 추가하세요")
        return

    # 저장 경로 확인
    if len(txt_dest_path.get()) == 0:
        msgbox.showwarning("경고", "저장 경로를 선택하세요")
        return

    ##########
    # 이미지 통합 작업
    merge_image()


# 파일 프레임 (파일 추가, 선택 삭제)

file_frame = Frame(root)
file_frame.pack(fill="x", padx= 5, pady=5)

btn_add_file = Button(file_frame, padx=5, pady=5,width =12, text="파일추가", command=add_file)
btn_add_file.pack(side="left")

btn_del_file = Button(file_frame,padx=5, pady=5,width =12, text="파일삭제", command=del_file)
btn_del_file.pack(side="right")

# 리스트 프레임
list_frame = Frame(root)
list_frame.pack(fill="both", padx= 5, pady=5)

scrollbar = Scrollbar(list_frame)
scrollbar.pack(side="right", fill="y")

list_file = Listbox(list_frame, selectmode="extended", height=15, yscrollcommand=scrollbar.set) # yscrollcommand=scrollbar.set 이걸 해줘야 서로 맵핑이됨
list_file.pack(side="left", fill="both", expand=True)
scrollbar.config(command=list_file.yview)

# 저장 경로 프레임
path_frame = LabelFrame(root, text="저장경로")
path_frame.pack(fill="x", padx= 5, pady=5, ipady=5) # fill="x"  : 프레임 늘려줌

txt_dest_path = Entry(path_frame)
txt_dest_path.pack(side="left", fill="x", expand=True,  padx= 5, pady=5, ipady=4) # ipad : 안쪽 패딩

btn_dest_path = Button(path_frame, text="찾아보기", width=10, command=brows_dest_path)
btn_dest_path.pack(side="right", padx= 5, pady=5)


# 옴션 프레임
frame_option = LabelFrame(root, text="옵션")
frame_option.pack(padx= 5, pady=5, ipady=5)

# 1. 가로 넓이 옵션
# 가로넓이 레이블
lbl_width = Label(frame_option, text="가로넓이", width=8)
lbl_width.pack(side="left", padx= 5, pady=5)

# 가로넓이 콤보박스
opt_width = ["원본유지", "1024", "800", "640"]
cmb_width = ttk.Combobox(frame_option, state="readonly", values=opt_width, width=10)
cmb_width.current(0) # 첫번째 값 기본선택
cmb_width.pack(side="left", padx= 5, pady=5)



# 2. 간격 옵션
# 간격 옵션 레이블
lbl_space = Label(frame_option, text="간격", width=8)
lbl_space.pack(side="left", padx= 5, pady=5)

# 간격 옵션 콤보
opt_space = ["없음", "좁게", "보통", "넓게"]
cmb_space = ttk.Combobox(frame_option, state="readonly", values=opt_space, width=10)
cmb_space.current(0) # 첫번째 값 기본선택
cmb_space.pack(side="left", padx= 5, pady=5)

# 3. 파일 포맷 옵션
# 파일포맷 옵션 레이블
lbl_format = Label(frame_option, text="포맷", width=8)
lbl_format.pack(side="left", padx= 5, pady=5)

# 파일포맷 옵션 콤보
opt_format = ["PNG", "JPG", "BMP"]
cmb_format = ttk.Combobox(frame_option, state="readonly", values=opt_format, width=10)
cmb_format.current(0) # 첫번째 값 기본선택
cmb_format.pack(side="left", padx= 5, pady=5)

# 진행 상황 Progress Bar
frame_progress = LabelFrame(root, text="진행상황")
frame_progress.pack(fill="x", padx= 5, pady=5, ipady=5)

p_var = DoubleVar()
progress_bar = ttk.Progressbar(frame_progress, maximum=100, variable=p_var)
progress_bar.pack(fill="x", padx= 5, pady=5)

# 실행 프레임
frame_run = Frame(root)
frame_run.pack(fill="x", padx= 5, pady=5)

btn_close = Button(frame_run, padx=5, pady=5, text="닫기", width=12, command=root.quit)
btn_close.pack(side="right", padx= 5, pady=5)

btn_start = Button(frame_run, padx=5, pady=5, text="시작", width=12, command= start)
btn_start.pack(side="right", padx= 5, pady=5)





root.resizable(False, False) # x(너비), y(높이) 값 변경 불가 (창 크기 변경 불가)
root.mainloop()  # 창이 닫히지 않도록 해줌
