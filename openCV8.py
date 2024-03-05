import cv2 
import numpy as np
print(cv2.__version__)
import time
WEBCamNumber=0
width=640
height=360
myThick=4
myRadius=30
myColor=(0,0,0)
myText='Hey there Boss!'
myFont=cv2.FONT_HERSHEY_COMPLEX
recColor=(0,255,0)
fontColor=(255,0,0)
upperLeft=(250,140)
lowerRight=(390,220)
boxColor=(255,0,0)
textStart=(120,120)
fontSize=2
textHeavy=2

cam= cv2.VideoCapture(WEBCamNumber,cv2.CAP_DSHOW)
cam.set(cv2.CAP_PROP_FRAME_WIDTH, width)
cam.set(cv2.CAP_PROP_FRAME_HEIGHT,height)
cam.set(cv2.CAP_PROP_FPS, 10)
cam.set(cv2.CAP_PROP_FOURCC,cv2.VideoWriter_fourcc(*'MJPG'))
tlast=time.time()
time.sleep(.01)
fpsFILT=10
while True:
    dT=time.time()-tlast
    fps=1/dT
    fpsFILT=fpsFILT*0.97+fps*.03
    print(fpsFILT)
    tlast=time.time()
    ignore, frame= cam.read()
    frame[140:220,250:390]=boxColor
    cv2.rectangle(frame,upperLeft,lowerRight,recColor,myThick)
    cv2.circle(frame,(int(width/2),int(height/2)),myRadius,myColor,myThick)
    cv2.putText(frame,myText,textStart,myFont,fontSize,fontColor,textHeavy)
    cv2.rectangle(frame,(0,0),(120,35),(255,0,255),-1)
    cv2.putText(frame,str(int(fpsFILT))+' fps',(5,30),myFont,1,(0,255,255),1)
    cv2.imshow('my WEBcam',frame)
    cv2.moveWindow('my WEBcam',0,0)

    if cv2.waitKey(1) & 0xFF==ord('q'):
        break
    
cam.release()




        
