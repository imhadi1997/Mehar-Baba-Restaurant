from PyQt5 import QtCore, QtGui, QtWidgets
from close import main_page
from database import menu_database
from PyQt5.QtWidgets import QMessageBox
from PyQt5.QtWidgets import QHeaderView


class menu_class:
    #   init
    def __init__(self, centralwidget, username , usertype, mainwindow, userid):
        self.centralwidget = centralwidget
        self.username = username
        self.usertype = usertype
        self.mainwindow = mainwindow
        self.userid = userid
        

    #   Stock Frame
    def menu_frame(self):
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(0, 80, 1131, 571))
        self.frame.setStyleSheet("background-color: rgb(255, 255, 204);\n"
        "border-style: groove;")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.frame.show()
        self.widget = QtWidgets.QWidget(self.frame)
        self.widget.setGeometry(QtCore.QRect(60, 50, 1011, 461))
        self.widget.setStyleSheet("border: 1px solid black;")
        self.widget.setObjectName("widget")
        self.widget.show()

        self.label = QtWidgets.QLabel(self.widget)
        self.label.setGeometry(QtCore.QRect(10, 10, 81, 21))
        self.label.setStyleSheet("border : 0px;")
        self.label.setObjectName("label")
        self.label.show()

        self.lineEdit = QtWidgets.QLineEdit(self.widget)
        self.lineEdit.setGeometry(QtCore.QRect(100, 10, 191, 21))
        self.lineEdit.setStyleSheet("background-color: rgb(255, 255, 255);\n"
        "color: rgb(0, 0, 0);\n"
        "font: 8pt \"MS Shell Dlg 2\";\n"
        "border : 1px solid black;")
        self.lineEdit.setPlaceholderText("")
        self.lineEdit.setCursorMoveStyle(QtCore.Qt.LogicalMoveStyle)
        self.lineEdit.setClearButtonEnabled(False)
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit.show()

        self.tableView = QtWidgets.QTableView(self.widget)
        self.tableView.setGeometry(QtCore.QRect(15, 40, 420, 411))
        self.tableView.setStyleSheet("font: 8pt \"MS Shell Dlg 2\";\n"
        "background-color: rgb(255, 255, 255);\n"
        "color: rgb(0, 0, 0);\n"
        "")
        self.tableView.setGridStyle(QtCore.Qt.SolidLine)
        self.tableView.setObjectName("tableView")
        self.tableView.show()

        self.pushButton = QtWidgets.QPushButton(self.widget)
        self.pushButton.setGeometry(QtCore.QRect(300, 10, 75, 23))
        self.pushButton.setStyleSheet("QPushButton {\n"
        "    background-color: #f0f0f0;\n"
        "    border: 1px solid #555;\n"
        "    padding: 5px;\n"
        "}\n"
        "\n"
        "QPushButton:pressed {\n"
        "    background-color: #b9ffb9;       /* darker when pressed */\n"
        "    border-style: inset;             /* gives a pushed-in look */\n"
        "}\n"
        "")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("images/blue-save-disk-icon-0.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton.setIcon(icon)
        self.pushButton.setObjectName("pushButton")
        self.pushButton.show()

        self.pushButton_2 = QtWidgets.QPushButton(self.widget)
        self.pushButton_2.setGeometry(QtCore.QRect(380, 10, 75, 23))
        self.pushButton_2.setStyleSheet("QPushButton {\n"
        "    background-color: #f0f0f0;\n"
        "    border: 1px solid #555;\n"
        "    padding: 5px;\n"
        "}\n"
        "\n"
        "QPushButton:pressed {\n"
        "    background-color: #ffad9e;       /* darker when pressed */\n"
        "    border-style: inset;             /* gives a pushed-in look */\n"
        "}\n"
        "")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("images/delete-sign.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_2.setIcon(icon1)
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_2.show()

        _translate = QtCore.QCoreApplication.translate
        self.label.setText(_translate("MainWindow", "    Master input :"))
        self.pushButton.setText(_translate("MainWindow", "Save"))
        self.pushButton_2.setText(_translate("MainWindow", "Close"))
        self.lineEdit.setFocus()
        self.pushButton_2.clicked.connect(lambda: self.close_button())
        self.pushButton.clicked.connect(self.save_new_master_input)

        model = QtGui.QStandardItemModel()
        model.setHorizontalHeaderLabels(["Code", "Name"])
        checkdata = menu_database().master_input_table()
        if checkdata == [] or checkdata != []:
            for row in checkdata:
                code_item = QtGui.QStandardItem(str(row[1]))
                code_item.setFlags(code_item.flags() & ~QtCore.Qt.ItemIsEditable)

                # Column 1 → name (editable)
                name_item = QtGui.QStandardItem(str(row[2]))
                model.appendRow([code_item, name_item])
        elif checkdata == False:
            self.mainwindow.setEnabled(False)
            self.msg_box = QMessageBox(self.mainwindow)
            self.msg_box.setWindowTitle('Error')
            self.msg_box.setIcon(QMessageBox.Critical)
            self.msg_box.setText('Contact admin, database connection lost')
            self.msg_box.setStandardButtons(QMessageBox.Ok)
            self.msg_box.exec_()
            self.mainwindow.setEnabled(True)

        self.tableView.setModel(model)
        self.tableView.setColumnWidth(0, 120)   # Code column width
        self.tableView.setColumnWidth(1, 250)   # Name column width
        header = self.tableView.horizontalHeader()
        header.setSectionResizeMode(QHeaderView.Fixed)
        model.itemChanged.connect(self.on_item_changed)
        
        self.pushButton_2.setDefault(True)
        self.pushButton.setDefault(True)
        
    #   Close to Main Window
    def close_button(self):
        main_page(self.centralwidget, self.username, self.usertype).close_function()

    #   Edit Master Item
    def on_item_changed(self, item):
        row = item.row()
        col = item.column()

        # Only handle edits in the "Name" column (index 1)
        if col == 1:
            new_name = item.text()
            code = self.tableView.model().item(row, 0).text()

            updatetable = menu_database().update_master_input_edit(new_name, code)
            if updatetable == True:
                self.mainwindow.setEnabled(False)
                self.msg_box = QMessageBox(self.mainwindow)
                self.msg_box.setWindowTitle('Edited')
                self.msg_box.setIcon(QMessageBox.Information)
                self.msg_box.setText('Master input edited')
                self.msg_box.setStandardButtons(QMessageBox.Ok)
                self.msg_box.exec_()
                self.mainwindow.setEnabled(True)
                self.menu_frame()
            elif updatetable == False:
                self.mainwindow.setEnabled(False)
                self.msg_box = QMessageBox(self.mainwindow)
                self.msg_box.setWindowTitle('Error')
                self.msg_box.setIcon(QMessageBox.Critical)
                self.msg_box.setText('Contact admin, database connection lost')
                self.msg_box.setStandardButtons(QMessageBox.Ok)
                self.msg_box.exec_()
                self.mainwindow.setEnabled(True)
        else:
            pass

    #   Save New Master input
    def save_new_master_input(self):
        itemname = self.lineEdit.text()
        savenew = menu_database().save_new_master_input_table(itemname)
        if savenew == True:
            self.mainwindow.setEnabled(False)
            self.msg_box = QMessageBox(self.mainwindow)
            self.msg_box.setWindowTitle('Saved')
            self.msg_box.setIcon(QMessageBox.Information)
            self.msg_box.setText('New master input saved')
            self.msg_box.setStandardButtons(QMessageBox.Ok)
            self.msg_box.exec_()
            self.mainwindow.setEnabled(True)
            self.menu_frame()
        elif savenew == False:
            self.mainwindow.setEnabled(False)
            self.msg_box = QMessageBox(self.mainwindow)
            self.msg_box.setWindowTitle('Error')
            self.msg_box.setIcon(QMessageBox.Critical)
            self.msg_box.setText('Contact admin, database connection lost')
            self.msg_box.setStandardButtons(QMessageBox.Ok)
            self.msg_box.exec_()
            self.mainwindow.setEnabled(True)


    #Enter key
    def keyPressEvent(self, event):
        if event.key() in (QtCore.Qt.Key_Return, QtCore.Qt.Key_Enter):
            focus_widget = self.focusWidget()
            if isinstance(focus_widget, QtWidgets.QPushButton):
                focus_widget.click() 