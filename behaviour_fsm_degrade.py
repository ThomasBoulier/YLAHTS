import sys
import fsm
import side
from MissionPlanner import *



sys.path.append(r"c:\Python27\Lib\site-packages")
sys.path.append(r"c:\Python27\Lib")
# Manque des imports ?

# global variables
f = fsm.fsm()   # defines finite state machine

global coordo
coordo = side.LoadWP("C:/Users/Thomas/Desktop/EnstaB/Python/YLAHTS-master/waysPoints.txt")

# FSM functions


def init():
    print "init"
    nextEvent = "init faite"
    return nextEvent


def decollage():
    print "decollage"
    Script.ChangeMode("TAKEOFF", coordo[0].pop(), coordo[1].pop(), coordo[2].pop() )
    nextEvent = "decollage fait"
    return nextEvent


def exploration():
    print "turn until detect"
    nextEvent = "RAS"
    while nextEvent != "RAS":
        if Script.getParam("battery_remaining") < 0.15:
            nextEvent = "atterrissage d'urgence"
        elif Script.getParam("battery_remaining") < 0.30:
            nextEvent = "retour point de depart"
        elif coordo:
            Script.ChangeMode("WAYPOINT", coordo[0].pop(), coordo[1].pop(), coordo[2].pop())
            nextEvent = "RAS"
        else:
            print "fin d'exploration"
            nextEvent = "retour point de depart"
    return nextEvent


def objetDetecte():
    print "objet detecte"
    Script.ChangeMode("LOITER")
    inTheLoop = True
    while inTheLoop:
        ask = input("Confirmez s'il y a un nid devant le drone\n y/n \n")
        if ask=="y":
            inTheLoop = False
            nextEvent = "confirmation manuelle"
        if ask=="n":
            inTheLoop = False
            nextEvent = "infirmation manuelle"
    return nextEvent


def destruction():
    print "BOOOM"
    nextEvent = "retour point de depart"
    return nextEvent


def rtl():
    print "go back home"
    Script.ChangeMode('RTL')
    nextEvent = "arrivee point de depart"
    return nextEvent


def atterrissage():
    print "landing"
    Script.ChangeMode('LAND')
    nextEvent = "fin de mission"
    return nextEvent


def finMission():
    print "Mission achevee"
    return "fin"

# Main 
if __name__== "__main__":

    # init FSM
    f.add_state ("init")
    f.add_state ("decollage")
    f.add_state ("exploration")
    f.add_state ("objet detecte")
    f.add_state ("destruction de nid")
    f.add_state ("rtl")
    f.add_state ("atterrissage")

    f.add_event ("init faite")
    f.add_event ("decollage fait")
    f.add_event ("zone de patrouille atteinte")
    f.add_event ("atterissage d'urgence")
    f.add_event ("retour point de depart")
    f.add_event ("objet detecte")
    f.add_event ("confirmation manuelle")
    f.add_event ("infirmation manuelle")
    f.add_event ("retour a l'exploration")
    f.add_event ("attaque du nid")
    f.add_event ("decollage fait")
    f.add_event ("nid detruit")
    f.add_event ("arrivee au point de depart")
    f.add_event ("fin de mission")

    f.add_transition ("init","decollage","init faite",decollage)
    f.add_transition ("decollage","exploration","decollage fait",exploration)
    f.add_transition ("exploration","objet detecte","objet detecte",objetDetecte)
    f.add_transition ("objet detecte","exploration","infirmation manuelle",exploration)
    f.add_transition ("exploration","rtl","retour point de depart",rtl)
    f.add_transition ("exploration","atterrissage","atterrissage d'urgence",atterrissage)
    f.add_transition ("objet detecte","destruction de nid","confirmation manuelle",destruction)
    f.add_transition ("destruction de nid","rtl","nid detruit",rtl)
    f.add_transition ("rtl","atterrissage","arrivee au point de depart",atterrissage)
    f.add_transition ("atterrissage","fin de mission","fin de mission",finMission)

    # FSM starting state and event 
    f.set_state ("init")
    f.set_event ("init faite")

    # run FSM
    # fonctions d'init a appeler ici.

    while (f.curState != "fin de mission"):   # wait for last state to occur
        funct = f.run ()
        newEvent = funct()
        print "New Event : ",newEvent
        f.set_event(newEvent)

    # fonctions d'arret a appeler la
