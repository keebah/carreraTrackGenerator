# -*- coding: utf-8 -*-
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QAction
                             
def MenuBar(self):
    menubar = self.menuBar()
    
    showMap = QAction(QIcon('stock_imagemap-editor.png'), 'Show Map', self)
    showMap.setStatusTip('Track Map')
    showMap.triggered.connect(
        lambda checked: self.toggleWindow(self.windows["trackplt"])
        )
        
    
    fileMenu = menubar.addMenu('&View')
    fileMenu.addAction(showMap)      
    
    
    findTrack = QAction(QIcon('stock_imagemap-editor.png'), 'Find Track', self)
    findTrack.setStatusTip('Generate random track based on available parts')
    findTrack.triggered.connect(self.findTrack)
        
    
    fileMenu = menubar.addMenu('&Track')
    fileMenu.addAction(findTrack)          
