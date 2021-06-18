#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Dec  4 20:52:55 2019

@author: kinchan
"""

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""

1. Alpha affect alot
2. Cant print histogram image
3. Output csv

"""

from PIL import Image 
from PIL import ImageOps
import numpy as np
import RPi.GPIO as GPIO
import picamera
import time

with picamera.PiCamera() as camera:
    camera.resolution = (720,480)
    camera.sensor_mode = 1
    camera.iso = 800
count=1
TRIG_pin = 23
ECHO_pin = 24
GPIO.setmode(GPIO.BCM)
GPIO.setup(TRIG_pin,GPIO.OUT)
GPIO.setup(ECHO_pin, GPIO.IN)

GPIO.setup(2, GPIO.OUT)
GPIO.setup(3, GPIO.OUT)
PWM = GPIO.PWM(3, 40)
imageSize = (32, 32)
imageArea = float(imageSize[0] * imageSize[1])
chopArea = (4, 4 , 4,4)
resultArray = []
fruitName = []

def ImageResize(image):
    resizedImage = image.resize(imageSize)
    croppedImage = ImageOps.crop(resizedImage, chopArea)
    #croppedImage.show()
    return resizedImage

def ColorQuantization(RGB_Image):
    i = 1
    list1 = []
    indexedImage = []
    imageData = list(RGB_Image.getdata())
    imageDataFlatten = [x for sets in imageData for x in sets]
    imageDataBinary = [str(bin(x))[2:].zfill(8) for x in imageDataFlatten]
    
    for x in imageDataBinary:
        if int(i) % 3 != 0:
            list1.append(x[:3])
            i += 1
        else:
            list1.append(x[:2])
            i += 1
    
    n=0
    m=0
    for x in range(len(imageData)):
        indexedImage.append(list1[m])
        m += 1
        indexedImage[n] += list1[m]
        m += 1
        indexedImage[n] += list1[m]
        m += 1
        n += 1
    return indexedImage

def GetHistogram(IndexedImage):
    histogram = np.zeros( (256), dtype=np.int )
    histogram_buffer = np.zeros( (256), dtype=np.float )
    imageDataDecimal = []
    for x in IndexedImage:     
        imageDataDecimal.append(int(x, 2))
    for x in imageDataDecimal:
        histogram[x] += 1
    for x in range(0, 256, 1):
         histogram_buffer[x] = histogram[x]/imageArea
    return histogram_buffer
    
def CheckSimlarity(ResultArray,name):
    i=0
    answerArray = []
    for x in range(len(ResultArray)-1):
        A = ResultArray[-1]     
        answer = sum(abs(A - ResultArray[i]))
        print('The simlarity between the %s and %s is:\t %f' % (name[-1],name[x],answer))
        i += 1
        answerArray.append(answer)
    minimum = answerArray.index(min(answerArray))
    print('the test object is '+ name[minimum])
    return 

def Process(filepath):
    image = Image.open(filepath)
    CroppedImage = ImageResize(image)
    CQimage = ColorQuantization(CroppedImage)
    imageHistogram = GetHistogram(CQimage)
    return imageHistogram

def Training():
    imGreen1= Process("/home/pi/Desktop/GreenFruit/image1.jpg")
    fruitName.append('GreenFruit')
    resultArray.append(imGreen1)
    imGreen2= Process("/home/pi/Desktop/GreenFruit/image2.jpg")
    fruitName.append('GreenFruit')
    resultArray.append(imGreen2)
    imGreen3= Process("/home/pi/Desktop/GreenFruit/image3.jpg")
    fruitName.append('GreenFruit')
    resultArray.append(imGreen3)   
    imGreen4= Process("/home/pi/Desktop/GreenFruit/image4.jpg")
    fruitName.append('GreenFruit')
    resultArray.append(imGreen4)    
    imGreen5= Process("/home/pi/Desktop/GreenFruit/image5.jpg")
    fruitName.append('GreenFruit')
    resultArray.append(imGreen5)
    imGreen6= Process("/home/pi/Desktop/GreenFruit/image6.jpg")
    fruitName.append('GreenFruit')
    resultArray.append(imGreen6)
    imGreen7= Process("/home/pi/Desktop/GreenFruit/image7.jpg")
    fruitName.append('GreenFruit')
    resultArray.append(imGreen7)
    imGreen8= Process("/home/pi/Desktop/GreenFruit/image8.jpg")
    fruitName.append('GreenFruit')
    resultArray.append(imGreen8)
    
    imPurple1 = Process("/home/pi/Desktop/PurpleFruit/image1.jpg")
    fruitName.append('PurpleFruit')
    resultArray.append(imPurple1)
    imPurple2 = Process("/home/pi/Desktop/PurpleFruit/image2.jpg")
    fruitName.append('PurpleFruit')
    resultArray.append(imPurple2)
    imPurple3 = Process("/home/pi/Desktop/PurpleFruit/image3.jpg")
    fruitName.append('PurpleFruit')
    resultArray.append(imPurple3)
    imPurple4 = Process("/home/pi/Desktop/PurpleFruit/image4.jpg")
    fruitName.append('PurpleFruit')
    resultArray.append(imPurple4)
    imPurple5 = Process("/home/pi/Desktop/PurpleFruit/image5.jpg")
    fruitName.append('PurpleFruit')
    resultArray.append(imPurple5)
    imPurple6 = Process("/home/pi/Desktop/PurpleFruit/image6.jpg")
    fruitName.append('PurpleFruit')
    resultArray.append(imPurple6)
    imPurple7 = Process("/home/pi/Desktop/PurpleFruit/image7.jpg")
    fruitName.append('PurpleFruit')
    resultArray.append(imPurple7)
    imPurple8 = Process("/home/pi/Desktop/PurpleFruit/image8.jpg")
    fruitName.append('PurpleFruit')
    resultArray.append(imPurple8)
    imPurple9 = Process("/home/pi/Desktop/PurpleFruit/image9.jpg")
    fruitName.append('PurpleFruit')
    resultArray.append(imPurple9)
    imPurple10 = Process("/home/pi/Desktop/PurpleFruit/image10.jpg")
    fruitName.append('PurpleFruit')
    resultArray.append(imPurple10)

    imRed1 = Process("/home/pi/Desktop/RedFruit/image1.jpg")
    fruitName.append('RedFruit')
    resultArray.append(imRed1)
    imRed2 = Process("/home/pi/Desktop/RedFruit/image2.jpg")
    fruitName.append('RedFruit')
    resultArray.append(imRed2)
    imRed3 = Process("/home/pi/Desktop/RedFruit/image3.jpg")
    fruitName.append('RedFruit')
    resultArray.append(imRed3)
    imRed4 = Process("/home/pi/Desktop/RedFruit/image4.jpg")
    fruitName.append('RedFruit')
    resultArray.append(imRed4)
    imRed5 = Process("/home/pi/Desktop/RedFruit/image5.jpg")
    fruitName.append('RedFruit')
    resultArray.append(imRed5)
    imRed6 = Process("/home/pi/Desktop/RedFruit/image6.jpg")
    fruitName.append('RedFruit')
    resultArray.append(imRed6)
    imRed7 = Process("/home/pi/Desktop/RedFruit/image7.jpg")
    fruitName.append('RedFruit')
    resultArray.append(imRed7)
    imRed8 = Process("/home/pi/Desktop/RedFruit/image8.jpg")
    fruitName.append('RedFruit')
    resultArray.append(imRed8)
    imRed9 = Process("/home/pi/Desktop/RedFruit/image9.jpg")
    fruitName.append('RedFruit')
    resultArray.append(imRed9)

    imYellow1 = Process("/home/pi/Desktop/YellowFruit/image1.jpg")
    fruitName.append('YellowFruit')
    resultArray.append(imYellow1)
    imYellow2 = Process("/home/pi/Desktop/YellowFruit/image2.jpg")
    fruitName.append('YellowFruit')
    resultArray.append(imYellow2)
    imYellow3 = Process("/home/pi/Desktop/YellowFruit/image5.jpg")
    fruitName.append('YellowFruit')
    resultArray.append(imYellow3)
    imYellow4 = Process("/home/pi/Desktop/YellowFruit/image8.jpg")
    fruitName.append('YellowFruit')
    resultArray.append(imYellow4)
    imYellow5 = Process("/home/pi/Desktop/YellowFruit/image3.jpg")
    fruitName.append('YellowFruit')
    resultArray.append(imYellow5)
    imYellow6 = Process("/home/pi/Desktop/YellowFruit/image6.jpg")
    fruitName.append('YellowFruit')
    resultArray.append(imYellow6)
    imYellow7 = Process("/home/pi/Desktop/YellowFruit/image4.jpg")
    fruitName.append('YellowFruit')
    resultArray.append(imYellow7)
    imYellow8 = Process("/home/pi/Desktop/YellowFruit/7.jpg")
    fruitName.append('YellowFruit')
    resultArray.append(imYellow8)



    imTest = Process("/home/pi/Desktop/red1.jpg")
    fruitName.append('Test subject')
    resultArray.append(imTest)

def Ultrasonic_Sensor():
    GPIO.output(TRIG_pin, False)
    time.sleep(0.25)
    GPIO.output(TRIG_pin, True)
    time.sleep(0.00001)
    GPIO.output(TRIG_pin,False)

    while GPIO.input(ECHO_pin)==0:
        pulse_start = time.time()
          
    while GPIO.input(ECHO_pin)==1:
        pulse_end = time.time()
    pulse_duration = pulse_end - pulse_start
    distance = pulse_duration * 17150
    distance = round(distance, 2)
    print ("Distance:", distance, "cm")
    return distance
    
if __name__ == '__main__':
    #Training
    try:
        print('按下 Ctrl-C 可停止程式')
        time.sleep(2)
        Training()
        GPIO.output(2, 0)

        PWM.start(40)
        while True:
            Ultrasonic_Sensor()
            if Ultrasonic_Sensor() < 10. :
                #time.sleep(0.5)
                print("About to take a picture.")
                with picamera.PiCamera() as camera:
                    camera.resolution = (720,480)
                    camera.sensor_mode = 1
                    camera.iso = 800
                    #time.sleep(2)
                    camera.capture("/home/pi/Desktop/image%d.jpg" %count)

                print("Picture taken.")
                resultArray[-1] = Process("/home/pi/Desktop/image%d.jpg" %count)
                
                CheckSimlarity(resultArray, fruitName)
                count+=1
                time.sleep(3)   
    except KeyboardInterrupt:
        print('關閉程式')
    finally:
        PWM.stop()
        GPIO.cleanup()
