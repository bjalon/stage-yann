import time

# Déclaration d'une fonction
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
    if valeurSaisie == "25":
        print("toto")
        print("toto2")
    verifierResultatAddition()
    for i in range(10):
        time.sleep(0.5)
        print("Bonjour " + str(i))


