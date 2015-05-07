import sys
import numpy as np

sys.path.append(r"c:\Python34\Lib\site-packages")
sys.path.append(r"c:\Python34\Lib")
import os, threading


def isThereAnObject():
    liste = [0 for i in range(24)]
    b = CamDetection()
    liste.append(b)
    rate = liste.count(True) / 24
    return rate > 0.8


def CamDetection():
    # ouverture d'un socket
    #recupe de l'info par le socket
    if donneesEntrante == "yes":
        return True
    elif donneesEntrante == "no":
        return False

def LoadWP(filepath):
    alt = []
    lat = []
    long = []
    file=open(filepath)
    count = 0
    for line in file:
        data = line.split('	')
        count += 1
        if count > 2:
            lat.append(float(data[8]))
            long.append(float(data[9]))
            alt.append(float(data[10]))

    return [lat.reverse(), long.reverse(), alt.reverse()] #pour avoir les wp dans le bon ordre en utilisant pop()
