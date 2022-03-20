# -*- coding: utf-8 -*-
from PyQt5.QtWidgets import ( QWidget, QVBoxLayout, QHBoxLayout, QLabel, QLineEdit )


class TrackProperties(QWidget):
    def __init__(self):
        
        super(QWidget, self).__init__()    
        
        layout1 = QVBoxLayout()
        self.name1 = labelLine("bla")
        self.name2 = labelLine("bla")
        self.name3 = labelLine("bla")
        # self.lastName = labelLine(anaView, "Nachname", anaView.anaModel.data["patient"]["nachname"])
        # self.birthday = labelLine(anaView, "Geburtstag", 0)
        # self.date = labelLine(anaView, "Date", 0)
        # layout1.addWidget(self.firstName)
        # layout1.addWidget(self.lastName)
        # layout1.addWidget(self.birthday)
        # layout1.addWidget(self.date)
        
        # layout2 = QHBoxLayout()
        # self.firstName = labelLine("Max. Volumen", anaView.anaModel.data["stats"]["vorname"])
        # self.lastName = labelLine("Max. Fluss", anaView.anaModel.data["stats"]["nachname"])
        # self.date = labelLine("Mittlerer Fluss", anaView.anaModel.data["stats"]["timestamp"][0])
        # layout1.addWidget(self.firstName)
        # layout1.addWidget(self.lastName)
        # layout1.addWidget(self.date)
                
        
        self.setLayout(layout1)

class labelLine(QWidget):
    def __init__(self, label: str):
        
        super(QWidget, self).__init__()

        self.label = QLabel(label)
        self.edit = QLineEdit()
        # self.edit.connect(self.infoLabelChanged, )
        # self.edit.editingFinished.connect(lambda: anaView.infoLabelChanged(self.edit, label))
        layout = QHBoxLayout()
        layout.addWidget(self.label)
        layout.addWidget(self.edit)
