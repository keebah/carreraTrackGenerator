# -*- coding: utf-8 -*-
"""
GUI for the carrera Track Generator
"""

from .ctgModel import ctgModel
from .ctgCtrl import ctgCtrl

from PyQt5.QtWidgets import (QMainWindow, QFileDialog)

import json

import matplotlib
matplotlib.use('Qt5Agg')


from .gui.TrackPlotter import TrackPlotter
from .gui.MenuBar import MenuBar
from .gui.MainGUI import MainGUI

class ctgView(QMainWindow):

    def __init__(self):
        super().__init__()
        
        self.ctgCtrl = ctgCtrl()
        self.ctgModel = self.ctgCtrl.ctgModel
        self.ctgModel.tracks[0]["coords"] = self.ctgModel.drawTrack(self.ctgModel.tracks[0]["layout"])
        l,r,c = self.ctgModel.calculateLength(self.ctgModel.tracks[0])
        self.ctgModel.tracks[0]["length"] = {'left': l, 'right': r, 'center': c}
        
        self.ctgModel.tracks[1]["coords"] = self.ctgModel.drawTrack(self.ctgModel.tracks[1]["layout"])
        l,r,c = self.ctgModel.calculateLength(self.ctgModel.tracks[1])
        self.ctgModel.tracks[1]["length"] = {'left': l, 'right': r, 'center': c}
        
        self.ctgModel.tracks[2]["coords"] = self.ctgModel.drawTrack(self.ctgModel.tracks[2]["layout"])
        l,r,c = self.ctgModel.calculateLength(self.ctgModel.tracks[2])
        self.ctgModel.tracks[2]["length"] = {'left': l, 'right': r, 'center': c}
        
        print(self.ctgModel.checkValid(self.ctgModel.tracks[0], True))
        print(self.ctgModel.checkValid(self.ctgModel.tracks[1], True))
        print(self.ctgModel.checkValid(self.ctgModel.tracks[2], True))
        
        
        self.gui = {}

        self.currentTrack = {"name": "", "length": {"left", "right", "center"}}
        
        self.initUI()

        return

    def initUI(self):
        QMainWindow.__init__(self)
        
        self.setGeometry(300, 400, 1024, 768)
        self.setWindowTitle('Carrera Track Generator')        
        
        # register windows
        self.windows = {"trackplt": TrackPlotter(self)}

        # menubar
        MenuBar(self)        
        
        # main window ocntent
        self.setCentralWidget(MainGUI(self))        

        self.show()
        
        return

    def trackListClicked(self):
        idx = self.gui["trackList"].currentIndex().row()
        self.currentTrack = self.ctgModel.tracks[idx]
        self.gui["trackProps"].updateLabels()
        return
    
    def toggleWindow(self, window):
        if window.isVisible():
            window.hide()
        else:
            window.show()
        return

    def findTrack(self):
        self.ctgCtrl.findTrack()
        self.gui["trackList"].insertItem(len(self.ctgModel.tracks), 
                                         self.ctgModel.tracks[len(self.ctgModel.tracks)-1]["name"])

    def designTrack(self, option):
        self.currentTrack = self.ctgCtrl.designTrack(self.currentTrack, option)
        self.windows["trackplt"].clearMap()
        self.windows["trackplt"].plotMap()
        self.gui["trackProps"].updateLabels()

    def exportTrack(self):
        name = QFileDialog.getSaveFileName(self, 'Save File')
        with open(name[0], 'w') as outfile:
            json.dump(self.currentTrack, outfile)        
        return