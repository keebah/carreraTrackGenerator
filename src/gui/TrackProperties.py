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
        
        self.txtLengthCenter = QLabel()
        layout.addWidget(QLabel('Length Center'), 1, 0, 1, 1)
        layout.addWidget(self.txtLengthCenter, 1, 1, 1, 1)        
        
        self.txtLengthLeft = QLabel()
        layout.addWidget(QLabel('Length Left'), 2, 0, 1, 1)
        layout.addWidget(self.txtLengthLeft, 2, 1, 1, 1)    
        
        self.txtLengthRight = QLabel()
        layout.addWidget(QLabel('Length Right'), 3, 0, 1, 1)
        layout.addWidget(self.txtLengthRight, 3, 1, 1, 1)    
        self.setLayout(layout)

    def updateLabels(self):
        self.editName.setText(self.ctgView.currentTrack["name"])
        self.txtLengthCenter.setText(str(round(self.ctgView.currentTrack["length"]["center"])))
        self.txtLengthLeft.setText(str(round(self.ctgView.currentTrack["length"]["left"])))
        self.txtLengthRight.setText(str(round(self.ctgView.currentTrack["length"]["right"])))