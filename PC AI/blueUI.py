# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'blueUI.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(318, 540)
        self.blueUi = QtWidgets.QWidget(MainWindow)
        self.blueUi.setObjectName("blueUi")
        self.label = QtWidgets.QLabel(self.blueUi)
        self.label.setGeometry(QtCore.QRect(-240, -20, 591, 361))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("C:/Users/sgurp/Downloads/Artificial Intelligence design.gif"))
        self.label.setObjectName("label")
        self.textBrowser = QtWidgets.QTextBrowser(self.blueUi)
        self.textBrowser.setGeometry(QtCore.QRect(-5, 340, 331, 201))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.textBrowser.setFont(font)
        self.textBrowser.setStyleSheet("background: transparent;\n"
"border-radius:none;")
        self.textBrowser.setObjectName("textBrowser")
        MainWindow.setCentralWidget(self.blueUi)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())




# # -*- coding: utf-8 -*-

# # Form implementation generated from reading ui file 'blueUI.ui'
# #
# # Created by: PyQt5 UI code generator 5.15.9
# #
# # WARNING: Any manual changes to this file will be lost when pyuic5 is
# # run again.  Do not edit this file unless you know what you are doing.

# from PyQt5 import QtCore, QtGui, QtWidgets

# class Ui_MainWindow(object):
#     def setupUi(self, MainWindow):
#         MainWindow.setObjectName("MainWindow")
#         MainWindow.resize(318, 540)
#         self.blueUi = QtWidgets.QWidget(MainWindow)
#         self.blueUi.setObjectName("blueUi")
#         self.label = QtWidgets.QLabel(self.blueUi)
#         self.label.setGeometry(QtCore.QRect(-240, -20, 591, 361))
#         self.label.setText("")
#         self.label.setPixmap(QtGui.QPixmap("C:/Users/sgurp/Downloads/Artificial Intelligence design.gif"))
#         self.label.setObjectName("label")
#         self.textBrowser = QtWidgets.QTextBrowser(self.blueUi)
#         self.textBrowser.setGeometry(QtCore.QRect(-5, 340, 331, 201))
#         font = QtGui.QFont()
#         font.setPointSize(12)
#         self.textBrowser.setFont(font)
#         self.textBrowser.setStyleSheet("background: transparent;\n"
#                                         "border-radius:none;")
#         self.textBrowser.setObjectName("textBrowser")
#         MainWindow.setCentralWidget(self.blueUi)

#         self.retranslateUi(MainWindow)
#         QtCore.QMetaObject.connectSlotsByName(MainWindow)

#     def retranslateUi(self, MainWindow):
#         _translate = QtCore.QCoreApplication.translate
#         MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))



# if __name__ == "__main__":
#     import sys
#     app = QtWidgets.QApplication(sys.argv)
#     MainWindow = Main()
#     MainWindow.show()
#     sys.exit(app.exec_())








