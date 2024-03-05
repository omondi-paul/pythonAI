import cv2
print(cv2.__version__)
def myCallBack1(val):
    global xPos
    xPos=val
def myCallBack2(val):
    global yPos
    yPos=val
def myCallBack3(val):
    global width
    width=val
    height=int(width*9/16)
    cam.set(cv2.CAP_PROP_FRAME_WIDTH, width)
    cam.set(cv2.CAP_PROP_FRAME_HEIGHT,height)
    
xPos=0
yPos=0
width=640
height=360
cam= cv2.VideoCapture(0,cv2.CAP_DSHOW)
cam.set(cv2.CAP_PROP_FRAME_WIDTH, width)
cam.set(cv2.CAP_PROP_FRAME_HEIGHT,height)
cam.set(cv2.CAP_PROP_FPS, 30)
cam.set(cv2.CAP_PROP_FOURCC,cv2.VideoWriter_fourcc(*'MJPG'))
cv2.namedWindow('my TrackBars')
cv2.moveWindow('my TrackBars',width,0,)
cv2.resizeWindow('my TrackBars',400,150)
cv2.createTrackbar('xPos','my TrackBars',0,2000,myCallBack1)
cv2.createTrackbar('yPos','my TrackBars',0,1000,myCallBack2)
cv2.createTrackbar('width','my TrackBars',width,1280,myCallBack3)

while True:
    ignore, frame= cam.read()
    gray=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    cv2.imshow('my WEBcam',frame)
    cv2.moveWindow('my WEBcam',xPos,yPos)
    
    if cv2.waitKey(1) & 0xFF==ord('q'):
        break
cam.release()