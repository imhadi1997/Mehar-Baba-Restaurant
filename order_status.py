from PyQt5 import QtCore, QtGui, QtWidgets
from database import add_item_database
from PyQt5.QtWidgets import QMessageBox
from PyQt5.QtWidgets import QHeaderView
from collections import defaultdict
from PyQt5.QtWidgets import QAbstractItemView
from close import main_page
from PyQt5.QtWidgets import QStyledItemDelegate, QPushButton, QApplication
from PyQt5.QtCore import Qt, QRect, pyqtSignal
from database import order_database



class punch_order_status:
    #   init
    def __init__(self, centralwidget, username , usertype, mainwindow, userid):
        self.centralwidget = centralwidget
        self.username = username
        self.usertype = usertype
        self.mainwindow = mainwindow
        self.userid = userid

    #   puch Order Frame
    def punched_order_frame(self):
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(0, 80, 1131, 571))
        self.frame.setStyleSheet("background-color: rgb(255, 255, 204);\n"
        "border-style: groove;")
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

        self.label_5 = QtWidgets.QLabel(self.widget)
        self.label_5.setGeometry(QtCore.QRect(20, 10, 61, 21))
        self.label_5.setStyleSheet("border : 0px;")
        self.label_5.setObjectName("label_5")
        self.label_5.show()

        self.lineEdit_2 = QtWidgets.QLineEdit(self.widget)
        self.lineEdit_2.setGeometry(QtCore.QRect(90, 10, 191, 21))
        self.lineEdit_2.setStyleSheet("background-color: rgb(255, 255, 255);\n"
        "color: rgb(0, 0, 0);\n"
        "font: 8pt \"MS Shell Dlg 2\";\n"
        "border : 1px solid black;")
        self.lineEdit_2.setReadOnly(True)
        self.lineEdit_2.setPlaceholderText("")
        self.lineEdit_2.setCursorMoveStyle(QtCore.Qt.LogicalMoveStyle)
        self.lineEdit_2.setClearButtonEnabled(False)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.lineEdit_2.show()

        self.lineEdit_8 = QtWidgets.QLineEdit(self.widget)
        self.lineEdit_8.setGeometry(QtCore.QRect(710, 20, 191, 21))
        self.lineEdit_8.setStyleSheet("background-color: rgb(255, 255, 255);\n"
        "color: rgb(0, 0, 0);\n"
        "font: 8pt \"MS Shell Dlg 2\";\n"
        "border : 1px solid black;")
        self.lineEdit_8.setPlaceholderText("")
        self.lineEdit_8.setCursorMoveStyle(QtCore.Qt.LogicalMoveStyle)
        self.lineEdit_8.setClearButtonEnabled(False)
        self.lineEdit_8.setObjectName("lineEdit_8")
        self.lineEdit_8.show()
        self.lineEdit_8.setFocus()

        self.label_11 = QtWidgets.QLabel(self.widget)
        self.label_11.setGeometry(QtCore.QRect(625, 20, 81, 21))
        self.label_11.setStyleSheet("border : 0px;")
        self.label_11.setObjectName("label_11")
        self.label_11.show()

        self.lineEdit = QtWidgets.QLineEdit(self.widget)
        self.lineEdit.setGeometry(QtCore.QRect(710, 50, 191, 21))
        self.lineEdit.setStyleSheet("background-color: rgb(255, 255, 255);\n"
        "color: rgb(0, 0, 0);\n"
        "font: 8pt \"MS Shell Dlg 2\";\n"
        "border : 1px solid black;")
        self.lineEdit.setPlaceholderText("")
        self.lineEdit.setCursorMoveStyle(QtCore.Qt.LogicalMoveStyle)
        self.lineEdit.setClearButtonEnabled(False)
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit.show()

        self.lineEdit_6 = QtWidgets.QLineEdit(self.widget)
        self.lineEdit_6.setGeometry(QtCore.QRect(710, 200, 191, 21))
        self.lineEdit_6.setStyleSheet("background-color: rgb(255, 255, 255);\n"
        "color: rgb(0, 0, 0);\n"
        "font: 8pt \"MS Shell Dlg 2\";\n"
        "border : 1px solid black;")
        self.lineEdit_6.setPlaceholderText("Only int value")
        self.lineEdit_6.setCursorMoveStyle(QtCore.Qt.LogicalMoveStyle)
        self.lineEdit_6.setClearButtonEnabled(False)
        self.lineEdit_6.setObjectName("lineEdit_6")
        self.lineEdit_6.show()
        int_validator = QtGui.QIntValidator(0, 999999)  # (min, max) range; use any range you want
        self.lineEdit_6.setValidator(int_validator)

        self.pushButton_3 = QtWidgets.QPushButton(self.widget)
        self.pushButton_3.setGeometry(QtCore.QRect(720, 230, 75, 23))
        self.pushButton_3.setStyleSheet("QPushButton {\n"
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
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("images/add_icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_3.setIcon(icon2)
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_3.show()

        self.pushButton_4 = QtWidgets.QPushButton(self.widget)
        self.pushButton_4.setGeometry(QtCore.QRect(810, 230, 75, 23))
        self.pushButton_4.setStyleSheet("QPushButton {\n"
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
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap("images/refresh.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_4.setIcon(icon3)
        self.pushButton_4.setObjectName("pushButton_4")
        self.pushButton_4.show()

        self.pushButton_2 = QtWidgets.QPushButton(self.widget)
        self.pushButton_2.setGeometry(QtCore.QRect(630, 380, 75, 23))
        self.pushButton_2.setStyleSheet("QPushButton {\n"
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
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("images/delete-sign.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_2.setIcon(icon1)
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_2.show()

        self.label_4 = QtWidgets.QLabel(self.widget)
        self.label_4.setGeometry(QtCore.QRect(640, 50, 51, 21))
        self.label_4.setStyleSheet("border : 0px;")
        self.label_4.setObjectName("label_4")
        self.label_4.show()

        self.label_6 = QtWidgets.QLabel(self.widget)
        self.label_6.setGeometry(QtCore.QRect(630, 110, 71, 21))
        self.label_6.setStyleSheet("border : 0px;")
        self.label_6.setObjectName("label_6")
        self.label_6.show()

        self.lineEdit_3 = QtWidgets.QLineEdit(self.widget)
        self.lineEdit_3.setGeometry(QtCore.QRect(710, 80, 191, 21))
        self.lineEdit_3.setStyleSheet("background-color: rgb(255, 255, 255);\n"
        "color: rgb(0, 0, 0);\n"
        "font: 8pt \"MS Shell Dlg 2\";\n"
        "border : 1px solid black;")
        self.lineEdit_3.setReadOnly(True)
        self.lineEdit_3.setPlaceholderText("")
        self.lineEdit_3.setCursorMoveStyle(QtCore.Qt.LogicalMoveStyle)
        self.lineEdit_3.setClearButtonEnabled(False)
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.lineEdit_3.show()

        self.lineEdit_4 = QtWidgets.QLineEdit(self.widget)
        self.lineEdit_4.setGeometry(QtCore.QRect(710, 110, 191, 21))
        self.lineEdit_4.setStyleSheet("background-color: rgb(255, 255, 255);\n"
        "color: rgb(0, 0, 0);\n"
        "font: 8pt \"MS Shell Dlg 2\";\n"
        "border : 1px solid black;")
        self.lineEdit_4.setReadOnly(True)
        self.lineEdit_4.setPlaceholderText("")
        self.lineEdit_4.setCursorMoveStyle(QtCore.Qt.LogicalMoveStyle)
        self.lineEdit_4.setClearButtonEnabled(False)
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.lineEdit_4.show()

        self.label_7 = QtWidgets.QLabel(self.widget)
        self.label_7.setGeometry(QtCore.QRect(630, 140, 71, 21))
        self.label_7.setStyleSheet("border : 0px;")
        self.label_7.setObjectName("label_7")
        self.label_7.show()

        self.label_8 = QtWidgets.QLabel(self.widget)
        self.label_8.setGeometry(QtCore.QRect(627, 200, 81, 21))
        self.label_8.setStyleSheet("border : 0px;")
        self.label_8.setObjectName("label_8")
        self.label_8.show()

        self.label_9 = QtWidgets.QLabel(self.widget)
        self.label_9.setGeometry(QtCore.QRect(630, 80, 71, 21))
        self.label_9.setStyleSheet("border : 0px;")
        self.label_9.setObjectName("label_9")
        self.label_9.show()

        self.label_10 = QtWidgets.QLabel(self.widget)
        self.label_10.setGeometry(QtCore.QRect(628, 170, 81, 21))
        self.label_10.setStyleSheet("border : 0px;")
        self.label_10.setObjectName("label_10")
        self.label_10.show()

        self.lineEdit_5 = QtWidgets.QLineEdit(self.widget)
        self.lineEdit_5.setGeometry(QtCore.QRect(710, 140, 191, 21))
        self.lineEdit_5.setStyleSheet("background-color: rgb(255, 255, 255);\n"
        "color: rgb(0, 0, 0);\n"
        "font: 8pt \"MS Shell Dlg 2\";\n"
        "border : 1px solid black;")
        self.lineEdit_5.setReadOnly(True)
        self.lineEdit_5.setPlaceholderText("")
        self.lineEdit_5.setCursorMoveStyle(QtCore.Qt.LogicalMoveStyle)
        self.lineEdit_5.setClearButtonEnabled(False)
        self.lineEdit_5.setObjectName("lineEdit_5")
        self.lineEdit_5.show()

        self.lcdNumber = QtWidgets.QLCDNumber(self.widget)
        self.lcdNumber.setGeometry(QtCore.QRect(860, 390, 141, 61))
        self.lcdNumber.setStyleSheet("border : 0px;\n"
        "background-color: rgb(29, 29, 29);\n"
        "color: rgb(85, 255, 0);;")
        self.lcdNumber.setSmallDecimalPoint(False)
        self.lcdNumber.setDigitCount(7)
        self.lcdNumber.setMode(QtWidgets.QLCDNumber.Dec)
        self.lcdNumber.setObjectName("lcdNumber")
        self.lcdNumber.show()

        self.label = QtWidgets.QLabel(self.widget)
        self.label.setGeometry(QtCore.QRect(770, 400, 81, 41))
        self.label.setStyleSheet("font: 10 10pt \"MS Shell Dlg 2\";\n"
        "border : 0px;")
        self.label.setObjectName("label")
        self.label.show()

        self.lineEdit_7 = QtWidgets.QLineEdit(self.widget)
        self.lineEdit_7.setGeometry(QtCore.QRect(710, 170, 191, 21))
        self.lineEdit_7.setStyleSheet("background-color: rgb(255, 255, 255);\n"
        "color: rgb(0, 0, 0);\n"
        "font: 8pt \"MS Shell Dlg 2\";\n"
        "border : 1px solid black;")
        self.lineEdit_7.setReadOnly(True)
        self.lineEdit_7.setCursorMoveStyle(QtCore.Qt.LogicalMoveStyle)
        self.lineEdit_7.setClearButtonEnabled(False)
        self.lineEdit_7.setObjectName("lineEdit_7")
        self.lineEdit_7.show()

        self.plainTextEdit = QtWidgets.QPlainTextEdit(self.widget)
        self.plainTextEdit.setGeometry(QtCore.QRect(10, 40, 611, 111))
        self.plainTextEdit.setReadOnly(True)
        self.plainTextEdit.setObjectName("plainTextEdit")
        font = QtGui.QFont("Courier New", 10)  # Or "Consolas", "Monospace"
        font.setPointSize(8)
        self.plainTextEdit.setFont(font)

        self.tableView = QtWidgets.QTableView(self.widget)
        self.tableView.setGeometry(QtCore.QRect(10, 160, 611, 291))
        self.tableView.setStyleSheet("font: 8pt \"MS Shell Dlg 2\";\n"
        "background-color: rgb(255, 255, 255);\n"
        "color: rgb(0, 0, 0);\n"
        "")
        self.tableView.setGridStyle(QtCore.Qt.SolidLine)
        self.tableView.setObjectName("tableView")
        self.tableView.show()

        self.label_5 = QtWidgets.QLabel(self.widget)
        self.label_5.setGeometry(QtCore.QRect(20, 10, 61, 21))
        self.label_5.setStyleSheet("border : 0px;")
        self.label_5.setObjectName("label_5")
        self.label_5.show()

        # Set the content
        self.plainTextEdit.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.plainTextEdit.setFocusPolicy(QtCore.Qt.NoFocus)
        self.plainTextEdit.show()


        item_input_dict = {}
        model = QtGui.QStandardItemModel()
        model.setHorizontalHeaderLabels(["Code", "item name","Sale Price", "Qty", "Total", "Action"])
        checkdata = order_database().all_unpaid_order(False, False)
        if checkdata == [] or checkdata != []:
            if checkdata == [] or checkdata != []:
                for row in checkdata:
                    item_input_dict[str(row[1])] = [str(row[3])+"/"+str(row[4]), str(row[10])]
            elif checkdata == False:
                self.mainwindow.setEnabled(False)
                self.msg_box = QMessageBox(self.mainwindow)
                self.msg_box.setWindowTitle('Error')
                self.msg_box.setIcon(QMessageBox.Critical)
                self.msg_box.setText('Contact admin, database connection lost')
                self.msg_box.setStandardButtons(QMessageBox.Ok)
                self.msg_box.exec_()
                self.mainwindow.setEnabled(True)

        self.completer_model = QtCore.QStringListModel()
        self.completer_model.setStringList(list(item_input_dict.keys()))
        
        self.completer = QtWidgets.QCompleter(self.completer_model)
        self.completer.setCaseSensitivity(QtCore.Qt.CaseInsensitive)
        self.completer.setFilterMode(QtCore.Qt.MatchContains)
        self.lineEdit_8.setCompleter(self.completer)

        def on_completer_activated(text):
            orderdetails = order_database().order_details_database(text)
            if orderdetails == False:
                self.mainwindow.setEnabled(False)
                self.msg_box = QMessageBox(self.mainwindow)
                self.msg_box.setWindowTitle('Error')
                self.msg_box.setIcon(QMessageBox.Critical)
                self.msg_box.setText('Contact admin, database connection lost')
                self.msg_box.setStandardButtons(QMessageBox.Ok)
                self.msg_box.exec_()
                self.mainwindow.setEnabled(True)
            else:
                self.table_model.removeRows(0, self.table_model.rowCount())
                self.lineEdit_8.setText(text)
                dict_values = item_input_dict[text]
                self.lineEdit_2.setText(text)
                text = """\
                            Mehar Baba Restaurant
        Baba Paghaa Wala Rajowal Joriya Mehar Toll Plaza Depallpur, Okara
                            Contact: 0333-4553258
    =========================================================================
    added Date/Time: """+str(dict_values[0]) + """\t     add by: """ + str(dict_values[1])
                self.plainTextEdit.setPlainText(text)
                for row in orderdetails:
                    codeno = QtGui.QStandardItem(str(row[2]))
                    codeno.setFlags(codeno.flags() & ~QtCore.Qt.ItemIsEditable)
                    itemname = QtGui.QStandardItem(str(row[7]))
                    itemname.setFlags(itemname.flags() & ~QtCore.Qt.ItemIsEditable)
                    itemprice = QtGui.QStandardItem(str(row[3]))
                    itemprice.setFlags(itemprice.flags() & ~QtCore.Qt.ItemIsEditable)
                    itemqty = QtGui.QStandardItem(str(row[4]))
                    itemqty.setFlags(itemqty.flags() | QtCore.Qt.ItemIsEditable)

                    total = int(row[3]) * int(row[4])
                    itemtotal = QtGui.QStandardItem(str(total))
                    itemtotal.setFlags(itemtotal.flags() & ~QtCore.Qt.ItemIsEditable)

                    remove_button_item = QtGui.QStandardItem("Remove")
                    remove_button_item.setFlags(remove_button_item.flags() & ~QtCore.Qt.ItemIsEditable)

                    model.appendRow([codeno, itemname, itemprice, itemqty, itemtotal, remove_button_item])

                self.lineEdit.setFocus()
                self.update_grand_total()

        self.completer.activated[str].connect(on_completer_activated)

        self.tableView.setModel(model)
        self.table_model = model  # Save reference for reuse in Add function
        self.tableView.setColumnWidth(0, 60)   # Code column width
        self.tableView.setColumnWidth(1, 230)
        self.tableView.setColumnWidth(2, 70)
        self.tableView.setColumnWidth(3, 70)
        self.tableView.setColumnWidth(4, 70)
        self.tableView.setColumnWidth(5, 90)
        header = self.tableView.horizontalHeader()
        header.setSectionResizeMode(QHeaderView.Fixed)

        model.itemChanged.connect(self.on_item_changed)
        self.tableView.clicked.connect(self.handle_table_click)
        self.button_delegate = ButtonDelegate(self.tableView)
        self.tableView.setItemDelegateForColumn(5, self.button_delegate)

        # Connect the delegate's clicked signal
        self.button_delegate.clicked.connect(self.handle_table_click)










        _translate = QtCore.QCoreApplication.translate
        self.label_5.setText(_translate("MainWindow", "    Order No :"))
        self.label_4.setText(_translate("MainWindow", "    Search :"))
        self.label_6.setText(_translate("MainWindow", "    item Code :"))
        self.label_7.setText(_translate("MainWindow", "    item Name :"))
        self.label_8.setText(_translate("MainWindow", "      Quantity :"))
        self.label_9.setText(_translate("MainWindow", "   Master level :"))
        self.label_10.setText(_translate("MainWindow", "     Sale Price :"))
        self.label_11.setText(_translate("MainWindow", "Search Order :"))
        self.label.setText(_translate("MainWindow", "Grand Total :"))
        self.lineEdit_7.setPlaceholderText(_translate("MainWindow", "0"))
        self.pushButton_2.setText(_translate("MainWindow", "Close"))
        self.pushButton_3.setText(_translate("MainWindow", "Add"))
        self.pushButton_4.setText(_translate("MainWindow", "Clear"))
        
        self.pushButton_2.clicked.connect(lambda: self.close_button())

        

        
    #   Close to Main Window
    def close_button(self):
        main_page(self.centralwidget, self.username, self.usertype).close_function()



    #   Remove From cart
    def handle_table_click(self, index):
        row = index.row()
        col = index.column()

        # Assuming "Remove" is in column 5
        if col == 5:
            self.table_model.removeRow(row)
            self.lineEdit.setFocus()
            self.update_grand_total()

    #   Grand Total update
    def update_grand_total(self):
        total = 0
        for row in range(self.table_model.rowCount()):
            item = self.table_model.item(row, 4)  # Total column
            if item:
                try:
                    total += float(item.text())
                except ValueError:
                    continue
        self.lcdNumber.display(total)

    #   Change Qty
    def on_item_changed(self, item):
        row = item.row()
        col = item.column()

        if col == 3:
            quantity_item = self.table_model.item(row, 3)
            price_item = self.table_model.item(row, 2)

            quantity_text = quantity_item.text().strip()

            if not quantity_text.isdigit():
                self.mainwindow.setEnabled(False)
                self.msg_box = QMessageBox(self.mainwindow)
                self.msg_box.setWindowTitle('Error')
                self.msg_box.setIcon(QMessageBox.Critical)
                self.msg_box.setText('Only integer values allowed for quantity')
                self.msg_box.setStandardButtons(QMessageBox.Ok)
                self.msg_box.exec_()
                self.mainwindow.setEnabled(True)
                cleaned_qty_item = QtGui.QStandardItem(str(1))
                cleaned_qty_item.setFlags(cleaned_qty_item.flags() | QtCore.Qt.ItemIsEditable)
                self.table_model.setItem(row, 3, cleaned_qty_item)
                self.update_grand_total()
                return  # Stop further execution
            else:
                if quantity_text.startswith('0') and len(quantity_text) > 1:
                    new_value = str(int(quantity_text))
                    # Clean leading zeros
                    quantity = int(new_value)
                    price = int(price_item.text())
                    total = quantity * price
                    
                    self.table_model.blockSignals(True)
                    total_item = QtGui.QStandardItem(str(total))
                    total_item.setFlags(total_item.flags() & ~QtCore.Qt.ItemIsEditable)
                    self.table_model.setItem(row, 4, total_item)

                    # Update cleaned quantity back to column 4
                    cleaned_qty_item = QtGui.QStandardItem(str(quantity))
                    cleaned_qty_item.setFlags(cleaned_qty_item.flags() | QtCore.Qt.ItemIsEditable)
                    self.table_model.setItem(row, 3, cleaned_qty_item)

                    # Re-enable signals
                    self.table_model.blockSignals(False)
                    self.update_grand_total()
                else:
                    new_value = quantity_text

                    # Clean leading zeros
                    quantity = int(new_value)
                    price = int(price_item.text())
                    total = quantity * price
                    
                    self.table_model.blockSignals(True)
                    total_item = QtGui.QStandardItem(str(total))
                    total_item.setFlags(total_item.flags() & ~QtCore.Qt.ItemIsEditable)
                    self.table_model.setItem(row, 4, total_item)

                    # Update cleaned quantity back to column 4
                    cleaned_qty_item = QtGui.QStandardItem(str(quantity))
                    cleaned_qty_item.setFlags(cleaned_qty_item.flags() | QtCore.Qt.ItemIsEditable)
                    self.table_model.setItem(row, 3, cleaned_qty_item)

                    # Re-enable signals
                    self.table_model.blockSignals(False)
                    self.update_grand_total()











#   Button --- button execution 
class ButtonDelegate(QStyledItemDelegate):
    clicked = pyqtSignal(QtCore.QModelIndex)

    def paint(self, painter, option, index):
        if index.column() == 5:  # "Remove" column
            button = QPushButton("Remove")
            button.setStyleSheet("background-color: red; color: white; border: none; padding: 5px;")
            button.resize(option.rect.size())
            painter.save()
            painter.translate(option.rect.topLeft())
            button.render(painter)
            painter.restore()
        else:
            super().paint(painter, option, index)

    def editorEvent(self, event, model, option, index):
        if event.type() == QtCore.QEvent.MouseButtonRelease and index.column() == 5:
            self.clicked.emit(index)
        return super().editorEvent(event, model, option, index)

                

