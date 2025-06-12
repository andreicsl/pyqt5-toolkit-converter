from PyQt5 import QtCore
from PyQt5.QtWidgets import QFrame


class Sidebar:
    def __init__(self, slide_menu, mini_menu, option_menu):
        self.slide_menu = slide_menu
        self.mini_menu = mini_menu
        self.option_menu = option_menu
        self.sidebar_open = False

    def open_sidebar(self):
        if not self.sidebar_open:
            self.sidebar_open = True
            self.animation_open = QtCore.QPropertyAnimation(
                self.slide_menu, b"minimumWidth"
            )
            self.animation_open.setDuration(200)
            self.animation_open.setStartValue(0)
            self.animation_open.setEndValue(200)
            self.animation_open.setEasingCurve(QtCore.QEasingCurve.OutQuart)
            self.animation_open.start()

            # change mini_menu color
            self.mini_menu.setStyleSheet("background-color:rgb(24, 24, 36);")
            self.option_menu.setStyleSheet("background-color:rgb(24, 24, 36);")
        else:
            self.sidebar_open = False
            self.animation_close = QtCore.QPropertyAnimation(
                self.slide_menu, b"minimumWidth"
            )
            self.animation_close.setDuration(200)
            self.animation_close.setStartValue(200)
            self.animation_close.setEndValue(0)
            self.animation_close.setEasingCurve(QtCore.QEasingCurve.OutQuart)
            self.animation_close.start()

            self.mini_menu.setStyleSheet("background-color:rgb(9, 5, 13);")
            self.option_menu.setStyleSheet("background-color:rgb(9, 5, 13);")
