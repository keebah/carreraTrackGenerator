# -*- coding: utf-8 -*-
"""
Created on Sun Mar 20 11:15:42 2022

Carrera Track Generator Controller

properties:
    
      
methods:
    - 

@author: kw
"""
from .ctgModel import ctgModel

from random import randint

class ctgCtrl():
    
    def __init__(self):
        
        self.ctgModel = ctgModel()
        
        return
    
    def randomTrack(self):
        nS = self.ctgModel.availableParts["straight"]
        nC = self.ctgModel.availableParts["corner"]
        nX = self.ctgModel.availableParts["laneChange"]
        track = ''
        while len(track) < 30:
            r = randint(0,3)
            if r == 0:
                if nS:
                    nS -= 1
                    track += 's'
            elif r == 1:
                if nC:
                    nC -= 1
                    track += 'l'
            elif r == 2:
                if nC:
                    nC -= 1
                    track += 'r'
            elif r == 3:
                if nX:
                    nX -= 1
                    track += 'x'
        return [char for char in track], track