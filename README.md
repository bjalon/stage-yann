# Stage de Yann

* Implémentation d'un site de jeu de calcul

## Installation



```
sudo apt-get install build-essential libcap-dev
```

## Execution

### Application Web

```
cd web
python -m http.server
```

Il suffit ensuite de se connecter depuis un navigateur à l'adresse [http://localhost:8000/](http:localhost:8000/)

### Application python

* Brancher la camera au Raspberry pi
* Brancher le capteur de mouvement sur les GPIO suivants
  * ECHO: 24
  * TRIG : 23
* Il faut installer pip et pipenv
* Puis executer les commandes suivantes

```
cd stage-yann
pipenv install
pipenv shell
python main.py
```

Le proj


