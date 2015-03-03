import fsm
# Manque des imports

# global variables
f = fsm.fsm()   # defines finite state machine


# FSM functions 
def myFunct():
    print "do something ..."
    nextEvent = "???"
    return nextEvent

# Main 
if __name__== "__main__":

    # init FSM
    f.add_state ("???")
    f.add_state ("???")

    f.add_event ("??")
    f.add_event ("??")
   
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
