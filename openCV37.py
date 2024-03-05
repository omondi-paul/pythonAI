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
findFace=mp.solutions.face_detection.FaceDetection()
drawFace=mp.solutions.drawing_utils
while True:
    ignore, frame= cam.read()
    frameRGB=cv2.cvtColor(frame,cv2.COLOR_BGR2RGB)
    results=findFace.process(frameRGB)
    #print(results.detections)
    if results.detections != None:
        for face in results.detections:
            drawFace.draw_detection(frame,face)
            bBox=face.location_data.relative_bounding_box
            topLeft=((int(bBox.xmin*width),int(bBox.ymin*height)))
            bottomRight=((int((bBox.xmin+bBox.width)*width),int((bBox.ymin+bBox.height)*height)))
            cv2.rectangle(frame,topLeft,bottomRight,(255,0,0),3)                        
    cv2.imshow('my Webcam',frame)
    cv2.moveWindow('my Webcam',0,0)
    if cv2.waitKey(1) & 0xFF==ord('q'):
        break
cam.release()