# -*- coding: utf-8 -*-
"""
GUI for the carrera Track Generator
"""

from .ctgModel import ctgModel

from PyQt5.QtWidgets import (QMainWindow, QTextEdit, QWidget, 
                             QTabWidget, QVBoxLayout, QAction, QFileDialog, 
                             QApplication)

from PyQt5.QtGui import QIcon

import matplotlib
matplotlib.use('Qt5Agg')


from .gui.TrackPlotter import TrackPlotter

class ctgView(QMainWindow):

    def __init__(self):
        super().__init__()
        
        self.ctgModel = ctgModel()
        self.ctgModel.drawTrack()
        self.initUI()

    def initUI(self):
        
        self.windows = {"trackplt": TrackPlotter(self.ctgModel.coordinates)}
        
        self.setGeometry(300, 400, 1024, 768)
        self.setWindowTitle('Carrera Track Generator')
        
        # menubar
        showMap = QAction(QIcon('stock_imagemap-editor.png'), 'Show Map', self)
        showMap.setStatusTip('Track Map')
        showMap.triggered.connect(
            lambda checked: self.toggleWindow(self.windows["trackplt"])
            )
        
        
        menubar = self.menuBar()
        fileMenu = menubar.addMenu('&View')
        fileMenu.addAction(showMap)        
        
        
        self.show()



    def toggleWindow(self, window):
        if window.isVisible():
            window.hide()
        else:
            window.show()




