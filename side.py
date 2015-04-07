import sys
sys.path.append(r"c:\Python34\Lib\site-packages")
sys.path.append(r"c:\Python34\Lib")
import serial, os, threading
import numpy as np

def isThereAnObject:
  liste = np.zeros(24)
  b = CamDetection()
  liste.append(b)
  rate = liste.count(True)/24
  return (rate > 0.8)
  
def CamDetection :
    #ouverture d'un socket
    #recupe de l'info par le socket
    if (donneesEntrante=="yes")
      return True
    else (donneesEntrante=="no")
      return False
      
