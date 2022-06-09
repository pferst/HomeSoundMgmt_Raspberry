def detectFace():

    import cv2

    image = cv2.imread('img.jpg') 

    #Load a cascade file for detecting faces
    face_cascade = cv2.CascadeClassifier('haarcascade.xml')

    #Convert to grayscale
    gray = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)

    #Look for faces in the image using the loaded cascade file
    faces = face_cascade.detectMultiScale(gray, 1.5, 5)

#     print("Found "+str(len(faces))+" face(s)")
    return len(faces)
    #Draw a rectangle around every found face
#     for (x,y,w,h) in faces:
#         cv2.rectangle(image,(x,y),(x+w,y+h),(255,255,0),2)
# 
#     #Save the result image
#     cv2.imwrite('result.jpg',image)
