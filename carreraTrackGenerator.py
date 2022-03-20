# -*- coding: utf-8 -*-
"""
Created on Sun Mar 20 11:29:35 2022

@author: kw
"""
import sys

from PyQt5.QtWidgets import (QApplication)
from src.ctgView import ctgView


app = QApplication(sys.argv)
ex = ctgView()
sys.exit(app.exec_())