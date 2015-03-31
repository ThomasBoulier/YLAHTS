import fsm
import sys
import side
sys.path.append(r"c:\Python34\Lib\site-packages")
sys.path.append(r"c:\Python34\Lib")
import serial, os, threading
# Manque des imports ?

# global variables
f = fsm.fsm()   # defines finite state machine


# FSM functions 
    
def init():
    print "init"
    nextEvent = "init faite"
    return nextEvent
    
def decollage():
    print "decollage"
    #corps de la fonction
    nextEvent = "decollage fait"
    return nextEvent 

def exploration():
    print "turn until detect"
    nextEvent = "RAS"
    while nextEvent =! "RAS"
        if (Script.getParam("battery_remaining") < 0.15) : 
            nextEvent = "atterrissage d'urgence" 
        elif (side.IsThereAnObject()) :
            nextEvent = "objet detecte"
        elif (Script.getParam("battery_remaining") < 0.30):
            nextEvent = "retour point de depart"
        else
            nextEvent = "RAS"
    return nextEvent
    
def objetDetecte():
    print "do something ..."
    Script.ChangeMode(LOITER)
    if ():
        nextEvent = "confirmation manuelle"
    else ():
        nextEvent = "infirmation manuelle"
    return nextEvent

def destruction():
    print "BOOOM"
    nextEvent = "retour point de depart"
    return nextEvent
    
def rtl():
    Script.ChangeMode('RTL')
    print "go back home"
    nextEvent = "arrivee point de depart"
    return nextEvent    
    
def atterissage():
    Script.ChangeMode('LAND')
    print "landing"
    nextEvent = "fin de mission"
    return nextEvent
    
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

    f.add_transition ("init","decollage","init faite",decollage);
    f.add_transition ("decollage","exploration","decollage fait",exploration);
    f.add_transition ("exploration","objet detecte","objet detecte",objetDetecte);
    f.add_transition ("objet detecte","exploration","infirmation manuelle",explore);
    f.add_transition ("exploration","rtl","retour point de depart",rtl);
    f.add_transition ("exploration","atterrissage","atterrissage d'urgence",atterrissage);
    f.add_transition ("objet detecte","destruction de nid","confirmation manuelle",destruction);
    f.add_transition ("destruction de nid","rtl","nid detruit",rtl);
    f.add_transition ("rtl","atterrissage","arrivee au point de depart",atterrissage);
    f.add_transition ("atterrissage","fin de mission","fin de mission",finMission);
    
    # FSM starting state and event 
    f.set_state ("init")
    f.set_event ("init faite")


    # run FSM
    #fonctions d'init à appeler ici.

    while (f.curState != "fin de mission"):   # wait for last state to occur
        funct = f.run ()
        newEvent = funct()
        print "New Event : ",newEvent
        f.set_event(newEvent)

    #fonctions d'arret à appeler là
