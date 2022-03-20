# -*- coding: utf-8 -*-
"""
Created on Sun Mar 20 12:01:04 2022

@author: kw

Carrera Track Generator - Track Map Plotting GUI
"""
from PyQt5.QtWidgets import (QWidget, QGridLayout, QPushButton)

from matplotlib.backends.backend_qt5agg import (FigureCanvasQTAgg)
from matplotlib.figure import Figure

class TrackPlotter(QWidget):
    
    def __init__(self, coords):
        super().__init__()
        self.layout = QGridLayout(self)
        self.coords = coords
        
        self.plotArea = MplCanvas(self, width=5, height=4, dpi=100)
        self.layout.addWidget(self.plotArea, 0, 0, 1, 2)
        
        btnPlot = QPushButton("Plot")
        btnPlot.clicked.connect(self.plotMap)
        btnClear = QPushButton("Clear")
        btnClear.clicked.connect(self.clearMap)
        
        self.layout.addWidget(btnPlot, 1, 0, 1, 1)
        self.layout.addWidget(btnClear, 1, 1, 1, 1)
        self.setLayout(self.layout)
        
        
                  
        
        
    def plotMap(self):
        self.plotArea.axes1.plot(self.coords["x"],self.coords["y"])
        self.plotArea.axes1.plot(self.coords["xDot"],self.coords["yDot"], 'x', linewidth=0)
        self.plotArea.fig.canvas.draw()
        
    def clearMap(self):
        self.plotArea.axes1.cla()
        self.plotArea.fig.canvas.draw()
        
        
class MplCanvas(FigureCanvasQTAgg):

    def __init__(self, parent=None, width=5, height=4, dpi=100):
        self.fig = Figure(figsize=(width, height), dpi=dpi)
        self.axes1 = self.fig.add_subplot(111)

        super(MplCanvas, self).__init__(self.fig)
