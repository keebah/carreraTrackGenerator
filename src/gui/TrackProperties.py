# -*- coding: utf-8 -*-
from PyQt5.QtWidgets import ( QWidget, QGridLayout, QLabel, QLineEdit,
                             QPushButton)


class TrackProperties(QWidget):
    def __init__(self, ctgView):
        
        super(QWidget, self).__init__()    
        
        self.ctgView = ctgView
        layout = QGridLayout()

        self.editName = QLineEdit(ctgView.currentTrack["name"])

        layout.addWidget(QLabel('Name'), 0, 0, 1, 6)
        layout.addWidget(self.editName, 0, 3, 1, 6)
        
        self.txtLengthCenter = QLabel()
        layout.addWidget(QLabel('Length Center'), 1, 0, 1, 6)
        layout.addWidget(self.txtLengthCenter, 1, 3, 1, 6)        
        
        self.txtLengthLeft = QLabel()
        layout.addWidget(QLabel('Length Left'), 2, 0, 1, 6)
        layout.addWidget(self.txtLengthLeft, 2, 3, 1, 6)    
        
        self.txtLengthRight = QLabel()
        layout.addWidget(QLabel('Length Right'), 3, 0, 1, 6)
        layout.addWidget(self.txtLengthRight, 3, 3, 1, 6)    
        self.setLayout(layout)
        
        self.txtAmountStraight = QLabel()
        layout.addWidget(QLabel('Straights'), 4, 0, 1, 6)
        layout.addWidget(self.txtAmountStraight, 4, 3, 1, 6)    
        self.setLayout(layout)
        
        self.txtAmountCorners = QLabel()
        layout.addWidget(QLabel('Corners'), 5, 0, 1, 6)
        layout.addWidget(self.txtAmountCorners, 5, 3, 1, 6)    
        self.setLayout(layout)
        
        buttonL = QPushButton('LEFT')
        buttonL.clicked.connect(
            lambda checked: ctgView.designTrack('l')
            )
        buttonS = QPushButton('STRAIGHT')
        buttonS.clicked.connect(
            lambda checked: ctgView.designTrack('s')
            )        
        buttonR = QPushButton('RIGHT')
        buttonR.clicked.connect(
            lambda checked: ctgView.designTrack('r')
            )
        buttonX = QPushButton('CROSS')
        buttonX.clicked.connect(
            lambda checked: ctgView.designTrack('x')
            )
        
        layout.addWidget(buttonL, 6, 0, 1, 2)
        layout.addWidget(buttonS, 6, 2, 1, 2)
        layout.addWidget(buttonR, 6, 4, 1, 2)
        layout.addWidget(buttonX, 6, 6, 1, 2)
        
        buttonU = QPushButton('Undo')
        buttonU.clicked.connect(
            lambda checked: ctgView.designTrack('undo')
            )
        layout.addWidget(buttonU, 7, 0, 1, 2)

    def updateLabels(self):
        self.editName.setText(self.ctgView.currentTrack["name"])
        self.txtLengthCenter.setText(str(round(self.ctgView.currentTrack["length"]["center"])))
        self.txtLengthLeft.setText(str(round(self.ctgView.currentTrack["length"]["left"])))
        self.txtLengthRight.setText(str(round(self.ctgView.currentTrack["length"]["right"])))
        self.txtAmountStraight.setText(str(self.ctgView.currentTrack["layout"].count('s')))
        self.txtAmountCorners.setText(str(self.ctgView.currentTrack["layout"].count('l')+self.ctgView.currentTrack["layout"].count('r')))

        