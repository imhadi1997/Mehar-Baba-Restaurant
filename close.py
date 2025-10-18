from PyQt5 import QtCore, QtGui, QtWidgets

class main_page:
    def __init__(self, parent_root, username, useretype):
        self.parent_root = parent_root
        self.username = username
        self.usertype = useretype

    def close_function(self):
        self.label = QtWidgets.QLabel(self.parent_root)
        self.label.setGeometry(QtCore.QRect(0, 80, 1131, 571))
        self.label.setStyleSheet("border : 1px solid black;")
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("images/Preview MB 02 (1).PNG"))
        self.label.setScaledContents(True)
        self.label.setObjectName("label")
        self.label.show()