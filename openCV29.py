import cv2
print(cv2.__version__)
import mediapipe as mp

hands=mp.solutions.hands.Hands(False,2,.5,.5)
mpDraw=mp.solutions.drawing_utils
width=640
height=360
def parseLandmarks(frame):
    myHands=[] #array of array, [[],[]] with the each having 21 values for the hands
    frameRGB=cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    results=hands.process(frameRGB)
    if results.multi_hand_landmarks != None:
        for handLandMarks in results.multi_hand_landmarks:
            myHand=[]
            for landMark in handLandMarks.landmark:
                myHand.append((int(landMark.x*width),int(landMark.y*height)))
            myHands.append(myHand)
    return myHands




cam= cv2.VideoCapture(0,cv2.CAP_DSHOW)
cam.set(cv2.CAP_PROP_FRAME_WIDTH, width)
cam.set(cv2.CAP_PROP_FRAME_HEIGHT,height)
cam.set(cv2.CAP_PROP_FPS, 30)
cam.set(cv2.CAP_PROP_FOURCC,cv2.VideoWriter_fourcc(*'MJPG'))
while True:
    ignore, frame= cam.read()
    myHands=parseLandmarks(frame)
    for hand in myHands:
        for dig in [8,12,16,20]:
            cv2.circle(frame,hand[dig],10,(0,255,0),3)

    cv2.imshow('my Webcam',frame)
    cv2.moveWindow('my Webcam',0,0)
    if cv2.waitKey(1) & 0xFF==ord('q'):
        break
cam.release()