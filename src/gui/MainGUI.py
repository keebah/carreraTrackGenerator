# -*- coding: utf-8 -*-
from PyQt5.QtWidgets import (QListWidget, QWidget, QGridLayout)

from .TrackProperties import TrackProperties

class MainGUI(QWidget):
    def __init__(self, ctgView):
        super(QWidget, self).__init__()
        ctgView.gui["trackList"] = QListWidget()        
        for iTrack in range(len(ctgView.ctgModel.tracks)):
            ctgView.gui["trackList"].insertItem(iTrack,ctgView.ctgModel.tracks[iTrack]["name"])
            
        ctgView.gui["trackList"].clicked.connect(ctgView.trackListClicked)
        
        
        ctgView.gui["trackProps"] = TrackProperties(ctgView)
        
        layout = QGridLayout()
        layout.addWidget(ctgView.gui["trackList"], 0, 0, 1, 1)
        layout.addWidget(ctgView.gui["trackProps"], 0, 1, 1, 1)
        self.setLayout(layout)