import cv2
print(cv2.__version__)
import face_recognition as FR  #import the trained model for face_recognition
font=cv2.FONT_HERSHEY_SIMPLEX  #declare a variable font 
donFace=FR.load_image_file('C:/Users/HP/Documents/PYTHON/demoImages/known/Donald Trump.jpg') #load the image of Donald Trump
faceLoc=FR.face_locations(donFace)[0]        #use face recognition to get the location of the face
donFaceEncode=FR.face_encodings(donFace)[0]  #encode the face measurements

nancyFace=FR.load_image_file('C:/Users/HP/Documents/PYTHON/demoImages/known/Nancy Pelosi.jpg') #load
faceLoc=FR.face_locations(nancyFace)[0] #locate face
nancyFaceEncode=FR.face_encodings(nancyFace)[0]  #encode

penceFace=FR.load_image_file('C:/Users/HP/Documents/PYTHON/demoImages/known/Mike Pence.jpg')  #load
faceLoc=FR.face_locations(penceFace)[0]     #locate face
penceFaceEncode=FR.face_encodings(penceFace)[0]     #encode

knownEncodings=[donFaceEncode,nancyFaceEncode,penceFaceEncode]      #create array of known faces
names=['Donald Trump','Nancy Pelosi','Mike Pence']              #create array of names of known faces


unknownFace=FR.load_image_file('C:/Users/HP/Documents/PYTHON/demoImages/unknown/u1.jpg')  #load unknown face
unknownFaceBGR=cv2.cvtColor(unknownFace,cv2.COLOR_RGB2BGR)      #convert color fro rgb to bgr
faceLocations=FR.face_locations(unknownFace)        #read the face locations
unknownEncodings=FR.face_encodings(unknownFace,faceLocations) #encode unknown face

for faceLocation,unknownEncoding in zip(faceLocations,unknownEncodings):#start for loop for unknown face
    top,right,bottom,left=faceLocation  #assign the faceLocations values into variables
    print(faceLocation)                 #print the array faceLocation
    cv2.rectangle(unknownFaceBGR,(left,top),(right,bottom),(255,0,0),3)     #draw a rectangle around the face
    name='Unknown Person'     #assign the name variable unknown persons
    matches=FR.compare_faces(knownEncodings,unknownEncoding)  #use compare_faces to find matches
    print(matches)
    if True in matches:    #start a loop for matches true
        matchIndex=matches.index(True)
        print(matchIndex)
        print(names[matchIndex])
        name=names[matchIndex]     #if they match assign the name from the known array matching the index
    cv2.putText(unknownFaceBGR,name,(left,top),font,.75,(0,0,255),2)   #name the face
cv2.imshow('My Faces',unknownFaceBGR)
cv2.waitKey(5000)
