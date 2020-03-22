# elendsindex


## Was ist das hier?
Wir haben in der WG das Spiel [Verdammt nochmal](https://www.amazon.de/dp/B06XR31LLF/ref=cm_sw_r_tw_dp_U_x_P.NDEbZRQSHDM) gespielt.

Im Prinzip geht es darum dass man eine Reihe von Karten mit "schlimmen Sachen" hat die auf einer Skala von 0 bis 100
einen Elendsindex haben wie schlimm sie sind.
Dann bekommt man eine Karte vorgelesen und muss schätzen in welche Lücke die Karte gehört. Dabei ist uns aufgefallen
dass viele Karten unserer Meinung nach einen vollkommen falschen Wert haben und wir sie deutlich anders einordnen
würden.

Daher entstand nach ein paar Bier die Idee für diese Webseite um ein neues Ranking zu erstellen und zu schauen wie
stark unsere Einschätzung von der, der Spieleredaktion abweicht. Also in 2 Stunden kurz ein bisschen Python und Flask
zusammengedängelt und ab gehts :D


## Setup
Ihr braucht Python3 und pipenv
```
git clone https://github.com/fleaz/elendsindex.git
cd elendsindex
pipenv install
pipenv shell
flask db upgrade
FLASK_APP=run.py FLASK_ENV=development flask run
```
