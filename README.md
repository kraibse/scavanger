# Scavanger - Space Miner

Das Spiel Scavanger ist ein rundenbasiertes Abbauspiel im Weltraum.
Ein Raumschiff bewegt sich durch ein Feld von Planeten und Asteroiden und baut Ressourcen ab, um sich weiterzuentwickeln und weitere Regionen zu erkunden.

**Steuerung**

- Beschleunigung mit der Leertaste
- Richtung angeben durch den Mauszeiger


**Gameloop**
- Man startet als ein einfaches Raumschiff ohne Upgrades
- Es werden Ressourcen durch den Abbau von Planeten aufgenommen
- Im Shop werden Upgrades gekauft, um die Überlebenschancen in den Regionen zu erhöhen
- Alle Regionen erkunden und das Spiel gewinnen

**Wie startet man das Spiel?**

- Voraussetzungen installieren `python -m pip install -r requirements.txt`
- Startdatei ausführen `python start_scavanger.py`


## Tag 1 - 2024-11-22

Am Ende des Tages sollte ein Grundgerüst stehen, das ein grundlegendes Pygame Fester darstellt. Man kann es schließen und erste Events erkennen.

Erste Vorbereitungen für den Spieler und die Sprites und Animationen werden umgesetzt.


**Was wurde gemacht?**

Leon Horn
- Spielerklasse mit grundlegendem Controller
- Vorbereitungen der Sprites und Animationen

Marcus Schmidt
- Datei zum Starten des Spiels
- Scene Manager
- Erstellung des Level Grundgerüsts

Lucian Kath
- Basisklasse der abbaubaren Spielobjekten
- Vorbereitung der Planetenklassen


**Welche Themen bestehen noch?**

Das Spiel ist schwarz und zeigt keine Spielobjekte an. Die Animationen funktionieren nicht.


## Tag 2 - 2024-11-26

Am Ende des Tages soll sich der Spieler auf der Karte bewegen können.
Ertse UI Elemente werden eingebracht und ohne Datenzugriff auf dem Bildschirm dargestellt.

**Was wurde gemacht?**

Leon Horn
- Anpassung und Fix der im Spielerskript entstandenen Fehler
- Anpassungen an den Animationen

Marcus Schmidt
- TextBoxen, Buttons
- Level UI
- Bugfixing, Implementierung der UI

Lucian Kath (krank)


**Welche Themen bestehen noch?**

Der Spieler steht alleine in einem leeren Spielfeld. Die UI-Elemente sind noch nicht dynamisch und mit Werten bestückt.


## Tag 3 - 2024-11-27

**Was wurde gemacht?**

Leon Horn

- Planeten abbauen und Ressourcen spawnen
    - Spielerradius
    - Abbauen des Planetens
    - Despawn des Planetens
- Planetenradar

Marcus Schmidt

- Implementierung des Shopsystems
- Levelwechsel
- Spielerupgrades
- Health Bar überarbeiten

Lucian Kath (krank)


**Welche Themen bestehen noch?**

Die gekauften Spielerupgrades reduzieren nicht die Währung.
Neben den Planeten gibt es keinen Grund die Upgrades zu verwenden, Gegner und Asteroiden stehen aus.
Die Planetenkollision war inkorrekt und nicht mit der Planetensprite stimmig.


## Tag 4 - 2024-11-29

Es werden die letzten Anpassungen gemacht und Tests durchgeführt.
Gegner werden eingebunden und das UI und Spielerlebnis wird finalisiert.

Asteroiden werden eingeführt und Leveltransitionen werden ermöglicht.


**Was wurde gemacht?**

Leon Horn
- Implementierung der Asteroiden
- Kollisionen mit dem Spieler ziehen Leben ab
- Persistente Spielereigenschaften
- Friere den Bildschirm ein, wenn der Shop aktiv ist

Marcus Schmidt
- Levelübergänge
- Game Over Bildschirm
- Anpassungen am Main Menu
- Anpassungen am Game-UI

Lucian Kath
- ändern der enemyBase klasse zu einer einzigen enemyTurrent
- implementieren von Geschützen die bei einer bestimmten Entfernung zum Spieler auf diesen feuern
- testing und feedback