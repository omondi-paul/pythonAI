import cv2
print(cv2.__version__)
import mediapipe as mp
width=640
height=360
cam= cv2.VideoCapture(0,cv2.CAP_DSHOW)
cam.set(cv2.CAP_PROP_FRAME_WIDTH, width)
cam.set(cv2.CAP_PROP_FRAME_HEIGHT,height)
cam.set(cv2.CAP_PROP_FPS, 30)
cam.set(cv2.CAP_PROP_FOURCC,cv2.VideoWriter_fourcc(*'MJPG'))
hands=mp.solutions.hands.Hands(False,2,.5,.5)
mpDraw=mp.solutions.drawing_utils
while True:
    ignore, frameBGR=cam.read()
    frameRGB=cv2.cvtColor(frameBGR,cv2.COLOR_BGR2RGB)
    results=hands.process(frameRGB)
    if results.multi_hand_landmarks != None:
        for handLandMarks in results.multi_hand_landmarks:
            mpDraw.draw_landmarks(frameBGR,handLandMarks,mp.solutions.hands.HAND_CONNECTIONS)


    cv2.imshow('my Webcam',frameBGR)
    cv2.moveWindow('my Webcam',0,0)
    if cv2.waitKey(1) & 0xFF==ord('q'):
        break
cam.release()