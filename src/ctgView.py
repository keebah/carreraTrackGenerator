# -*- coding: utf-8 -*-
"""
Analysegui für UroFlow Daten

"""
import sys
import os

from .ctgModel import ctgModel

from PyQt5.QtWidgets import (QMainWindow, QTextEdit, QWidget, 
                             QTabWidget, QVBoxLayout, QAction, QFileDialog, 
                             QApplication)

from PyQt5.QtGui import QIcon

import matplotlib
matplotlib.use('Qt5Agg')
from matplotlib.backends.backend_qt5agg import (FigureCanvasQTAgg)
from matplotlib.figure import Figure
import matplotlib.pyplot as plt



class ctgView(QMainWindow):

    def __init__(self):
        super().__init__()
        
        self.ctgModel = ctgModel()
        self.initUI()

    def initUI(self):
        
        self.windows = {"trackplt": TrackPlotter()}
        
        self.setGeometry(300, 400, 1024, 768)
        self.setWindowTitle('Carrera Track Generator')
        
        # menubar
        openFile = QAction(QIcon('stock_imagemap-editor.png'), 'Show Map', self)
        openFile.setStatusTip('Track Map')
        openFile.triggered.connect(
            lambda checked: self.toggleWindow(self.windows["trackplt"])
            )
        
        
        menubar = self.menuBar()
        fileMenu = menubar.addMenu('&View')
        fileMenu.addAction(openFile)        
        
        
        self.show()



    def toggleWindow(self, window):
        if window.isVisible():
            window.hide()
        else:
            window.show()





class TrackPlotter(QWidget):
    
    def __init__(self):
        super().__init__()
        self.layout = QVBoxLayout(self)
        self.setWindowTitle = 'Track Plotter'
        
        self.plotArea = MplCanvas(self, width=5, height=4, dpi=100)
        self.layout.addWidget(self.plotArea)
        self.setLayout(self.layout)

class MplCanvas(FigureCanvasQTAgg):

    def __init__(self, parent=None, width=5, height=4, dpi=100):
        fig = Figure(figsize=(width, height), dpi=dpi)
        self.axes1 = fig.add_subplot(111)
        self.setWindowTitle = 'Track Plotter'

        super(MplCanvas, self).__init__(fig)
