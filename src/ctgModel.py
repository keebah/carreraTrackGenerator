# -*- coding: utf-8 -*-
"""
Created on Sun Mar 20 11:15:42 2022

Carrera Track Generator Model

properties:
    - track layout: list of strings describing a carrera track layout
      - s: straight (345mm long)
      - c: corner with 60deg radius
      - x: lane change
    - coordinates: dictionary 
      - x,y: list of coordinates used to plot the track centerline
      - xDot,yDot: list of coordinates to plot the physical part intersections
      - a: heading angle of the element
      
methods:
    - 

@author: kw
"""

from matplotlib import pyplot as plt
import math
from random import randint


class ctgModel():
    
    def __init__(self):
        # self.trackLayout = ['s','s','r','r','r','s','s','r','r','r']
        self.trackLayout = ['s','s','l','l','l','l','s','s','s','r','s','r','r','r','s','s']   # carrera evolution basic layout
        self.trackLayout = ['s','r','r','s','r','s','l','x','l','l','l','l','l','r','l','s','l','r','r','s','s','r','r','s','s','s','s','s','s']
        self.tracks = [{'name': 'Wohnzimmer',
                        'layout': ['s','r','r','s','r','s','l','x','l','l','l','l','l','r','l','s','l','r','r','s','s','r','r','s','s','s','s','s','s'],
                        'coords': {'x': [],
                                   'y': [],
                                   'xDot': [],
                                   'yDot': [],
                                   'a': []}},
                       {'name': 'Evolution',
                        'layout': ['s','s','l','l','l','l','s','s','s','r','s','r','r','r','s','s'],
                        'coords': {'x': [],
                                   'y': [],
                                   'xDot': [],
                                   'yDot': [],
                                   'a': []}},          
                       {'name': 'SmallCircle',
                        'layout': ['s','l','l','l','s','l','l','l'],
                        'coords': {'x': [],
                                   'y': [],
                                   'xDot': [],
                                   'yDot': [],
                                   'a': []}},                        
                       ]
        # self.trackLayout = ['s','r','r','s','r','s','l','s','l','l','l','l','l','r','l','s','l','r','r','s','s','r','r','s','s','s','s','s','s']
        self.coordinates = {'x': [],
                            'y': [],
                            'xDot': [],
                            'yDot': [],
                            'a': []}
        
        self.availableParts = {'straight': 12,
                               'corner': 16,
                               'laneChange': 2}
        
        self.validTracks = []
        return
    

   
    def plotTrack(self):
       
        plt.plot(self.coordinates["x"],self.coordinates["y"])
        plt.plot(self.coordinates["xDot"],self.coordinates["yDot"], 'x', linewidth=0)
        
        plt.show()
   

    



    
    def buildTrack(self):
        nS = self.availableParts["straight"]
        nC = self.availableParts["corner"]
        nX = self.availableParts["laneChange"]
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
                
    def runOpti(self):
        
        validTracksFound = 0
        while validTracksFound < 10:
            trackLayout, trackString = self.buildTrack()
            self.trackLayout = trackLayout
            self.drawTrack()
            if self.checkValid():
                validTracksFound += 1
                self.validTracks.append(trackString)

        
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

    @staticmethod
    def drawTrack(trackLayout):
        def drawStraight(x, y, heading):
            length = 345
            x.append(x[-1] + length * math.sin(heading[-1]))
            y.append(y[-1] + length * math.cos(heading[-1]))
            heading.append(heading[-1])
            
            return x, y, heading
        
        def drawCorner(x, y, heading, direction):
            length = 311.05
            drawSteps = 6
            # draw a cricle in steps of 10deg => 60deg total for corner
            for i in range(drawSteps):
                if direction == 'l':
                    heading.append(heading[-1] - 1/drawSteps * math.pi/3)
                if direction == 'r':
                    heading.append(heading[-1] + 1/drawSteps * math.pi/3)
                    
                meanHeading = (heading[-2]+heading[-1])/2
                x.append(x[-1] + length/drawSteps * math.sin(meanHeading))
                y.append(y[-1] + length/drawSteps * math.cos(meanHeading))
                
            return x, y, heading        
        
        x = [0]
        y = [0]
        heading = [0]
        xDot = [0]
        yDot = [0]
        for elem in trackLayout:
            if elem == 's' or elem == 'x':
                x, y, heading = drawStraight(x, y, heading)
            else:
                x, y, heading = drawCorner(x, y, heading, elem)
                
            xDot.append(x[-1])
            yDot.append(y[-1])
     
        
        return  {"x": x, "y": y, "a": heading, "xDot": xDot, "yDot": yDot}

    @staticmethod
    def checkValid(track):
        if len(track["layout"]) >= 8:
            if abs(track["coords"]["x"][-1]) < 10 and \
               abs(track["coords"]["y"][-1]) < 10 and \
               abs(track["coords"]["a"][-1] % (2*math.pi)) < 10:
                   return True
           
        return False
    
    @staticmethod
    def calculateLaneLength(track):
        leftLane = 0
        rightLane = 0
        for elem in track["layout"]:
            if elem == 's':
                leftLane += 345
                rightLane += 345
            if elem == 'l':
                leftLane += 259.2
                rightLane += 362.9
            if elem == 'r':
                leftLane += 362.9
                rightLane += 259.2
            if elem == 'x':
                temp = rightLane
                rightLane = leftLane + 364.2
                leftLane = temp + 364.2
                
        return leftLane, rightLane