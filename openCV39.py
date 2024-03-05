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

faceMesh=mp.solutions.face_mesh.FaceMesh(False,3,.5,.5)
mpDraw=mp.solutions.drawing_utils

drawSpecCircle=mpDraw.DrawingSpec(thickness=0,circle_radius=0,color=(255,0,0))
drawSpecLine=mpDraw.DrawingSpec(thickness=3,circle_radius=2,color=(0,0,255))

font=cv2.FONT_HERSHEY_SIMPLEX
fontSize=.2
fontColor=(0,255,255)
fontThick=1

while True:
    ignore, frame= cam.read()
    frameRGB=cv2.cvtColor(frame,cv2.COLOR_BGR2RGB)
    results=faceMesh.process(frameRGB)
    #print(results.multi_face_landmarks)
    if results.multi_face_landmarks != None:
        for faceLandMarks in results.multi_face_landmarks:
            mpDraw.draw_landmarks(frame,faceLandMarks,mp.solutions.face_mesh.FACE_CONNECTIONS,drawSpecCircle,drawSpecLine)
            indx=0
            for lm in faceLandMarks.landmark:
                cv2.putText(frame,str(indx),(int(lm.x*width),int(lm.y*height)),font,fontSize,fontColor,fontThick)
                indx+=1
    cv2.imshow('my Webcam',frame)
    cv2.moveWindow('my Webcam',0,0)
    if cv2.waitKey(1) & 0xFF==ord('q'):
        break
cam.release()