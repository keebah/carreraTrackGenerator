# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
from matplotlib import pyplot as plt
import math
from random import randint

class trackGenerator():
    
    def __init__(self):
        # self.trackLayout = ['s','s','r','r','r','s','s','r','r','r']
        self.trackLayout=['s','s','l','l','l','l','s','s','s','r','s','r','r','r','s','s']        
        self.coordinates = {'x': [],
                            'y': [],
                            'xDot': [],
                            'yDot': [],
                            'a': []}
        
        self.validTracks = []
        return
    
    def drawStraight(self, x, y, heading):
        length = 345
        x.append(x[-1] + length * math.sin(heading[-1]))
        y.append(y[-1] + length * math.cos(heading[-1]))
        
        return x, y
    
    def drawCorner(self, x, y, heading, direction):
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
        return x, y
   
    def plotTrack(self):
       
        plt.plot(self.coordinates["x"],self.coordinates["y"])
        plt.plot(self.coordinates["xDot"],self.coordinates["yDot"], 'x', linewidth=0)
        
        plt.show()
   
    def calculateLaneLength(self):
        leftLane = 0
        rightLane = 0
        for elem in self.trackLayout:
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
    
    def drawTrack(self):
        x = [0]
        y = [0]
        heading = [0]
        xDot = [0]
        yDot = [0]
        for elem in self.trackLayout:
            if elem == 's':
                x, y = self.drawStraight(x, y, heading)
            else:
                x, y = self.drawCorner(x, y, heading, elem)
                
            xDot.append(x[-1])
            yDot.append(y[-1])

        self.coordinates["x"] = x
        self.coordinates["y"] = y
        self.coordinates["a"] = heading
        self.coordinates["xDot"] = xDot
        self.coordinates["yDot"] = yDot        
        
        return

    def checkValid(self):
        if abs(self.coordinates["x"][-1]) < 1 and abs(self.coordinates["y"][-1]) < 1 and abs(self.coordinates["a"][-1]) < 1:
               return True
           
        return False
    
    def buildTrack(self):
        nS = 14
        nC = 16
        track = ''
        while len(track) < 30:
            r = randint(0,2)
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

        
    
g = trackGenerator()

# g.drawTrack()
# print(g.checkValid())
# t = g.buildTrack()
# g.trackLayout = t
# g.drawTrack()
# g.plotTrack()

# g.runOpti()

# g.trackLayout = [char for char in g.validTracks[3]]
# g.drawTrack()
# g.plotTrack()

# nSegmentsStraight = 14
# nSegmentsCorner = 16

# nSegmentsTotal = nSegmentsStraight + nSegmentsCorner

# headingAngle = 0

# lengthStraight = 35.4
# lengthCorner = 32.1


# trackLayout = ['s','s','r','r','r','s','s','r','r','r']
# for i in range(nSegmentsTotal):
#     # pick segment
    