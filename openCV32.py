import cv2
print(cv2.__version__)

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
width=640
height=360
cam=cv2.VideoCapture(0,cv2.CAP_DSHOW)
cam.set(cv2.CAP_PROP_FRAME_WIDTH, width)
cam.set(cv2.CAP_PROP_FRAME_HEIGHT,height)
cam.set(cv2.CAP_PROP_FPS, 30)
cam.set(cv2.CAP_PROP_FOURCC,cv2.VideoWriter_fourcc(*'MJPG'))
findHands=mpHands(1)
paddleWidth=125
paddleHeight=25
paddleColor=(0,0,255)
ballRadius=15
ballColor=(255,0,0)
xPos=int(width/2)
yPos=int(height/2)
deltaX=5
deltaY=5
score=0
lives=5
font=cv2.FONT_HERSHEY_SIMPLEX
ind=8
while True:
    ignore,  frame = cam.read()
    frame=cv2.flip(frame,1)
    cv2.circle(frame,(xPos,yPos),ballRadius,ballColor,-1)
    cv2.putText(frame,str(score),(25,int(6*paddleHeight)),font,6,paddleColor,5)
    cv2.putText(frame,str(lives),(width-125,int(6*paddleHeight)),font,6,paddleColor,5)
    handData=findHands.Marks(frame)
    for hand in handData:
        cv2.rectangle(frame,(int(hand[8][0]-paddleWidth/2),0),(int(hand[8][0]+paddleWidth/2),paddleHeight),paddleColor,-1)
    topEdgeBall=yPos-ballRadius
    bottomEdgeBall=yPos+ballRadius
    leftEdgeBall=xPos-ballRadius
    rightEdgeBall=xPos+ballRadius
    if leftEdgeBall<=0 or rightEdgeBall>=width:
        deltaX=deltaX*(-1)
    if bottomEdgeBall>=height:
        deltaY=deltaY*(-1)
    if topEdgeBall<=paddleHeight:
        if xPos>(int(hand[ind][0]-paddleWidth/2)) and int(xPos<(hand[ind][0]+paddleWidth/2)):
            deltaY=deltaY*(-1)
            score=score+1
            if score%5==0:
                deltaX=deltaX*2
                deltaY=deltaY*2
                
        else:
            xPos=int(width/2)
            yPos=int(height/2)
            lives=lives-1
    xPos+=deltaX
    yPos+=deltaY
    cv2.imshow('my WEBcam', frame)
    cv2.moveWindow('my WEBcam',0,0)
    if lives==0:
        cv2.putText(frame,'GAME OVER',(int(width/2),int(height/2)),font,5,paddleColor,5)
        cv2.waitKey(3000)
        break
    if cv2.waitKey(1) & 0xff ==ord('q'):
        break
cam.release()