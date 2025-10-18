from PyQt5 import QtCore, QtGui, QtWidgets
from database import add_item_database
from PyQt5.QtWidgets import QMessageBox
from PyQt5.QtWidgets import QHeaderView
from collections import defaultdict
from PyQt5.QtWidgets import QAbstractItemView
from close import main_page

class main_menu_of_item_class:
    #   init
    def __init__(self, centralwidget, username , usertype, mainwindow, userid):
        self.centralwidget = centralwidget
        self.username = username
        self.usertype = usertype
        self.mainwindow = mainwindow
        self.userid = userid
        
    #   Main Menu Frame
    def main_menu_items_frame(self):
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
        self.lineEdit.setGeometry(QtCore.QRect(80, 10, 191, 21))
        self.lineEdit.setStyleSheet("background-color: rgb(255, 255, 255);\n"
        "color: rgb(0, 0, 0);\n"
        "font: 8pt \"MS Shell Dlg 2\";\n"
        "border : 1px solid black;")
        self.lineEdit.setPlaceholderText("")
        self.lineEdit.setCursorMoveStyle(QtCore.Qt.LogicalMoveStyle)
        self.lineEdit.setClearButtonEnabled(False)
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit.show()

        self.pushButton = QtWidgets.QPushButton(self.widget)
        self.pushButton.setGeometry(QtCore.QRect(280, 10, 75, 23))
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
        icon.addPixmap(QtGui.QPixmap("images/refresh.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton.setIcon(icon)
        self.pushButton.setObjectName("pushButton")
        self.pushButton.show()

        self.pushButton_2 = QtWidgets.QPushButton(self.widget)
        self.pushButton_2.setGeometry(QtCore.QRect(370, 10, 75, 23))
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
        self.tableView.setGeometry(QtCore.QRect(10, 40, 675, 411))
        self.tableView.setStyleSheet("font: 8pt \"MS Shell Dlg 2\";\n"
        "background-color: rgb(255, 255, 255);\n"
        "color: rgb(0, 0, 0);\n"
        "")
        self.tableView.setGridStyle(QtCore.Qt.SolidLine)
        self.tableView.setObjectName("tableView")
        self.tableView.show()

        self.label_4 = QtWidgets.QLabel(self.widget)
        self.label_4.setGeometry(QtCore.QRect(20, 10, 51, 21))
        self.label_4.setStyleSheet("border : 0px;")
        self.label_4.setObjectName("label_4")
        self.label_4.show()

        self.label = QtWidgets.QLabel(self.widget)
        self.label.setGeometry(QtCore.QRect(700, 80, 271, 300))
        self.label.setStyleSheet("border : 0px;")
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("images/Logo MB 02 (1).PNG"))
        self.label.setScaledContents(True)
        self.label.setObjectName("label")
        self.label.show()

        _translate = QtCore.QCoreApplication.translate
        self.pushButton.setText(_translate("MainWindow", "Search"))
        self.pushButton_2.setText(_translate("MainWindow", "Close"))
        self.label_4.setText(_translate("MainWindow", "    Search :"))

        self.lineEdit.setFocus()

        master_input_dict = {}
        item_input_dict = {}
        model = QtGui.QStandardItemModel()
        model.setHorizontalHeaderLabels(["Code", "Master", "item", "Sale Price"])
        checkdata = add_item_database().existing_add_new_item()
        if checkdata == [] or checkdata != []:
            # Group rows by master ID (row[6] in your structure)
            grouped = defaultdict(list)
            for row in checkdata:
                grouped[row[6]].append(row)

            for master_id, rows in grouped.items():

                # (1) INSERT HEADER/BLANK ROW SHOWING MASTER NAME
                header_code    = QtGui.QStandardItem("")     # Code empty
                header_master  = QtGui.QStandardItem(str(master_id)+ " - " + str(rows[0][7]))  # Master name
                header_item    = QtGui.QStandardItem("")     # rest empty
                header_price   = QtGui.QStandardItem("")

                # Lock them to be not editable
                for cell in [header_code, header_master, header_item, header_price]:
                    cell.setFlags(cell.flags() & ~QtCore.Qt.ItemIsEditable)

                model.appendRow([header_code, header_master, header_item, header_price])

                # (2) INSERT ALL ITEMS BELONGING TO THIS MASTER
                for row in rows:
                    code_item   = QtGui.QStandardItem(str(row[1]))
                    code_item.setFlags(code_item.flags() & ~QtCore.Qt.ItemIsEditable)

                    item_id     = QtGui.QStandardItem(str(row[2]))
                    item_id.setFlags(code_item.flags() & ~QtCore.Qt.ItemIsEditable)

                    item_name   = QtGui.QStandardItem(str(row[5]))
                    item_name.setFlags(code_item.flags() & ~QtCore.Qt.ItemIsEditable)

                    item_cat    = QtGui.QStandardItem(str(row[3]))
                    item_cat.setFlags(code_item.flags() & ~QtCore.Qt.ItemIsEditable)

                    sale_price  = QtGui.QStandardItem(str(row[4]))
                    # allow editing only sale price (col 4)
                    sale_price.setFlags(code_item.flags() & ~QtCore.Qt.ItemIsEditable)

                    master_input_dict[str(row[7])] = str(row[6])

                    fullname_text = str(item_name.text()) + " " + str(item_cat.text())
                    fullname_item = QtGui.QStandardItem(fullname_text)
                    fullname_item.setFlags(code_item.flags() & ~QtCore.Qt.ItemIsEditable)

                    empty_text = ""
                    emptytext_item = QtGui.QStandardItem(empty_text)
                    emptytext_item.setFlags(code_item.flags() & ~QtCore.Qt.ItemIsEditable)

                    model.appendRow([code_item, emptytext_item, fullname_item, sale_price])

                    item_input_dict[str(fullname_text)]   = str(row[1])

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
        self.tableView.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.tableView.setColumnWidth(0, 80)   # Code column width
        self.tableView.setColumnWidth(1, 120)   # Name column width
        self.tableView.setColumnWidth(2, 350)
        self.tableView.setColumnWidth(3, 80)
        header = self.tableView.horizontalHeader()
        header.setSectionResizeMode(QHeaderView.Fixed)

        self.completer_model = QtCore.QStringListModel()
        self.completer_model.setStringList(list(item_input_dict.keys()))
        
        self.completer = QtWidgets.QCompleter(self.completer_model)
        self.completer.setCaseSensitivity(QtCore.Qt.CaseInsensitive)
        self.completer.setFilterMode(QtCore.Qt.MatchContains)
        self.lineEdit.setCompleter(self.completer)

        def on_completer_activated(text):
            self.lineEdit.setText(text)
            self.lineEdit.setText(item_input_dict[text])

            for row in range(model.rowCount()):
                index = model.index(row, 2)  # assuming "item name" is in column 2
                if index.data() == text:
                    # Select that row in the table
                    self.tableView.selectRow(row)
                    break

        def on_pushButton_clicked():
            code = self.lineEdit.text()  # what the user typed (item code)
            
            # Loop through all rows, check column 0 ("Code")
            for row in range(model.rowCount()):
                index = model.index(row, 0)  # column 0 is the "Code" column
                if index.data() == code:
                    self.tableView.selectRow(row)             # highlight row
                    self.tableView.scrollTo(index)            # (optional) scroll to it
                    break
                else:
                    self.mainwindow.setEnabled(False)
                    self.msg_box = QMessageBox(self.mainwindow)
                    self.msg_box.setWindowTitle('item code')
                    self.msg_box.setIcon(QMessageBox.Critical)
                    self.msg_box.setText('No match found')
                    self.msg_box.setStandardButtons(QMessageBox.Ok)
                    self.msg_box.exec_()
                    self.mainwindow.setEnabled(True)


        self.completer.activated[str].connect(on_completer_activated)
        self.pushButton.clicked.connect(on_pushButton_clicked)
        self.pushButton_2.clicked.connect(lambda: self.close_button())

        self.pushButton_2.setDefault(True)
        self.pushButton.setDefault(True)

    #   Close to Main Window
    def close_button(self):
        main_page(self.centralwidget, self.username, self.usertype).close_function()

    
    #Enter key
    def keyPressEvent(self, event):
        if event.key() in (QtCore.Qt.Key_Return, QtCore.Qt.Key_Enter):
            focus_widget = self.focusWidget()
            if isinstance(focus_widget, QtWidgets.QPushButton):
                focus_widget.click()

