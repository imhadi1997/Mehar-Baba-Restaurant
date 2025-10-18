from PyQt5 import QtCore, QtGui, QtWidgets
from database import add_item_database
from PyQt5.QtWidgets import QMessageBox
from PyQt5.QtWidgets import QHeaderView
from close import main_page

class item_category_class:
    #   init
    def __init__(self, centralwidget, username , usertype, mainwindow, userid):
        self.centralwidget = centralwidget
        self.username = username
        self.usertype = usertype
        self.mainwindow = mainwindow
        self.userid = userid
        

    #   item category frame
    def item_category_frame(self):
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

        self.lineEdit_5 = QtWidgets.QLineEdit(self.widget)
        self.lineEdit_5.setGeometry(QtCore.QRect(100, 100, 191, 21))
        self.lineEdit_5.setStyleSheet("background-color: rgb(255, 255, 255);\n"
        "color: rgb(0, 0, 0);\n"
        "font: 8pt \"MS Shell Dlg 2\";\n"
        "border : 1px solid black;")
        self.lineEdit_5.setPlaceholderText("Only int value")
        self.lineEdit_5.setCursorMoveStyle(QtCore.Qt.LogicalMoveStyle)
        self.lineEdit_5.setClearButtonEnabled(False)
        self.lineEdit_5.setObjectName("lineEdit_4")
        self.lineEdit_5.show()

        int_validator = QtGui.QIntValidator(0, 999999)  # (min, max) range; use any range you want
        self.lineEdit_5.setValidator(int_validator)


        self.pushButton = QtWidgets.QPushButton(self.widget)
        self.pushButton.setGeometry(QtCore.QRect(100, 130, 75, 23))
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
        self.pushButton_2.setGeometry(QtCore.QRect(190, 130, 75, 23))
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
        self.tableView.setGeometry(QtCore.QRect(310, 10, 691, 441))
        self.tableView.setStyleSheet("font: 8pt \"MS Shell Dlg 2\";\n"
        "background-color: rgb(255, 255, 255);\n"
        "color: rgb(0, 0, 0);\n"
        "")
        self.tableView.setGridStyle(QtCore.Qt.SolidLine)
        self.tableView.setObjectName("tableView")
        self.tableView.show()

        self.label_2 = QtWidgets.QLabel(self.widget)
        self.label_2.setGeometry(QtCore.QRect(30, 40, 81, 21))
        self.label_2.setStyleSheet("border : 0px;")
        self.label_2.setObjectName("label_2")
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

        self.label_5 = QtWidgets.QLabel(self.widget)
        self.label_5.setGeometry(QtCore.QRect(10, 100, 81, 21))
        self.label_5.setStyleSheet("border : 0px;")
        self.label_5.setObjectName("label_4")
        self.label_5.show()

        self.label_4 = QtWidgets.QLabel(self.widget)
        self.label_4.setGeometry(QtCore.QRect(10, 10, 81, 21))
        self.label_4.setStyleSheet("border : 0px;")
        self.label_4.setObjectName("label_4")
        self.label_4.show()

        self.lineEdit.setFocus()

        _translate = QtCore.QCoreApplication.translate
        self.pushButton.setText(_translate("MainWindow", "Save"))
        self.pushButton_2.setText(_translate("MainWindow", "Close"))
        self.label_2.setText(_translate("MainWindow", "  item id :"))
        self.lineEdit_2.setPlaceholderText(_translate("MainWindow", "item id"))
        self.label_3.setText(_translate("MainWindow", "    type of item :"))
        self.label_4.setText(_translate("MainWindow", "     item Name :"))
        self.label_5.setText(_translate("MainWindow", "      Sale Price :"))
        

        master_input_dict = {}
        item_input_dict = {}
        model = QtGui.QStandardItemModel()
        model.setHorizontalHeaderLabels(["Code", "Master", "item", "types of item", "Sale Price"])
        checkdata = add_item_database().existing_add_new_item()
        if checkdata == [] or checkdata != []:
            for row in checkdata:
                code_item = QtGui.QStandardItem(str(row[1]))
                code_item.setFlags(code_item.flags() & ~QtCore.Qt.ItemIsEditable)

                item_id = QtGui.QStandardItem(str(row[2]))
                item_id.setFlags(code_item.flags() & ~QtCore.Qt.ItemIsEditable)
                item_name = QtGui.QStandardItem(str(row[5]))
                item_name.setFlags(code_item.flags() & ~QtCore.Qt.ItemIsEditable)

                master_input = QtGui.QStandardItem(str(row[6]))
                master_input.setFlags(code_item.flags() & ~QtCore.Qt.ItemIsEditable)

                master_name = QtGui.QStandardItem(str(row[7])) 
                master_name.setFlags(code_item.flags() & ~QtCore.Qt.ItemIsEditable)

                itemcategoryname = QtGui.QStandardItem(str(row[3]))
                itemsaleprice = QtGui.QStandardItem(str(row[4]))

                item_input_dict[str(row[5])] = str(row[1])
                master_input_dict[str(row[7])] = str(row[6])
                model.appendRow([code_item, master_name, item_name, itemcategoryname, itemsaleprice])
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
        self.tableView.setColumnWidth(0, 80)   # Code column width
        self.tableView.setColumnWidth(1, 120)   # Name column width
        self.tableView.setColumnWidth(2, 150)
        self.tableView.setColumnWidth(3, 200)
        self.tableView.setColumnWidth(4, 80)
        header = self.tableView.horizontalHeader()
        header.setSectionResizeMode(QHeaderView.Fixed)
        model.itemChanged.connect(self.on_item_changed)

        def block_leading_zero(text):
            if text.startswith("0") and len(text) > 1:
                # Remove leading zero
                self.lineEdit_5.setText(text.lstrip("0"))

        self.lineEdit_5.textChanged.connect(block_leading_zero)
        self.pushButton_2.clicked.connect(lambda: self.close_button())
        self.pushButton.clicked.connect(self.save_new_item_type)

        self.completer_model = QtCore.QStringListModel()
        self.completer_model.setStringList(list(item_input_dict.keys()))
        
        self.completer = QtWidgets.QCompleter(self.completer_model)
        self.completer.setCaseSensitivity(QtCore.Qt.CaseInsensitive)
        self.completer.setFilterMode(QtCore.Qt.MatchContains)
        self.lineEdit.setCompleter(self.completer)

        def on_completer_activated(text):
            self.lineEdit.setText(text)
            self.lineEdit_2.setText(item_input_dict[text])
        
        def on_lineedit_text_changed(text):
            if text == "":
                self.lineEdit_2.clear()

        self.completer.activated[str].connect(on_completer_activated)
        self.lineEdit.textChanged.connect(on_lineedit_text_changed)

        self.pushButton_2.setDefault(True)
        self.pushButton.setDefault(True)

    
    #   Close to Main Window
    def close_button(self):
        main_page(self.centralwidget, self.username, self.usertype).close_function()


    #   Edit Item Name
    def on_item_changed(self, item):
        row = item.row()
        col = item.column()

        # Only handle edits in the "Name" column (index 1)
        if col == 3:
            new_name = item.text()
            code = self.tableView.model().item(row, 0).text()
            changeitemname = add_item_database().edit_type_of_item_table(new_name, code)
            if changeitemname == True:
                self.mainwindow.setEnabled(False)
                self.msg_box = QMessageBox(self.mainwindow)
                self.msg_box.setWindowTitle('Edited')
                self.msg_box.setIcon(QMessageBox.Information)
                self.msg_box.setText('type of item edited')
                self.msg_box.setStandardButtons(QMessageBox.Ok)
                self.msg_box.exec_()
                self.mainwindow.setEnabled(True)
                self.item_category_frame()
            elif changeitemname == False:
                self.mainwindow.setEnabled(False)
                self.msg_box = QMessageBox(self.mainwindow)
                self.msg_box.setWindowTitle('Error')
                self.msg_box.setIcon(QMessageBox.Critical)
                self.msg_box.setText('Contact admin, database connection lost')
                self.msg_box.setStandardButtons(QMessageBox.Ok)
                self.msg_box.exec_()
                self.mainwindow.setEnabled(True)
        
        elif col == 4:
            new_name = item.text()
            code = self.tableView.model().item(row, 0).text()
            if not new_name.isdigit():
                self.mainwindow.setEnabled(False)
                self.msg_box = QMessageBox(self.mainwindow)
                self.msg_box.setWindowTitle('Error')
                self.msg_box.setIcon(QMessageBox.Critical)
                self.msg_box.setText('Only int value')
                self.msg_box.setStandardButtons(QMessageBox.Ok)
                self.msg_box.exec_()
                self.mainwindow.setEnabled(True)
            else:
                if new_name.startswith('0') and len(new_name) > 1:
                    new_value = str(int(new_name))
                else:
                    new_value = new_name
                changesaleprice = add_item_database().edit_item_sale_price_table(new_value, code)
                if changesaleprice == True:
                    self.mainwindow.setEnabled(False)
                    self.msg_box = QMessageBox(self.mainwindow)
                    self.msg_box.setWindowTitle('Edited')
                    self.msg_box.setIcon(QMessageBox.Information)
                    self.msg_box.setText('item sale price edited')
                    self.msg_box.setStandardButtons(QMessageBox.Ok)
                    self.msg_box.exec_()
                    self.mainwindow.setEnabled(True)
                    self.item_category_frame()
                elif changesaleprice == False:
                    self.mainwindow.setEnabled(False)
                    self.msg_box = QMessageBox(self.mainwindow)
                    self.msg_box.setWindowTitle('Error')
                    self.msg_box.setIcon(QMessageBox.Critical)
                    self.msg_box.setText('Contact admin, database connection lost')
                    self.msg_box.setStandardButtons(QMessageBox.Ok)
                    self.msg_box.exec_()
                    self.mainwindow.setEnabled(True)

    #   Save New item
    def save_new_item_type(self):
        newtypename = self.lineEdit_3.text()
        mainitemcode = self.lineEdit_2.text()
        saleprice = self.lineEdit_5.text()
        if newtypename and mainitemcode and saleprice:
            savenew = add_item_database().save_new_item_type_table(newtypename, mainitemcode, saleprice)
            if savenew == True:
                self.mainwindow.setEnabled(False)
                self.msg_box = QMessageBox(self.mainwindow)
                self.msg_box.setWindowTitle('Saved')
                self.msg_box.setIcon(QMessageBox.Information)
                self.msg_box.setText('New type of item saved')
                self.msg_box.setStandardButtons(QMessageBox.Ok)
                self.msg_box.exec_()
                self.mainwindow.setEnabled(True)
                self.item_category_frame()
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
            self.msg_box.setText('type of item, item id & sale price required')
            self.msg_box.setStandardButtons(QMessageBox.Ok)
            self.msg_box.exec_()
            self.mainwindow.setEnabled(True)

    #Enter key
    def keyPressEvent(self, event):
        if event.key() in (QtCore.Qt.Key_Return, QtCore.Qt.Key_Enter):
            focus_widget = self.focusWidget()
            if isinstance(focus_widget, QtWidgets.QPushButton):
                focus_widget.click()