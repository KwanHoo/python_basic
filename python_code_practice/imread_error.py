
from enlighten_inference import EnlightenOnnxModel
import cv2
# imread() src.empty() 에러 : 경로(path)를 '\'를 '/'로 바꾸고 r''로 해서 불러오기 
# r"C:\Users\블라블라"  : r을 앞에 써주게되면 로우 스트링임, 이스케이프 문자상관없이 상관없이 그대로 쓴다는거
img14 = cv2.imread(r'D:/python_basic/python_basic/gui_project/image/image10.png')

model = EnlightenOnnxModel()

processed14 = model.predict(img14)

cv2.imshow('test1', img14)
cv2.imshow('dst14', processed14)
cv2.waitKey()
cv2.destroyAllWindows()