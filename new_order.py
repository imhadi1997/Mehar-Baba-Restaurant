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



class new_order_class:
    #   init
    def __init__(self, centralwidget, username , usertype, mainwindow, userid):
        self.centralwidget = centralwidget
        self.username = username
        self.usertype = usertype
        self.mainwindow = mainwindow
        self.userid = userid

    #   New Order Frame
    def new_order_frame(self):
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

        self.tableView = QtWidgets.QTableView(self.widget)
        self.tableView.setGeometry(QtCore.QRect(10, 40, 611, 411))
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

        self.pushButton = QtWidgets.QPushButton(self.widget)
        self.pushButton.setGeometry(QtCore.QRect(630, 350, 75, 23))
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

        _translate = QtCore.QCoreApplication.translate
        self.label_5.setText(_translate("MainWindow", "    Order No :"))
        self.label_4.setText(_translate("MainWindow", "    Search :"))
        self.label_6.setText(_translate("MainWindow", "    item Code :"))
        self.label_7.setText(_translate("MainWindow", "    item Name :"))
        self.label_8.setText(_translate("MainWindow", "      Quantity :"))
        self.label_9.setText(_translate("MainWindow", "   Master level :"))
        self.label_10.setText(_translate("MainWindow", "     Sale Price :"))
        self.label.setText(_translate("MainWindow", "Grand Total :"))
        self.lineEdit_7.setPlaceholderText(_translate("MainWindow", "0"))
        self.pushButton.setText(_translate("MainWindow", "Save"))
        self.pushButton_2.setText(_translate("MainWindow", "Close"))
        self.pushButton_3.setText(_translate("MainWindow", "Add"))
        self.pushButton_4.setText(_translate("MainWindow", "Clear"))
        
        self.pushButton_2.clicked.connect(lambda: self.close_button())

        master_input_dict = {}
        item_input_dict = {}
        model = QtGui.QStandardItemModel()
        model.setHorizontalHeaderLabels(["Code", "item name","Sale Price", "Quantity", "Total", "Action"])
        checkdata = add_item_database().existing_add_new_item()
        if checkdata == [] or checkdata != []:
            for row in checkdata:
                item_input_dict[str(row[5]) + " " + str(row[3])] = [str(row[1]), str(row[7]), str(row[4])]
                master_input_dict[str(row[7])] = str(row[6])
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
        self.lineEdit.setCompleter(self.completer)

        def on_completer_activated(text):
            self.lineEdit.setText(text)
            dict_values = item_input_dict[text]
            self.lineEdit_4.setText(dict_values[0])
            self.lineEdit_5.setText(text)
            self.lineEdit_3.setText(dict_values[1])
            self.lineEdit_7.setText(dict_values[2])
            self.lineEdit_6.clear()
            self.lineEdit_6.setFocus()
        
        def block_leading_zero(text):
            if text.startswith("0") and len(text) > 1:
                # Remove leading zero
                self.lineEdit_6.setText(text.lstrip("0"))

        self.lineEdit_6.textChanged.connect(block_leading_zero)
        self.completer.activated[str].connect(on_completer_activated)
        self.lineEdit.setFocus()

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
        # Add delegate to column 5 ("Remove")
        self.button_delegate = ButtonDelegate(self.tableView)
        self.tableView.setItemDelegateForColumn(5, self.button_delegate)

        # Connect the delegate's clicked signal
        self.button_delegate.clicked.connect(self.handle_table_click)


        self.pushButton.clicked.connect(self.save_new_order_details)
        self.pushButton_3.clicked.connect(self.add_to_cart)
        self.pushButton_4.clicked.connect(self.clear_every_thing)
        self.pushButton_4.setDefault(True)
        self.pushButton_3.setDefault(True)
        self.pushButton_2.setDefault(True)
        self.pushButton.setDefault(True)
        self.new_order_number_backend()

        
    #   Close to Main Window
    def close_button(self):
        main_page(self.centralwidget, self.username, self.usertype).close_function()

    #   Add to Cart
    def add_to_cart(self):
        # Get values from line edits
        item_name = self.lineEdit.text()
        item_code = self.lineEdit_4.text()
        master = self.lineEdit_3.text()
        sale_price = self.lineEdit_7.text()
        quantity = self.lineEdit_6.text()
        if item_name and item_code and master and sale_price and quantity:
            for row in range(self.table_model.rowCount()):
                existing_code = self.table_model.item(row, 0).text()  # Column 0 = item_code
                if existing_code == item_code:
                    # Show warning and skip adding
                    self.mainwindow.setEnabled(False)
                    self.msg_box = QMessageBox(self.mainwindow)
                    self.msg_box.setWindowTitle('Duplicate')
                    self.msg_box.setIcon(QMessageBox.Warning)
                    self.msg_box.setText(f'Item code "{item_code}" already exists in the cart.')
                    self.msg_box.setStandardButtons(QMessageBox.Ok)
                    self.msg_box.exec_()
                    self.mainwindow.setEnabled(True)
                    return  # Exit the function, don't add duplicate
                
            remove_button_item = QtGui.QStandardItem("Remove")
            total = int(sale_price) * int(quantity)
            row = [
            QtGui.QStandardItem(item_code),
            QtGui.QStandardItem(item_name),
            QtGui.QStandardItem(sale_price),
            QtGui.QStandardItem(quantity),
            QtGui.QStandardItem(str(total)),
            QtGui.QStandardItem(remove_button_item)
            ]
            for col, item in enumerate(row):
                if col == 3:  # Quantity column
                    item.setFlags(item.flags() | QtCore.Qt.ItemIsEditable)
                else:
                    item.setFlags(item.flags() & ~QtCore.Qt.ItemIsEditable)

            self.table_model.appendRow(row)

            self.lineEdit.clear()
            self.lineEdit_4.clear()
            self.lineEdit_3.clear()
            self.lineEdit_5.clear()
            self.lineEdit_7.clear()
            self.lineEdit_6.clear()
            self.lineEdit.setFocus()
            self.update_grand_total()

        else:
            self.mainwindow.setEnabled(False)
            self.msg_box = QMessageBox(self.mainwindow)
            self.msg_box.setWindowTitle('Empty')
            self.msg_box.setIcon(QMessageBox.Critical)
            self.msg_box.setText('Code, item name & quantity required')
            self.msg_box.setStandardButtons(QMessageBox.Ok)
            self.msg_box.exec_()
            self.mainwindow.setEnabled(True)

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

    #   Clear everything
    def clear_every_thing(self):
        self.lineEdit.clear()
        self.lineEdit_4.clear()
        self.lineEdit_3.clear()
        self.lineEdit_5.clear()
        self.lineEdit_7.clear()
        self.lineEdit_6.clear()
        self.table_model.removeRows(0, self.table_model.rowCount())
        self.lcdNumber.display(0)
        self.lineEdit.setFocus()
        self.new_order_number_backend()

    #Enter key
    def keyPressEvent(self, event):
        if event.key() in (QtCore.Qt.Key_Return, QtCore.Qt.Key_Enter):
            focus_widget = self.focusWidget()
            if isinstance(focus_widget, QtWidgets.QPushButton):
                focus_widget.click()

    #   New order number
    def new_order_number_backend(self):
        fromdatabase = order_database().new_order_number()
        if fromdatabase == False:
            self.mainwindow.setEnabled(False)
            self.msg_box = QMessageBox(self.mainwindow)
            self.msg_box.setWindowTitle('Error')
            self.msg_box.setIcon(QMessageBox.Critical)
            self.msg_box.setText('Contact admin, database connection lost')
            self.msg_box.setStandardButtons(QMessageBox.Ok)
            self.msg_box.exec_()
            self.mainwindow.setEnabled(True)
        else:
            self.lineEdit_2.setText(str(fromdatabase))

    #   Save New Order Details
    def save_new_order_details(self):
        model = self.tableView.model()
        rows = model.rowCount()
        if rows == 0:
            self.mainwindow.setEnabled(False)
            self.msg_box = QMessageBox(self.mainwindow)
            self.msg_box.setWindowTitle('Error')
            self.msg_box.setIcon(QMessageBox.Critical)
            self.msg_box.setText('Cart is empty')
            self.msg_box.setStandardButtons(QMessageBox.Ok)
            self.msg_box.exec_()
            self.mainwindow.setEnabled(True)
        else:
            data_to_save = []
            for row in range(rows):
                col0 = model.item(row, 0).text() if model.item(row, 0) else ""
                col2 = model.item(row, 2).text() if model.item(row, 2) else ""
                col3 = model.item(row, 3).text() if model.item(row, 3) else ""

                data_to_save.append((col0, col2, col3))
            
            saveorderdetails = order_database().save_new_order_database(self.userid, data_to_save)
            if saveorderdetails == False:
                self.mainwindow.setEnabled(False)
                self.msg_box = QMessageBox(self.mainwindow)
                self.msg_box.setWindowTitle('Error')
                self.msg_box.setIcon(QMessageBox.Critical)
                self.msg_box.setText('Contact admin, database connection lost')
                self.msg_box.setStandardButtons(QMessageBox.Ok)
                self.msg_box.exec_()
                self.mainwindow.setEnabled(True)
            elif isinstance(saveorderdetails, tuple) and len(saveorderdetails) == 2 and saveorderdetails[0] == 'Save':
                self.mainwindow.setEnabled(False)
                self.msg_box = QMessageBox(self.mainwindow)
                self.msg_box.setWindowTitle('Saved')
                self.msg_box.setIcon(QMessageBox.Information)
                self.msg_box.setText(str(saveorderdetails[1]) + ' order has been saved')
                self.msg_box.setStandardButtons(QMessageBox.Ok)
                self.msg_box.exec_()
                self.mainwindow.setEnabled(True)
                self.clear_every_thing()




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

                

