import cv2
print(cv2.__version__)
import time
width=640
height=360
x=0
y=0
w=1
h=1
cam= cv2.VideoCapture(0,cv2.CAP_DSHOW)
cam.set(cv2.CAP_PROP_FRAME_WIDTH, width)
cam.set(cv2.CAP_PROP_FRAME_HEIGHT,height)
cam.set(cv2.CAP_PROP_FPS, 30)
cam.set(cv2.CAP_PROP_FOURCC,cv2.VideoWriter_fourcc(*'MJPG'))

faceCascade=cv2.CascadeClassifier('haar\haarcascade_frontalface_default.xml')
eyeCascade=cv2.CascadeClassifier('haar\haarcascade_eye.xml')
fps=10
timeStamp=time.time()
while True:
    ignore, frame= cam.read()
    frameGray=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    faces=faceCascade.detectMultiScale(frameGray,1.3,5)
    for face in faces:
        print(faces)
        x,y,w,h=face
        cv2.rectangle(frame,(x,y),(x+w,y+h),(255,0,0),3)
        frameROI=frame[y:y+h,x:x+w]
        frameROIGray=cv2.cvtColor(frameROI,cv2.COLOR_BGR2GRAY)
        eyes=eyeCascade.detectMultiScale(frameROIGray)
        for eye in eyes:
            xEye,yEye,wEye,hEye=eye
            cv2.rectangle(frame[y:y+h,x:x+w],(xEye,yEye),(xEye+wEye,yEye+hEye),(0,255,0),3)
    

    loopTime=time.time()-timeStamp
    timeStamp=time.time()
    fpsNew=1/loopTime
    fps=.9*fps+.1*fpsNew  
     
    cv2.rectangle(frame,(0,0),(120,35),(255,0,255),-1)
    cv2.putText(frame,str(int(fps))+' fps',(5,30),cv2.FONT_HERSHEY_PLAIN,2,(255,0,0),2)
    cv2.imshow('my Webcam',frame)
    cv2.moveWindow('my Webcam',0,0)
    if cv2.waitKey(1) & 0xFF==ord('q'):
        break
cam.release()