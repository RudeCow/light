from time import sleep
from picamera import PiCamera

camera = PiCamera()
camera.resolution = (1024, 768)
camera.start_preview()
# Camera warm-up time
sleep(300)
camera.capture('/home/gr103/Desktop/Scripts/test.jpg')