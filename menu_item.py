from close import main_page
from PyQt5 import QtCore, QtGui, QtWidgets
from database import main_category_database
from PyQt5.QtWidgets import QMessageBox
from PyQt5.QtWidgets import QHeaderView



class menu_item_class:
    #   init
    def __init__(self, centralwidget, username , usertype, mainwindow, userid):
        self.centralwidget = centralwidget
        self.username = username
        self.usertype = usertype
        self.mainwindow = mainwindow
        self.userid = userid
        

    #   Add Item Frame
    def add_item_frame(self):
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

        self.lineEdit_3 = QtWidgets.QLineEdit(self.widget)
        self.lineEdit_3.setGeometry(QtCore.QRect(100, 70, 191, 21))
        self.lineEdit_3.setStyleSheet("background-color: rgb(255, 255, 255);\n"
        "color: rgb(0, 0, 0);\n"
        "font: 8pt \"MS Shell Dlg 2\";\n"
        "border : 1px solid black;")
        self.lineEdit_3.setPlaceholderText("")
        self.lineEdit_3.setCursorMoveStyle(QtCore.Qt.LogicalMoveStyle)
        self.lineEdit_3.setClearButtonEnabled(False)
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.lineEdit_3.show()

        self.pushButton = QtWidgets.QPushButton(self.widget)
        self.pushButton.setGeometry(QtCore.QRect(100, 100, 75, 23))
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
        self.pushButton_2.setGeometry(QtCore.QRect(190, 100, 75, 23))
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

        self.tableView = QtWidgets.QTableView(self.widget)
        self.tableView.setGeometry(QtCore.QRect(310, 10, 540, 441))
        self.tableView.setStyleSheet("font: 8pt \"MS Shell Dlg 2\";\n"
        "background-color: rgb(255, 255, 255);\n"
        "color: rgb(0, 0, 0);\n"
        "")
        self.tableView.setGridStyle(QtCore.Qt.SolidLine)
        self.tableView.setObjectName("tableView")
        self.tableView.show()

        self.label_2 = QtWidgets.QLabel(self.widget)
        self.label_2.setGeometry(QtCore.QRect(20, 40, 81, 21))
        self.label_2.setStyleSheet("border : 0px;")
        self.label_2.setObjectName("label_2")
        self.label.show()
        self.label_2.show()
        
        self.lineEdit_2 = QtWidgets.QLineEdit(self.widget)
        self.lineEdit_2.setGeometry(QtCore.QRect(100, 40, 191, 21))
        self.lineEdit_2.setStyleSheet("background-color: rgb(255, 255, 255);\n"
        "color: rgb(0, 0, 0);\n"
        "font: 8pt \"MS Shell Dlg 2\";\n"
        "border : 1px solid black;")
        self.lineEdit_2.setReadOnly(True)
        self.lineEdit_2.setCursorMoveStyle(QtCore.Qt.LogicalMoveStyle)
        self.lineEdit_2.setClearButtonEnabled(False)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.lineEdit_2.show()

        self.label_3 = QtWidgets.QLabel(self.widget)
        self.label_3.setGeometry(QtCore.QRect(10, 70, 81, 21))
        self.label_3.setStyleSheet("border : 0px;")
        self.label_3.setObjectName("label_3")
        self.label_3.show()


        _translate = QtCore.QCoreApplication.translate
        self.label.setText(_translate("MainWindow", "    Master input :"))
        self.pushButton.setText(_translate("MainWindow", "Save"))
        self.pushButton_2.setText(_translate("MainWindow", "Close"))
        self.label_2.setText(_translate("MainWindow", "  Master id :"))
        self.lineEdit_2.setPlaceholderText(_translate("MainWindow", "Master id"))
        self.label_3.setText(_translate("MainWindow", "     item Name :"))
        self.lineEdit.setFocus()
        self.pushButton_2.clicked.connect(lambda: self.close_button())
        self.pushButton.clicked.connect(self.save_newitem)

        master_input_dict = {}
        model = QtGui.QStandardItemModel()
        model.setHorizontalHeaderLabels(["Code", "Master", "item"])
        checkdata = main_category_database().existing_main_category()
        if checkdata == [] or checkdata != []:
            for row in checkdata:
                code_item = QtGui.QStandardItem(str(row[1]))
                code_item.setFlags(code_item.flags() & ~QtCore.Qt.ItemIsEditable)

                master_input = QtGui.QStandardItem(str(row[4]))
                master_input.setFlags(code_item.flags() & ~QtCore.Qt.ItemIsEditable)

                # Column 1 → name (editable)
                name_item = QtGui.QStandardItem(str(row[3]))
                model.appendRow([code_item, master_input, name_item])
                master_input_dict[str(row[4])] = str(row[2])
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
        self.tableView.setColumnWidth(0, 100)   # Code column width
        self.tableView.setColumnWidth(1, 120)   # Name column width
        self.tableView.setColumnWidth(2, 250)
        header = self.tableView.horizontalHeader()
        header.setSectionResizeMode(QHeaderView.Fixed)
        model.itemChanged.connect(self.on_item_changed)

        self.completer_model = QtCore.QStringListModel()
        self.completer_model.setStringList(list(master_input_dict.keys()))
        
        self.completer = QtWidgets.QCompleter(self.completer_model)
        self.completer.setCaseSensitivity(QtCore.Qt.CaseInsensitive)
        self.completer.setFilterMode(QtCore.Qt.MatchContains)
        self.lineEdit.setCompleter(self.completer)

        def on_completer_activated(text):
            self.lineEdit.setText(text)
            self.lineEdit_2.setText(master_input_dict[text])
        
        def on_lineedit_text_changed(text):
            if text == "":
                self.lineEdit_2.clear()

        self.completer.activated[str].connect(on_completer_activated)
        self.lineEdit.textChanged.connect(on_lineedit_text_changed)

    #   Close to Main Window
    def close_button(self):
        main_page(self.centralwidget, self.username, self.usertype).close_function()

    #   Edit Item Name
    def on_item_changed(self, item):
        row = item.row()
        col = item.column()

        # Only handle edits in the "Name" column (index 1)
        if col == 2:
            new_name = item.text()
            code = self.tableView.model().item(row, 0).text()

            updatetable = main_category_database().update_item_name_table(new_name, code)
            if updatetable == True:
                self.mainwindow.setEnabled(False)
                self.msg_box = QMessageBox(self.mainwindow)
                self.msg_box.setWindowTitle('Edited')
                self.msg_box.setIcon(QMessageBox.Information)
                self.msg_box.setText('item name edited')
                self.msg_box.setStandardButtons(QMessageBox.Ok)
                self.msg_box.exec_()
                self.mainwindow.setEnabled(True)
                self.add_item_frame()
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

    #   Save new item
    def save_newitem(self):
        itemname = self.lineEdit_3.text()
        mastercode = self.lineEdit_2.text()
        if itemname and mastercode:
            savenew = main_category_database().save_new_main_category(itemname, mastercode)
            if savenew == True:
                self.mainwindow.setEnabled(False)
                self.msg_box = QMessageBox(self.mainwindow)
                self.msg_box.setWindowTitle('Saved')
                self.msg_box.setIcon(QMessageBox.Information)
                self.msg_box.setText('New item saved')
                self.msg_box.setStandardButtons(QMessageBox.Ok)
                self.msg_box.exec_()
                self.mainwindow.setEnabled(True)
                self.add_item_frame()
            elif savenew == False:
                self.mainwindow.setEnabled(False)
                self.msg_box = QMessageBox(self.mainwindow)
                self.msg_box.setWindowTitle('Error')
                self.msg_box.setIcon(QMessageBox.Critical)
                self.msg_box.setText('Contact admin, database connection lost')
                self.msg_box.setStandardButtons(QMessageBox.Ok)
                self.msg_box.exec_()
                self.mainwindow.setEnabled(True)
        else:
            self.mainwindow.setEnabled(False)
            self.msg_box = QMessageBox(self.mainwindow)
            self.msg_box.setWindowTitle('Empty')
            self.msg_box.setIcon(QMessageBox.Critical)
            self.msg_box.setText('item name & master id required')
            self.msg_box.setStandardButtons(QMessageBox.Ok)
            self.msg_box.exec_()
            self.mainwindow.setEnabled(True)


