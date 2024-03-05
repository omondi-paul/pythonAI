import cv2
print(cv2.__version__)
def myCallBack1(val):
    global xPos
    print('xPos:',val)
    xPos=val
def myCallBack2(val):
    global yPos
    print('yPos:',val)
    yPos=val
def myCallBack3(val):
    global myRad
    print('myRad:',val)
    myRad=val
def myCallBack4(val):
    global myThick
    print('thickness:',val)
    myThick=val
myThick=1
width=620
height=360
myRad=25
xPos=int(width/2)
yPos=int(height/2)
cam=cv2.VideoCapture(0,cv2.CAP_DSHOW)
cam.set(cv2.CAP_PROP_FRAME_WIDTH, width)
cam.set(cv2.CAP_PROP_FRAME_HEIGHT,height)
cam.set(cv2.CAP_PROP_FPS, 30)
cam.set(cv2.CAP_PROP_FOURCC,cv2.VideoWriter_fourcc(*'MJPG'))
cv2.namedWindow('my Trackbars')
cv2.resizeWindow('my Trackbars',400,200)
cv2.moveWindow('my Trackbars',width,0)
cv2.createTrackbar('xPos','my Trackbars',xPos,1920,myCallBack1)
cv2.createTrackbar('yPos','my Trackbars',yPos,1080,myCallBack2)
cv2.createTrackbar('radius','my Trackbars',myRad,int(height/2),myCallBack3)
cv2.createTrackbar('thick','my Trackbars',myThick,7,myCallBack4)

while True:
    ignore,  frame = cam.read()
    if myThick==0:
        myThick=(-1)
    cv2.circle(frame,(xPos,yPos),myRad,(255,0,0),myThick)
    cv2.imshow('my WEBcam', frame)
    cv2.moveWindow('my WEBcam',0,0)
    if cv2.waitKey(1) & 0xff ==ord('q'):
        break
cam.release()