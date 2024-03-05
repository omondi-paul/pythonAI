import cv2
print(cv2.__version__)

width=640
height=360
class mpHands:
    import mediapipe as mp
    def __init__(self,maxHands=2,tol1=.5,tol2=.5):
        self.hands=self.mp.solutions.hands.Hands(False,maxHands,tol1,tol2)
    def Marks(self,frame):
        myHands=[]
        frameRGB=cv2.cvtColor(frame,cv2.COLOR_BGR2RGB)
        results=self.hands.process(frameRGB)
        if results.multi_hand_landmarks != None:
            for handLandMarks in results.multi_hand_landmarks:
                myHand=[]
                for landMark in handLandMarks.landmark:
                    myHand.append((int(landMark.x*width),int(landMark.y*height)))
                myHands.append(myHand)
        return myHands

cam=cv2.VideoCapture(0,cv2.CAP_DSHOW)
cam.set(cv2.CAP_PROP_FRAME_WIDTH, width)
cam.set(cv2.CAP_PROP_FRAME_HEIGHT,height)
cam.set(cv2.CAP_PROP_FPS, 30)
cam.set(cv2.CAP_PROP_FOURCC,cv2.VideoWriter_fourcc(*'MJPG'))
findHands=mpHands(1)
paddleWidth=125
paddleHeight=25
paddleColor=(0,255,0)
xPos=300
yPos=40
deltaX=20
deltaY=20
rad=25
while True:
    ignore,  frame = cam.read()
    handData=findHands.Marks(frame)
    for hand in handData:
        cv2.rectangle(frame,(int(hand[8][0]-paddleWidth/2),0),(int(hand[8][0]+paddleWidth/2),paddleHeight),paddleColor,-1) 
        xhan=hand[8][0]
        yhan=hand[8][1]
    cv2.circle(frame,(xPos,yPos),rad,(255,0,255),-1)
    if yPos<=paddleHeight:
        if xPos>=(int(hand[8][0]-paddleWidth/2)) and xPos<=(int(hand[8][0]+paddleWidth/2)):
            deltaY=deltaY*-1
    elif xPos>=width or xPos<=0:
        deltaX=deltaX*(-1)
    elif yPos>=height:
        deltaY=deltaY*(-1)

    xPos=xPos+deltaX
    yPos=yPos+deltaY

    cv2.imshow('my WEBcam', frame)
    cv2.moveWindow('my WEBcam',0,0)
    if cv2.waitKey(1) & 0xff ==ord('q'):
        break
cam.release()