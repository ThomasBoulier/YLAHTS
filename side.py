import sys
sys.path.append(r"c:\Python34\Lib\site-packages")
sys.path.append(r"c:\Python34\Lib")
import serial, os, threading
import numpy as np

def isThereAnObject:
  liste = np.zeros(24)
  b = objectFrontCam()
  liste.append(b)
  rate = liste.count(True)/24
  return (rate > 0.8)
  
def objectFrontCam :
  return ()
