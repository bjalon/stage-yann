import os
import time
import RPi.GPIO as GPIO
import picamera

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


if __name__ == '__main__':
    detectMovement()
    print("Mouvement détecté")
    

    
    

