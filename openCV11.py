import cv2
print(cv2.__version__)
evt=0
evt1=0
evt2=0
def mouseClick(event,xPos,yPos,flags,params):
    global evt
    global pnt
    global pnt1
    global evt1
    global upperLeft
    global lowerRight
    global column
    global row
    global row1
    global column1
    if event==cv2.EVENT_LBUTTONDOWN:
        print('Mouse Event was: ', event)
        print('at position',xPos,yPos)
        evt=event
        evt1=event
        column=xPos
        row=yPos
        upperLeft=(xPos,yPos)
    if event==cv2.EVENT_LBUTTONUP:
        print('Mouse Event was: ', event)
        print('at position',xPos,yPos)
        lowerRight=(xPos,yPos)
        column1=xPos
        row1=yPos
        evt1=event
    if event==cv2.EVENT_RBUTTONUP:
        print('Right Button Up', event)
        pnt=(xPos,yPos)
        evt=event
recColor=(0,255,0)
myThick=1
width=640
height=360
cam=cv2.VideoCapture(0,cv2.CAP_DSHOW)
cam.set(cv2.CAP_PROP_FRAME_WIDTH, width)
cam.set(cv2.CAP_PROP_FRAME_HEIGHT,height)
cam.set(cv2.CAP_PROP_FPS, 30)
cam.set(cv2.CAP_PROP_FOURCC,cv2.VideoWriter_fourcc(*'MJPG'))
cv2.namedWindow('my Webcam')
cv2.setMouseCallback('my Webcam',mouseClick)
while True:
    ignore,  frame = cam.read()
    if evt==1 and  evt1==4 and row<row1 and column<column1:
            cv2.rectangle(frame,upperLeft,lowerRight,recColor,myThick)
            frame1=frame[row:row1,column:column1]  
            cv2.imshow('my webcam',frame1)
            cv2.moveWindow('my webcam',650,0)
    cv2.imshow('my Webcam', frame)
    cv2.moveWindow('my Webcam',0,0)
    if cv2.waitKey(1) & 0xff ==ord('q'):
        break
cam.release()