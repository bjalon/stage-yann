import os
import time
import RPi.GPIO as GPIO
import picamera
import cv2


GPIO.setmode(GPIO.BCM)

# Déclaration d'une fonction hé
# KOLTIN
# fun nomFonction(): Unit {}
# JAVA
#   void nomFonction() {}
# JS
#  function nomFonction {}
# FLUTTER
# void nomFonction() { }

# Déclaration de variable et création de la zone mémoire associé
valeurSaisie = "25"
# JS : var valeurSaisie = "25"
# Java : String valeurSaisie = "25"
# Koltin : valeurSaisie = "25"
GPIO_TRIGGER = 23
GPIO_ECHO = 24
captureIndex = 0

GPIO.setwarnings(False)
GPIO.setup(GPIO_TRIGGER, GPIO.OUT)
GPIO.setup(GPIO_ECHO, GPIO.IN)
current_distance = -1
previous_distance = -1



#home = os.path.expanduser("~")
home="/home/yann"

#This is to pull the information about what each object is called
classNames = []
classFile = f"{home}/tools/Object_Detection_Files/coco.names"
with open(classFile,"rt") as f:
    classNames = f.read().rstrip("\n").split("\n")

#This is to pull the information about what each object should look like
configPath = f"{home}/tools/Object_Detection_Files/ssd_mobilenet_v3_large_coco_2020_01_14.pbtxt"
weightsPath = f"{home}/tools/Object_Detection_Files/frozen_inference_graph.pb"

#This is some set up values to get good results
net = cv2.dnn_DetectionModel(weightsPath,configPath)
net.setInputSize(320,320)
net.setInputScale(1.0/ 127.5)
net.setInputMean((127.5, 127.5, 127.5))
net.setInputSwapRB(True)

#This is to set up what the drawn box size/colour is and the font/size/colour of the name tag and confidence label
def getObjects(img, thres, nms, draw=True, objects=[]):
    classIds, confs, bbox = net.detect(img,confThreshold=thres,nmsThreshold=nms)
#Below has been commented out, if you want to print each sighting of an object to the console you can uncomment below
#print(classIds,bbox)
    if len(objects) == 0: objects = classNames
    objectInfo =[]
    if len(classIds) != 0:
        for classId, confidence,box in zip(classIds.flatten(),confs.flatten(),bbox):
            className = classNames[classId - 1]
            if className in objects:
                objectInfo.append([box,className])
                if (draw):
                    cv2.rectangle(img,box,color=(0,255,0),thickness=2)
                    cv2.putText(img,classNames[classId-1].upper(),(box[0]+10,box[1]+30),
                    cv2.FONT_HERSHEY_COMPLEX,1,(0,255,0),2)
                    cv2.putText(img,str(round(confidence*100,2)),(box[0]+200,box[1]+30),
                    cv2.FONT_HERSHEY_COMPLEX,1,(0,255,0),2)

    return img,objectInfo


    
    
def distance():
    
    # set Trigger to HIGH
    GPIO.output(GPIO_TRIGGER, True)

    # set Trigger after 0.01ms to LOW
    time.sleep(0.00001)
    GPIO.output(GPIO_TRIGGER, False)

    StartTime = time.time()
    StopTime = time.time()

    # save StartTime
    while GPIO.input(GPIO_ECHO) == 0:
        StartTime = time.time()

    # save time of arrival
    while GPIO.input(GPIO_ECHO) == 1:
        StopTime = time.time()

    # time difference between start and arrival
    TimeElapsed = StopTime - StartTime
    # multiply with the sonic speed (34300 cm/s)
    # and divide by 2, because there and back
    distance = (TimeElapsed * 34300) / 2
    # print(f"Distance = {str(distance)}")

    return distance

def detectMovement():
    global current_distance
    global previous_distance
    for i in range(100):
        current_distance = distance()
        if previous_distance != -1 and current_distance - previous_distance > 100:
            return
        previous_distance = current_distance
        time.sleep(0.5)


def capturePhoto():
    global captureIndex
    
    newpath = r'/tmp/yann' 
    if not os.path.exists(newpath):
        os.makedirs(newpath)

    with picamera.PiCamera() as camera:
        captureFile = f'{newpath}/capture_{captureIndex}.jpg'
        #camera.start_preview()
        camera.capture(captureFile)
        captureIndex = captureIndex + 1
        #camera.stop_preview()
        return captureFile

if __name__ == '__main__':
    while True:
        # detectMovement()
        #print("Mouvement détecté")
        captureFile = capturePhoto()
        img = cv2.imread(captureFile)
        result, detectedObjectsInfo = getObjects(img, 0.55, 0.2)
        detectedObjectsName = [it[1] for it in detectedObjectsInfo]
        if "person" in detectedObjectsName:
            print(f"Une personne a été détectée")
        else:
            os.remove(captureFile)
        time.sleep(1)        
        
    

    
    

