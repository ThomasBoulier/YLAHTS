import fsm
import sys
sys.path.append(r"c:\Python34\Lib\site-packages")
sys.path.append(r"c:\Python34\Lib")
import serial, os, threading
# Manque des imports ?

# global variables
f = fsm.fsm()   # defines finite state machine


# FSM functions 
def myFunct():
    print "do something ..."
    nextEvent = "???"
    return nextEvent
    
def Init():
    print "init"
    nextEvent = "init_done"
    return nextEvent
    
def decollage():
    print "decollage"
    #corps de la fonction
    nextEvent = "decollage_done"
    return nextEvent 

# Main 
if __name__== "__main__":

    # init FSM
    f.add_state ("init")    
    f.add_state ("decollage")
    f.add_state ("???")

    f.add_event ("init_done")
    f.add_event ("decollage_done")
   
    f.add_transition ("??","??","??",myFunct);
    
    # FSM starting state and event 
    f.set_state ("??")
    f.set_event ("??")


    # run FSM
    #fonctions d'init à appeler ici.

    while (f.curState != "??"):   # wait for last state to occur
        funct = f.run ()
        newEvent = funct()
        print "New Event : ",newEvent
        f.set_event(newEvent)

    #fonctions d'arret à appeler là
