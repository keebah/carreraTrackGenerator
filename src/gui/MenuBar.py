# -*- coding: utf-8 -*-
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QAction
                             
def MenuBar(self):
    showMap = QAction(QIcon('stock_imagemap-editor.png'), 'Show Map', self)
    showMap.setStatusTip('Track Map')
    showMap.triggered.connect(
        lambda checked: self.toggleWindow(self.windows["trackplt"])
        )
        
    menubar = self.menuBar()
    fileMenu = menubar.addMenu('&View')
    fileMenu.addAction(showMap)      