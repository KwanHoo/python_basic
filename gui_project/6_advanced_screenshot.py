# 키보드 모듈 : 사용자가 키입력을 하면은 그 값을 낚아채는거
import time
import keyboard

from PIL import ImageGrab

def screenshot():
    curr_time = time.strftime("_%Y%m%d_%H%M%S")  # 시간값 ex)20210814_191320
    img = ImageGrab.grab()
    img.save("image{}.png".format(curr_time))

keyboard.add_hotkey("F9", screenshot) # 사용자가 F9 키를 누르면 스크린 샷 저장

keyboard.wait("esc") # 사용자가 esc를 누를 떄 까지 프로그램 수행