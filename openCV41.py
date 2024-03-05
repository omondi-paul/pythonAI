import cv2
print(cv2.__version__)
import numpy as np

class mpHands:
    import mediapipe as mp
    def __init__(self,still=False,maxHands=2,complexity=1,tol1=.5,tol2=.5):
        self.hands=self.mp.solutions.hands.Hands(still,maxHands,complexity,tol1,tol2)
    def Marks(self,frame):
        myHands=[]
        handsType=[]
        frameRGB=cv2.cvtColor(frame,cv2.COLOR_BGR2RGB)
        results=self.hands.process(frameRGB)
        if results.multi_hand_landmarks != None:
            #print(results.multi_handedness)
            for hand in results.multi_handedness:
                #print(hand)
                #print(hand.classification)
                #print(hand.classification[0])
                handType=hand.classification[0].label
                handsType.append(handType)
            for handLandMarks in results.multi_hand_landmarks:
                myHand=[]
                for landMark in handLandMarks.landmark:
                    myHand.append((int(landMark.x*width),int(landMark.y*height)))
                myHands.append(myHand)
        return myHands,handsType
    
def findDistances(handData):
    distMatrix=np.zeros([len(handData),len(handData)],dtype='float')
    for row in range(0,len(handData)):
        for column in range(0,len(handData)):
            distMatrix[row][column]=((handData[row][0]-handData[column][0])**2 + (handData[row][1]-handData[column][1])**2)**(1/2)
    return distMatrix

def findError(gestureMatrix,unknownMatrix,keyPoints):
    error=0
    for row in keyPoints:
        for column in keyPoints:
            error= error+abs(gestureMatrix[row][column]-unknownMatrix[row][column])
    return error 
        

width=640
height=360
cam=cv2.VideoCapture(0,cv2.CAP_DSHOW)
cam.set(cv2.CAP_PROP_FRAME_WIDTH, width)
cam.set(cv2.CAP_PROP_FRAME_HEIGHT,height)
cam.set(cv2.CAP_PROP_FPS, 30)
cam.set(cv2.CAP_PROP_FOURCC,cv2.VideoWriter_fourcc(*'MJPG'))
findHands=mpHands(1)

keyPoints=[0,4,5,9,13,17,8,12,16,20]
train=True
while True:
    ignore,  frame = cam.read()
    frame=cv2.flip(frame,1)
    handData,handsType=findHands.Marks(frame)
    if train==True:
        if handData != []:
            print('Show your Gesture, press t when Ready')
            if cv2.waitKey(1) & 0xff==ord('t'):
                knownGesture=findDistances(handData[0])
                train=False
                print(knownGesture)

    if train==False:
        if handData !=[]:
            unknownGesture=findDistances(handData[0])
            error=findError(knownGesture,unknownGesture,keyPoints)
            cv2.putText(frame,str(int(error)),(100,175),cv2.FONT_HERSHEY_SIMPLEX,3,(255,0,0),8)

    for hand,handType in zip(handData,handsType):
        if handType=='Right':
            handColor=(255,0,0)
        if handType=='Left':
            handColor=(0,0,255)
        for ind in keyPoints:
            cv2.circle(frame,hand[ind],15,handColor,5)
    cv2.imshow('my WEBcam', frame)
    cv2.moveWindow('my WEBcam',0,0)
    if cv2.waitKey(1) & 0xff ==ord('q'):
        break
cam.release()