import cv2
import imutils
#import serial
import math
import time
import pyautogui as pag
from playsound import playsound 
#arduino = serial.Serial(port='COM8', baudrate=9600, timeout=.1) 
prevxco = 0
prevyco = 0
dist = 0
pag.moveTo(1920,720,0.01)
pag.mouseDown()
face_classifier = cv2.CascadeClassifier(
    cv2.data.haarcascades + "haarcascade_frontalface_default.xml"
)
video_capture = cv2.VideoCapture(0)
def detect_bounding_box(vid):
    gray_image = cv2.cvtColor(vid, cv2.COLOR_BGR2GRAY)
    faces = face_classifier.detectMultiScale(gray_image, 1.1, 5, minSize=(40, 40))
    for (x, y, w, h) in faces:
        cv2.rectangle(vid, (x, y), (x + w, y + h), (0, 255, 0), 4)
    return faces
while True:

    result, video_frame = video_capture.read()
    video_frame = imutils.resize(video_frame, width=800)
    if result is False:
        break  

    faces = detect_bounding_box(
        video_frame
    )
    cv2.imshow(
        "Tracking", video_frame
    ) 
    try:
        l = str(faces).replace("[", "").replace("]", "").split(" ")
        if(str(faces) != "()"):
            if "" in l:
                l.remove("")
            x = (f"X{l[0]}")
            y = (f"Y{l[1]}")
            xco = int(l[0])-300
            yco = int(l[1])-200
            
            pag.moveTo((-xco)/3+1920,yco/3+720,0.1)
            if(prevxco!=0):
                dist = math.sqrt((xco-prevxco)**2+(yco-prevyco)**2)
            print(dist)
            if dist>60:
                #arduino.write(bytes('a','utf-8'))
                playsound('shoot.mp3')
            #arduino.write(bytes(x, 'utf-8'))
            #arduino.write(bytes(y, 'utf-8'))
            print(xco,yco)
            time.sleep(0.07)
            prevxco = xco
            prevyco = yco
    except:
        pass
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break
video_capture.release()
cv2.destroyAllWindows()
