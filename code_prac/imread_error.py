
from enlighten_inference import EnlightenOnnxModel
import cv2
# imread() src.empty() 에러 : 경로(path)를 '\'를 '/'로 바꾸고 r''로 해서 불러오기 
img14 = cv2.imread(r'D:/python_basic/python_basic/gui_project/image10.png')

model = EnlightenOnnxModel()

processed14 = model.predict(img14)

cv2.imshow('test1', img14)
cv2.imshow('dst14', processed14)
cv2.waitKey()
cv2.destroyAllWindows()