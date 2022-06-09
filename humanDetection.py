def detectHuman():
    import cv2
    import imutils
    from detectFace import detectFace
       
    # Initializing the HOG person 
    hog = cv2.HOGDescriptor() 
    hog.setSVMDetector(cv2.HOGDescriptor_getDefaultPeopleDetector())
       
    # Reading the Image 
    image = cv2.imread('img.jpg') 
       
    # Resizing the Image 
    image = imutils.resize(image, 
                           width=min(600, image.shape[1])) 
       
    # Detecting all humans 
    (humans, _) = hog.detectMultiScale(image,  
                                        winStride=(5, 5), 
                                        padding=(3, 3), 
                                        scale=1.21)
    # getting no. of human detected
    print('Human Detected : ', len(humans))

    persons = len(humans)

    if len(humans)==0:
        faces = detectFace()
        print("Found "+str(faces)+" face(s)")
        persons+=faces
       
    # Drawing the rectangle regions
    # for (x, y, w, h) in humans: 
    #     cv2.rectangle(image, (x, y),  
    #                   (x + w, y + h),  
    #                   (0, 0, 255), 2) 
      
    # Displaying the output Image 
    # cv2.imshow("Image", image) 
    # cv2.waitKey(0) 
    #    
    # cv2.destroyAllWindows() 
    return persons