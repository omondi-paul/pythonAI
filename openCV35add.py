import cv2
import mediapipe as mp
print(cv2.__version__)
width=640
height=360
cam= cv2.VideoCapture(0,cv2.CAP_DSHOW)
cam.set(cv2.CAP_PROP_FRAME_WIDTH, width)
cam.set(cv2.CAP_PROP_FRAME_HEIGHT,height)
cam.set(cv2.CAP_PROP_FPS, 30)
cam.set(cv2.CAP_PROP_FOURCC,cv2.VideoWriter_fourcc(*'MJPG'))

pose=mp.solutions.pose.Pose(False,False,True,.5,.5)
mpDraw=mp.solutions.drawing_utils

circleRadius=20
circleColor=(0,0,255)
circleThickness=4
eyeColor=(255,0,0)
eyeRadius=10
eyeThickness=-1

while True:
    ignore, frame= cam.read()
    frameRGB=cv2.cvtColor(frame,cv2.COLOR_BGR2RGB)
    results=pose.process(frameRGB)
    landMarks=[]
    if results.pose_landmarks != None:
        #print(results.pose_landmarks)
        for lm in results.pose_landmarks.landmark:
            #print((lm.x,lm.y))
            landMarks.append((int(lm.x*width),int(lm.y*height)))
        cv2.circle(frame,landMarks[0],circleRadius,circleColor,circleThickness)
        cv2.circle(frame,landMarks[2],eyeRadius,eyeColor,eyeThickness)
        cv2.circle(frame,landMarks[5],eyeRadius,eyeColor,eyeThickness)
    cv2.imshow('my Webcam',frame)
    cv2.moveWindow('my Webcam',0,0)
    if cv2.waitKey(1) & 0xFF==ord('q'):
        break
cam.release()