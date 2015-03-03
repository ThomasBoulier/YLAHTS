import fsm
import sys
sys.path.append(r"c:\Python34\Lib\site-packages")
sys.path.append(r"c:\Python34\Lib")
import serial, os, threading
# Manque des imports ?

# global variables
f = fsm.fsm()   # defines finite state machine


# FSM functions 
    
def init():
    print "init"
    nextEvent = "init_done"
    return nextEvent
    
def decollage():
    print "decollage"
    #corps de la fonction
    nextEvent = "decollage_done"
    return nextEvent 

def exploration():
    print "turn until detect"
    if () : 
        nextEvent = "atterrissage d'urgence" 
    elif () :
        nextEvent = "objet detecte"
    elif ():
    return nextEvent
    
def objetDetecte():
    print "do something ..."
    if ():
        nextEvent = "confirmation manuelle"
    else ():
        nextEvent = "infirmation manuelle"
    return nextEvent

def myFunct():
    print "do something ..."
    nextEvent = "???"
    return nextEvent
    
def myFunct():
    print "do something ..."
    nextEvent = "???"
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

    f.add_transition ("state1","state2","event",myFunct);
    f.add_transition ("state1","state2","event",myFunct);
    f.add_transition ("state1","state2","event",myFunct);
    f.add_transition ("state1","state2","event",myFunct);
    f.add_transition ("state1","state2","event",myFunct);
    f.add_transition ("state1","state2","event",myFunct);
    f.add_transition ("state1","state2","event",myFunct);
    f.add_transition ("state1","state2","event",myFunct);
    f.add_transition ("state1","state2","event",myFunct);
    f.add_transition ("state1","state2","event",myFunct);
    
    # FSM starting state and event 
    f.set_state ("init")
    f.set_event ("init faite")


    # run FSM
    #fonctions d'init à appeler ici.

    while (f.curState != "??"):   # wait for last state to occur
        funct = f.run ()
        newEvent = funct()
        print "New Event : ",newEvent
        f.set_event(newEvent)

    #fonctions d'arret à appeler là
