import cv2 #ライブラリインポート
import sys #sysライブラリインポート
img=cv2.imread("cat.jpg")

if img is None:
    print("画像を正しく読み込めていません")
    sys.exit()#ライブラリの終了。プログラムの終了ともいえる

cascade=cv2.CascadeClassifier("haarcascade_frontalcatface.xml")
#カスケード分類機の読み込み

gray=cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
face=cascade.detectMultiScale(gray, minNeighbors=5, minSize=(10,10))
#grayは白黒画像に変更したファイルを変数に、faceはgrayから猫の顔を探している

if not len(face)==0:
    for(x,y,w,h) in face:
        cv2.rectangle(img, (x,y), (x + w, y + h), (0,0,200), 3)#猫の顔が見つかったら赤枠で囲む

else:
    print("猫の顔が判別できていません")
    sys.exit()

cv2.imwrite("result.jpg",img)#編集画像を保存
cv2.imshow("image",img)
cv2.waitKey(0)
