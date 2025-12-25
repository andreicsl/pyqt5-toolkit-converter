from PyQt5 import QtCore, QtWidgets
from PyQt5.QtCore import Qt, QUrl
from PyQt5.QtWidgets import (
    QApplication,
    QMainWindow,
    QSizeGrip,
    QMessageBox,
    QToolTip,
)
from PyQt5.QtGui import QDoubleValidator, QIcon, QFont, QDesktopServices, QPixmap
from PyQt5.uic import loadUi

import sys
from ui.jzltoolkit import Ui_MainWindow
from core.weight_conversion import WeightConverter
from core.length_conversion import LengthConverter
from core.bmi_calculation import calculate_bmi
from components.sidebar import Sidebar
from ui.styles.button_style import style1, style2


class MyMainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super(MyMainWindow, self).__init__(parent)
        self.setupUi(self)

        self.clickPosition = None

        # validate to accept an integer and decimal number/s only
        weight_validator = QDoubleValidator(self)
        weight_validator.setNotation(QDoubleValidator.StandardNotation)
        weight_validator.setDecimals(4)
        self.weight_input.setValidator(weight_validator)

        length_validator = QDoubleValidator(self)
        length_validator.setNotation(QDoubleValidator.StandardNotation)
        length_validator.setDecimals(4)
        self.length_input.setValidator(length_validator)

        # set default page
        self.stackedWidget.setCurrentWidget(self.weight_page)

        # navigate to weight page
        self.weight_menu.clicked.connect(
            lambda: self.stackedWidget.setCurrentWidget(self.weight_page)
        )
        self.min_weight.clicked.connect(
            lambda: self.stackedWidget.setCurrentWidget(self.weight_page)
        )

        # navigate to length page
        self.length_menu.clicked.connect(
            lambda: self.stackedWidget.setCurrentWidget(self.length_page)
        )
        self.min_length.clicked.connect(
            lambda: self.stackedWidget.setCurrentWidget(self.length_page)
        )

        # navigate to bmi page
        self.bmi_menu.clicked.connect(
            lambda: self.stackedWidget.setCurrentWidget(self.bmi_page)
        )
        self.min_bmi.clicked.connect(
            lambda: self.stackedWidget.setCurrentWidget(self.bmi_page)
        )
        # navigate to about page
        self.min_about.clicked.connect(
            lambda: self.stackedWidget.setCurrentWidget(self.about_page)
        )
        self.about.clicked.connect(
            lambda: self.stackedWidget.setCurrentWidget(self.about_page)
        )
        # navigate to help page
        self.min_help.clicked.connect(
            lambda: self.stackedWidget.setCurrentWidget(self.help_page_1)
        )
        self.help.clicked.connect(
            lambda: self.stackedWidget.setCurrentWidget(self.help_page_1)
        )

        # HELP PAGES (NEXT)

        # navigate to second page
        self.help_next_1.clicked.connect(
            lambda: self.stackedWidget.setCurrentWidget(self.help_page_2)
        )
        # navigate to third page
        self.help_next_2.clicked.connect(
            lambda: self.stackedWidget.setCurrentWidget(self.help_page_3)
        )

        # navigate to fourth page
        self.help_next_3.clicked.connect(
            lambda: self.stackedWidget.setCurrentWidget(self.help_page_4)
        )
        # navigate to fourth page
        self.help_next_4.clicked.connect(
            lambda: self.stackedWidget.setCurrentWidget(self.help_page_5)
        )

        # HELP PAGES (PREV)

        # prev_1
        self.prev_1.clicked.connect(
            lambda: self.stackedWidget.setCurrentWidget(self.help_page_1)
        )
        # prev_2
        self.prev_2.clicked.connect(
            lambda: self.stackedWidget.setCurrentWidget(self.help_page_2)
        )
        # prev_1
        self.prev_3.clicked.connect(
            lambda: self.stackedWidget.setCurrentWidget(self.help_page_3)
        )
        # prev_1
        self.prev_4.clicked.connect(
            lambda: self.stackedWidget.setCurrentWidget(self.help_page_4)
        )

        # setting default stylesheet
        self.weight_menu_stylesheet = self.weight_menu.styleSheet()
        self.min_weight_stylesheet = self.min_weight.styleSheet()
        self.length_menu_stylesheet = self.length_menu.styleSheet()
        self.min_length_stylesheet = self.min_length.styleSheet()
        self.bmi_menu_stylesheet = self.bmi_menu.styleSheet()
        self.min_bmi_stylesheet = self.min_bmi.styleSheet()

        self.min_weight.setStyleSheet(style1)
        self.weight_menu.setStyleSheet(style2)

        # connect button clicks to a slot function
        self.min_weight.clicked.connect(self.updateButtonStyles)
        self.min_length.clicked.connect(self.updateButtonStyles)
        self.weight_menu.clicked.connect(self.updateButtonStyles)
        self.length_menu.clicked.connect(self.updateButtonStyles)
        self.bmi_menu.clicked.connect(self.updateButtonStyles)
        self.min_bmi.clicked.connect(self.updateButtonStyles)

        # remove window frame
        self.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)

        # sidebar exit button/s
        self.exit_btn.clicked.connect(self.close)
        self.min_exit.clicked.connect(self.close)

        # minimize, maximize, exit
        self.close_btn.clicked.connect(self.exit_msgbox)
        self.max_btn.clicked.connect(self.max_window)
        self.min_btn.clicked.connect(self.showMinimized)

        # initialize sidebar
        self.slide_menu.setFixedWidth(0)
        self.sidebar = Sidebar(self.slide_menu, self.mini_menu, self.option_menu)

        # sidebar button
        self.menu_btn.clicked.connect(self.sidebar.open_sidebar)

        # convert button
        self.convert_btn.clicked.connect(self.convert_weight)
        self.convert_btn_2.clicked.connect(self.convert_length)

        # calculate button
        self.calculate_btn.clicked.connect(self.calculate_bmi)

        # no value msgbox

        QSizeGrip(self.size_grip)

        # clickable links
        self.fb.clicked.connect(self.open_fb)
        self.gm.clicked.connect(self.open_gmail)
        self.ig.clicked.connect(self.open_ig)

    # Reset border styles for buttons
    def updateButtonStyles(self):
        self.weight_menu.setStyleSheet(self.weight_menu_stylesheet)
        self.min_weight.setStyleSheet(self.min_weight_stylesheet)

    # moving the ui using the header frame: mousePressEvent, mouseMoveEvent, mouseReleaseEvent
    def mousePressEvent(self, event):
        if event.button() == QtCore.Qt.LeftButton:
            self.clickPosition = event.globalPos()

    def mouseMoveEvent(self, event):
        if event.buttons() == QtCore.Qt.LeftButton:
            if self.clickPosition is not None:
                if self.header.rect().contains(
                    self.header.mapFromGlobal(self.clickPosition)
                ):
                    self.move(self.pos() + event.globalPos() - self.clickPosition)
                    self.clickPosition = event.globalPos()
                    event.accept()

    def mouseReleaseEvent(self, event):
        self.clickPosition = None

    # resizing the UI (if the UI can be moved, then the UI can be resized also) resizing the window are available only when it's minimized
    def resizeEvent(self, event):
        if self.clickPosition is not None:
            if self.header.rect().contains(
                self.header.mapFromGlobal(self.clickPosition)
            ):
                self.move(self.pos() + event.globalPos() - self.clickPosition)
                self.clickPosition = event.globalPos()
                event.accept()

    # max window
    def max_window(self):
        if self.isMaximized():
            self.showNormal()
        else:
            self.showMaximized()

    # convert weight
    def convert_weight(self):
        # if no value
        if self.weight_input.text() == "":
            msg = QMessageBox()
            msg.setWindowTitle("Invalid Input - JZL Toolkit")
            msg.setText("Please Enter a value for weight.")
            msg.setWindowIcon(QIcon("icon_not.png"))
            msg.setIcon(QMessageBox.Warning)

            msg.setStandardButtons(QMessageBox.Ok)
            msg.exec_()

            return

        input_weight = float(self.weight_input.text())
        convert_from = self.convert_from.currentText()
        convert_to = self.convert_to.currentText()

        converter = WeightConverter()
        converted_weight = converter.convert_weight(
            input_weight, convert_from, convert_to
        )

        # print format (decimal)
        self.weight_result.setPlainText("{:.4f}".format(converted_weight))

    # convert length
    def convert_length(self):
        # if no value
        if self.length_input.text() == "":
            msg = QMessageBox()
            msg.setWindowTitle("Invalid Input - JZL Toolkit")
            msg.setText("Please Enter a value for length.")
            msg.setWindowIcon(QIcon("icon_not.png"))
            msg.setIcon(QMessageBox.Warning)

            msg.setStandardButtons(QMessageBox.Ok)
            msg.exec_()

            return
        length_input = float(self.length_input.text())
        convert_from_2 = self.convert_from_2.currentText()
        convert_to_2 = self.convert_to_2.currentText()

        converter = LengthConverter()
        converted_length = converter.convert_length(
            length_input, convert_from_2, convert_to_2
        )

        self.length_result.setPlainText("{:.4f}".format(converted_length))

    # calculate bmi
    def calculate_bmi(self):
        weight = self.weight_bmi.text()
        height = self.height_bmi.text()
        # if no value
        if weight == "" or height == "":
            msg = QMessageBox()
            msg.setWindowTitle("Invalid Input - JZL Toolkit")
            msg.setText("Please Enter your weight and height.")
            msg.setWindowIcon(QIcon("icon_not.png"))
            msg.setIcon(QMessageBox.Warning)

            msg.setStandardButtons(QMessageBox.Ok)
            msg.exec_()

            return

        else:
            self.weight_bmi.setToolTip("")
            self.height_bmi.setToolTip("")

        weight = float(self.weight_bmi.text())
        height = float(self.height_bmi.text())
        bmi, category = calculate_bmi(weight, height)

        self.bmi_result.setText(f"BMI: {bmi:.2f}\n{category}")

    # exit msgbox
    def exit_msgbox(self):
        msg = QMessageBox()
        msg.setWindowTitle("Quit? - JZL Toolkit")
        msg.setText("Are you sure you want to quit?")
        msg.setWindowIcon(QIcon("icon_not.png"))

        msg.setIcon(QMessageBox.Question)
        msg.setStandardButtons(QMessageBox.Cancel | QMessageBox.Yes)
        x = msg.exec_()

        if x == QMessageBox.Yes:
            QApplication.quit()

    def open_fb(self):
        QDesktopServices.openUrl(QUrl("https://www.facebook.com/jzl.andrei"))

    def open_gmail(self):
        QDesktopServices.openUrl(
            QUrl(
                "https://mail.google.com/mail/?view=cm&fs=1&to=jelomarkandrei@gmail.com"
            )
        )

    def open_ig(self):
        QDesktopServices.openUrl(QUrl("https://www.instagram.com/instagram/"))


def main():
    app = QApplication(sys.argv)
    form = MyMainWindow()
    form.show()
    app.exec_()


if __name__ == "__main__":
    main()
