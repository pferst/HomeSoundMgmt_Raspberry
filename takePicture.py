def takePicture():
    from picamera import PiCamera
    camera = PiCamera()
    #time.sleep(2)
    camera.capture("img.jpg")
    print("Captured.")
    camera.close()
