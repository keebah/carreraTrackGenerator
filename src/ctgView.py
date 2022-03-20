# -*- coding: utf-8 -*-
"""
GUI for the carrera Track Generator
"""

from .ctgModel import ctgModel

from PyQt5.QtWidgets import (QMainWindow, QListWidget,
                             QGridLayout)


import matplotlib
matplotlib.use('Qt5Agg')


from .gui.TrackPlotter import TrackPlotter
from .gui.MenuBar import MenuBar

class ctgView(QMainWindow):

    def __init__(self):
        super().__init__()
        
        self.ctgModel = ctgModel()
        self.ctgModel.tracks[0]["coords"] = self.ctgModel.drawTrack(self.ctgModel.tracks[0]["layout"])
        self.ctgModel.tracks[1]["coords"] = self.ctgModel.drawTrack(self.ctgModel.tracks[1]["layout"])
        self.ctgModel.tracks[2]["coords"] = self.ctgModel.drawTrack(self.ctgModel.tracks[2]["layout"])
        
        print(self.ctgModel.checkValid(self.ctgModel.tracks[0]))
        print(self.ctgModel.checkValid(self.ctgModel.tracks[1]))
        print(self.ctgModel.checkValid(self.ctgModel.tracks[2]))
        
        
        self.gui = {}

        self.currentTrack = {}
        
        self.initUI()

        return

    def initUI(self):
        QMainWindow.__init__(self)
        
        self.setGeometry(300, 400, 1024, 768)
        self.setWindowTitle('Carrera Track Generator')        
        
        # register windows
        self.windows = {"trackplt": TrackPlotter(self)}

        # track list
        self.gui["trackList"] = QListWidget()        
        for iTrack in range(len(self.ctgModel.tracks)):
            self.gui["trackList"].insertItem(iTrack,self.ctgModel.tracks[iTrack]["name"])
            
        self.gui["trackList"].clicked.connect(self.trackListClicked)
        
        # menubar
        MenuBar(self)
        
        
        # main window ocntent
        layout = QGridLayout()
        self.setLayout(layout)
        self.setCentralWidget(self.gui["trackList"] )        

        
        self.setLayout(layout)
        self.show()
        
        return

    def trackListClicked(self):
        idx = self.gui["trackList"].currentIndex().row()
        self.currentTrack = self.ctgModel.tracks[idx]
        
        return
    
    def toggleWindow(self, window):
        if window.isVisible():
            window.hide()
        else:
            window.show()

        return



