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

while True:
    ignore, frame= cam.read()
    frameRGB=cv2.cvtColor(frame,cv2.COLOR_BGR2RGB)
    results=pose.process(frameRGB)
    if results.pose_landmarks != None:
        mpDraw.draw_landmarks(frame,results.pose_landmarks,mp.solutions.pose.POSE_CONNECTIONS)
    cv2.imshow('my Webcam',frame)
    cv2.moveWindow('my Webcam',0,0)
    if cv2.waitKey(1) & 0xFF==ord('q'):
        break
cam.release()