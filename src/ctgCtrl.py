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
    

                
    def findTrack(self):
        
        validTracksFound = 0
        while validTracksFound < 1:
            track = {"layout": [],
                     "id": '',
                     "coords": ''}
            track["layout"], track["id"] = self.randomTrack()
            track["coords"] = self.ctgModel.drawTrack(track["layout"])
            
            if self.ctgModel.checkValid(track):
                track["name"] = track["id"]
                validTracksFound += 1
                self.ctgModel.tracks.append(track)

        
    def optimizeLaneChange(self):
        # where should the second lane change go to minimize the delta between lane length
        position = []
        
        for i in range(len(self.trackLayout)):
            if self.trackLayout[i] == 's':
                self.trackLayout[i] = 'x'
                sLeft, sRight = self.calculateLaneLength()
                position.append([i, sLeft-sRight])
                self.trackLayout[i] = 's'
        
        
        return position    
    
    
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