import cv2
print(cv2.__version__)

class mpFaceMesh:
    import mediapipe as mp
    def __init__(self,still=False,numFace=3,redefine=True,tol1=.5,tol2=.5,drawMesh=True):
        self.myFaceMesh=self.mp.solutions.face_mesh.FaceMesh(still,numFace,redefine,tol2,tol2)
        self.myDraw=self.mp.solutions.drawing_utils
        self.draw=drawMesh
    def Marks(self,frame):
        global width
        global height
        frameRGB=cv2.cvtColor(frame,cv2.COLOR_BGR2RGB)
        results=self.myFaceMesh.process(frameRGB)
        facesMeshLandMarks=[]
        if results.multi_face_landmarks != None:
            for faceMesh in results.multi_face_landmarks:
                faceMeshLandMarks=[]
                for lm in faceMesh.landmark:
                    loc=(int(lm.x*width),int(lm.y*height))
                    faceMeshLandMarks.append(loc)
                facesMeshLandMarks.append(faceMeshLandMarks)
                if self.draw==True:
                    self.myDraw.draw_landmarks(frame,faceMesh)
        return facesMeshLandMarks


class mpFace:
    import mediapipe as mp 
    def __init__(self):
        self.myFace=self.mp.solutions.face_detection.FaceDetection()
    def Marks(self,frame):
        frameRGB=cv2.cvtColor(frame,cv2.COLOR_BGR2RGB)
        results=self.myFace.process(frameRGB)
        faceBoundBoxs=[]
        if results.detections != None:
            for face in results.detections:
                bBox=face.location_data.relative_bounding_box
                topLeft=(int(bBox.xmin*width),int(bBox.ymin*height))
                bottomRight=(int((bBox.xmin+bBox.width)*width),int((bBox.ymin+bBox.height)*height))
                faceBoundBoxs.append((topLeft,bottomRight))
        return faceBoundBoxs

class mpPose:
    import mediapipe as mp
    def __init__(self,still=False,complexity=1,smooth=True,seg=False,smoothData=True, tol1=.5, tol2=.5):
        self.myPose=self.mp.solutions.pose.Pose(still,complexity,smooth,seg,smoothData,tol1,tol2)
    def Marks(self,frame):
        frameRGB=cv2.cvtColor(frame,cv2.COLOR_BGR2RGB)
        results=self.myPose.process(frameRGB)
        poseLandmarks=[]
        if results.pose_landmarks:
            for lm in results.pose_landmarks.landmark:            
                poseLandmarks.append((int(lm.x*width),int(lm.y*height)))
        return poseLandmarks

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

width=640
height=360
cam=cv2.VideoCapture(0,cv2.CAP_DSHOW)
cam.set(cv2.CAP_PROP_FRAME_WIDTH, width)
cam.set(cv2.CAP_PROP_FRAME_HEIGHT,height)
cam.set(cv2.CAP_PROP_FPS, 30)
cam.set(cv2.CAP_PROP_FOURCC,cv2.VideoWriter_fourcc(*'MJPG'))

findHands=mpHands(2)
findFace=mpFace()
findPose=mpPose()
findMesh=mpFaceMesh(drawMesh=False)

font=cv2.FONT_HERSHEY_SIMPLEX
fontColor=(0,0,255)
fontSize=.2
fontThick=1

lowerLimit=0
upperLimit=468

def setLower(value):
    global lowerLimit
    lowerLimit=value
def setUpper(value):
    global upperLimit
    upperLimit=value

cv2.namedWindow('Trackbars')
cv2.moveWindow('Trackbars',width+50,0)
cv2.resizeWindow('Trackbars',400,150)

cv2.createTrackbar('lowerLimit','Trackbars',0,468,setLower)
cv2.createTrackbar('upperLimit','Trackbars',468,468,setUpper)

while True:
    ignore,  frame = cam.read()
    cv2.flip(frame,1)
    handsLM,handsType=findHands.Marks(frame)
    faceLoc=findFace.Marks(frame)
    poseLM=findPose.Marks(frame)
    facesMeshLM=findMesh.Marks(frame)
    if poseLM != []:
        for ind in [13,14,15,16]:
            cv2.circle(frame,poseLM[ind],20,(0,255,0),-1)
    for face in faceLoc:
        cv2.rectangle(frame,face[0],face[1],(255,0,0),3)
    for hand,handType in zip(handsLM,handsType):
        if handType=='Right':
            lbl='Right'
        if handType=='Left':
            lbl='Left'
        cv2.putText(frame,lbl,hand[8],font,2,fontColor,2)
    for faceMeshLM in facesMeshLM:
        cnt=0
        for lm in faceMeshLM:
            if cnt>=lowerLimit and cnt<=upperLimit:
                cv2.putText(frame,str(cnt),lm,font,fontSize,fontColor,fontThick)
            cnt+=1
    cv2.imshow('my WEBcam', frame)
    cv2.moveWindow('my WEBcam',0,0)
    if cv2.waitKey(1) & 0xff ==ord('q'):
        break
cam.release()