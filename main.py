import time
import RPi.GPIO as GPIO

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


def verifierResultatAddition():
    print("titi")

if __name__ == '__main__':
    # Equivalent :  JS : valeurSaisie === "25"
    GPIO.setwarnings(False)
    GPIO.setmode(GPIO.BCM)
    gpioPort = 23
    
    # Je dis à la librairie que je vais écrire dans le port 23
    GPIO.setup(gpioPort, GPIO.OUT)
    
    # Je demande à librairie de mettre le courant dans le port 23 
    for i in range(10):
        GPIO.output(gpioPort, GPIO.HIGH)
        time.sleep(1)
        GPIO.output(gpioPort, GPIO.LOW)
        time.sleep(1)

    if valeurSaisie == "25":
        print("toto")
        print("toto2")
    verifierResultatAddition()
    for i in range(10):
        time.sleep(0.5)
        print("Bonjour " + str(i))


