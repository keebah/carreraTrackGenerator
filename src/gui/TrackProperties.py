# -*- coding: utf-8 -*-
from PyQt5.QtWidgets import ( QWidget, QGridLayout, QLabel, QLineEdit )


class TrackProperties(QWidget):
    def __init__(self, ctgView):
        
        super(QWidget, self).__init__()    
        
        self.ctgView = ctgView
        layout = QGridLayout()

        self.editName = QLineEdit(ctgView.currentTrack["name"])

        layout.addWidget(QLabel('Name'), 0, 0, 1, 1)
        layout.addWidget(self.editName, 0, 1, 1, 1)
        
        self.editLength = QLabel(ctgView.currentTrack["length"])
        layout.addWidget(QLabel('Length'), 1, 0, 1, 1)
        layout.addWidget(self.editLength, 1, 1, 1, 1)        
        
        self.setLayout(layout)

    def updateLabels(self):
        self.editName.setText(self.ctgView.currentTrack["name"])
        self.editLength.setText(self.ctgView.currentTrack["length"]["center"])