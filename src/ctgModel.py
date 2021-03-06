# -*- coding: utf-8 -*-
"""
Created on Sun Mar 20 11:15:42 2022

Carrera Track Generator Model

properties:
    - layout: list of strings describing a carrera track layout
      - s: straight (345mm long)
      - c: corner with 60deg radius
      - x: lane change
    - coords: dictionary 
      - x,y: list of coordinates used to plot the track centerline
      - xDot,yDot: list of coordinates to plot the physical part intersections
      - a: heading angle of the element
    - id: unique string of the track layout (yes I know it's kind of duplicate)
    - name: user can dedicde on a name
    
methods:
    - 

@author: kw
"""

import math

class ctgModel():
    
    def __init__(self):
        self.tracks = [{'name': 'Wohnzimmer',
                        'layout': ['s','r','r','s','r','s','l','x','l','l','l','l','l','r','l','s','l','r','r','s','s','r','r','s','s','s','s','s','s'],
                        'id': 'srrsrslxlllllrlslrrssrrssssss',
                        'coords': {'x': [],
                                   'y': [],
                                   'xDot': [],
                                   'yDot': [],
                                   'a': []},
                        'length': {'left','right','center'}},
                       {'name': 'Evolution',
                        'layout': ['s','s','l','l','l','l','s','s','s','r','s','r','r','r','s','s'],
                        'id': 'ssllllsssrsrrrss',
                        'coords': {'x': [],
                                   'y': [],
                                   'xDot': [],
                                   'yDot': [],
                                   'a': []},
                        'length': {'left','right','center'}},         
                       {'name': 'SmallCircle',
                        'layout': ['s','l','l','l','s','l','l','l'],
                        'id': 'slllslll',
                        'coords': {'x': [],
                                   'y': [],
                                   'xDot': [],
                                   'yDot': [],
                                   'a': []},
                        'length': {'left','right','center'}},         
                       {'name': 'Wohnzimmer2',
                        'layout': ['s','s','r','r','s','s','l','l','l','l','l','r','x','l','s','l','l','r','s','r','r','s','x','s','r','r','s','s','s','s'],
                        'id': 'ssrrsslllllrxlsllrsrrsxsrrssss',
                        'coords': {'x': [],
                                   'y': [],
                                   'xDot': [],
                                   'yDot': [],
                                   'a': []},
                        'length': {'left','right','center'}},                          
                       ]
        
        self.availableParts = {'straight': 12,
                               'corner': 16,
                               'laneChange': 2}

        return
    
    @staticmethod
    def drawTrack(trackLayout):
        def drawStraight(x, y, s, heading):
            length = 345
            s.append(s[-1] + length)
            x.append(x[-1] + length * math.sin(heading[-1]))
            y.append(y[-1] + length * math.cos(heading[-1]))
            heading.append(heading[-1])
            
            return x, y, s, heading
        
        def drawCorner(x, y, s, heading, direction):
            length = 311.05
            drawSteps = 6
            # draw a cricle in steps of 10deg => 60deg total for corner
            for i in range(drawSteps):
                if direction == 'l':
                    heading.append(heading[-1] - 1/drawSteps * math.pi/3)
                if direction == 'r':
                    heading.append(heading[-1] + 1/drawSteps * math.pi/3)
                    
                meanHeading = (heading[-2]+heading[-1])/2
                s.append(s[-1] + length/drawSteps)
                x.append(x[-1] + length/drawSteps * math.sin(meanHeading))
                y.append(y[-1] + length/drawSteps * math.cos(meanHeading))
                
            return x, y, s, heading        
        
        s = [0]
        x = [0]
        y = [0]
        heading = [0]
        xDot = [0]
        yDot = [0]
        for elem in trackLayout:
            if elem == 's':
                x, y, s, heading = drawStraight(x, y, s, heading)
            elif elem == 'x':
                x, y, s, heading = drawStraight(x, y, s, heading)
                xDot.append((x[-1]-x[-2])/2+x[-2])
                yDot.append((y[-1]-y[-2])/2+y[-2])                
            else:
                x, y, s, heading = drawCorner(x, y, s, heading, elem)
                
            xDot.append(x[-1])
            yDot.append(y[-1])
     
        
        return  {"x": x, "y": y, "a": heading, "s": s, "xDot": xDot, "yDot": yDot}

    @staticmethod
    def checkValid(track, forceCrossing):
        if len(track["layout"]) >= 8:
            if abs(track["coords"]["x"][-1]) < 10 and \
               abs(track["coords"]["y"][-1]) < 10:
                   if forceCrossing:
                       if abs(track["coords"]["a"][-1]) < 1:
                           return True
                   else:
                       if abs(track["coords"]["a"][-1] % (2*math.pi)) < 1:
                           return True
           
        return False
    
    @staticmethod
    def calculateLength(track):
        leftLane = 0
        rightLane = 0
        centerLine = 0
        for elem in track["layout"]:
            if elem == 's':
                leftLane += 345
                rightLane += 345
                centerLine += 345
            if elem == 'l':
                centerLine += 311.05
                leftLane += 259.2
                rightLane += 362.9
            if elem == 'r':
                centerLine += 311.05
                leftLane += 362.9
                rightLane += 259.2
            if elem == 'x':
                centerLine += 345
                temp = rightLane
                rightLane = leftLane + 364.2
                leftLane = temp + 364.2
                
        return leftLane, rightLane, centerLine