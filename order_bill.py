from PyQt5 import QtCore, QtGui, QtWidgets
import datetime
from close import main_page
from PyQt5.QtWidgets import QHeaderView
from database import order_database
from PyQt5.QtWidgets import QMessageBox
from PyQt5.QtWidgets import QStyledItemDelegate, QPushButton, QApplication
from PyQt5.QtCore import Qt, QRect, pyqtSignal

class customer_order_bill:
    #   init
    def __init__(self, centralwidget, username , usertype, mainwindow, userid):
        self.centralwidget = centralwidget
        self.username = username
        self.usertype = usertype
        self.mainwindow = mainwindow
        self.userid = userid

    #   New Order Frame
    def order_bill_fram(self):
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
        self.lineEdit.setGeometry(QtCore.QRect(720, 240, 191, 21))
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
        self.lineEdit_6.setGeometry(QtCore.QRect(720, 270, 191, 21))
        self.lineEdit_6.setStyleSheet("background-color: rgb(255, 255, 255);\n"
        "color: rgb(0, 0, 0);\n"
        "font: 8pt \"MS Shell Dlg 2\";\n"
        "border : 1px solid black;")
        self.lineEdit_6.setReadOnly(False)
        self.lineEdit_6.setCursorMoveStyle(QtCore.Qt.LogicalMoveStyle)
        self.lineEdit_6.setClearButtonEnabled(False)
        self.lineEdit_6.setObjectName("lineEdit_6")
        self.lineEdit_6.show()

        
        int_validator = QtGui.QIntValidator(0, 999999)  # (min, max) range; use any range you want
        self.lineEdit_6.setValidator(int_validator)

        self.spinBox = QtWidgets.QSpinBox(self.widget)
        self.spinBox.setGeometry(QtCore.QRect(720, 300, 191, 22))
        self.spinBox.setStyleSheet("color: rgb(0, 0, 0);\n"
        "background-color: rgb(255, 255, 255);")
        self.spinBox.setButtonSymbols(QtWidgets.QAbstractSpinBox.PlusMinus)
        self.spinBox.setAccelerated(False)
        self.spinBox.setProperty("showGroupSeparator", False)
        self.spinBox.setSuffix("")
        self.spinBox.setPrefix("")
        self.spinBox.setMaximum(100)
        self.spinBox.setStepType(QtWidgets.QAbstractSpinBox.DefaultStepType)
        self.spinBox.setProperty("value", 0)
        self.spinBox.setObjectName("spinBox")
        self.spinBox.lineEdit().setPlaceholderText("Only int value between 0 to 100")
        self.spinBox.show()

        self.pushButton_3 = QtWidgets.QPushButton(self.widget)
        self.pushButton_3.setGeometry(QtCore.QRect(720, 360, 121, 23))
        self.pushButton_3.setStyleSheet("QPushButton {\n"
        "    background-color: #f0f0f0;\n"
        "    border: 1px solid #555;\n"
        "    padding: 5px;\n"
        "}\n"
        "\n"
        "QPushButton:pressed {\n"
        "    background-color: #bdfff8;       /* darker when pressed */\n"
        "    border-style: inset;             /* gives a pushed-in look */\n"
        "}\n"
        "")
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_3.show()

        self.pushButton = QtWidgets.QPushButton(self.widget)
        self.pushButton.setGeometry(QtCore.QRect(850, 360, 75, 23))
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
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("images/blue-save-disk-icon-0.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton.setIcon(icon1)
        self.pushButton.setObjectName("pushButton")
        self.pushButton.show()

        self.pushButton_4 = QtWidgets.QPushButton(self.widget)
        self.pushButton_4.setGeometry(QtCore.QRect(630, 390, 75, 23))
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
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("images/refresh.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_4.setIcon(icon2)
        self.pushButton_4.setObjectName("pushButton_4")
        self.pushButton_4.show()

        self.pushButton_2 = QtWidgets.QPushButton(self.widget)
        self.pushButton_2.setGeometry(QtCore.QRect(630, 420, 75, 23))
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

        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("images/delete-sign.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_2.setIcon(icon)
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_2.show()

        self.label_4 = QtWidgets.QLabel(self.widget)
        self.label_4.setGeometry(QtCore.QRect(630, 240, 61, 21))
        self.label_4.setStyleSheet("border : 0px;")
        self.label_4.setObjectName("label_4")
        self.label_4.show()

        self.label_8 = QtWidgets.QLabel(self.widget)
        self.label_8.setGeometry(QtCore.QRect(650, 270, 31, 21))
        self.label_8.setStyleSheet("border : 0px;")
        self.label_8.setObjectName("label_8")
        self.label_8.show()

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

        self.label_11 = QtWidgets.QLabel(self.widget)
        self.label_11.setGeometry(QtCore.QRect(640, 300, 61, 21))
        self.label_11.setStyleSheet("border : 0px;")
        self.label_11.setObjectName("label_11")
        self.label_11.show()

        self.label_12 = QtWidgets.QLabel(self.widget)
        self.label_12.setGeometry(QtCore.QRect(630, 330, 81, 21))
        self.label_12.setStyleSheet("border : 0px;")
        self.label_12.setObjectName("label_12")
        self.label_12.show()

        self.lineEdit_7 = QtWidgets.QLineEdit(self.widget)
        self.lineEdit_7.setGeometry(QtCore.QRect(720, 330, 191, 21))
        self.lineEdit_7.setStyleSheet("background-color: rgb(255, 255, 255);\n"
        "color: rgb(0, 0, 0);\n"
        "font: 8pt \"MS Shell Dlg 2\";\n"
        "border : 1px solid black;")
        self.lineEdit_7.setReadOnly(True)
        self.lineEdit_7.setPlaceholderText("")
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

        now = datetime.datetime.now()
        todaydate = now.strftime("%Y-%m-%d")
        todaytime = now.strftime("%I:%M:%S %p")

        # Set the content
        self.plainTextEdit.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.plainTextEdit.setFocusPolicy(QtCore.Qt.NoFocus)
        self.plainTextEdit.show()

        self.label_2 = QtWidgets.QLabel(self.widget)
        self.label_2.setGeometry(QtCore.QRect(660, 10, 311, 221))
        self.label_2.setStyleSheet("border : 0pt;")
        self.label_2.setText("")
        self.label_2.setPixmap(QtGui.QPixmap("images/Logo MB 02 (1).PNG"))
        self.label_2.setScaledContents(True)
        self.label_2.setObjectName("label_2")
        self.label_2.show()

        _translate = QtCore.QCoreApplication.translate
        self.label_5.setText(_translate("MainWindow", "   Bill No :"))
        self.label_4.setText(_translate("MainWindow", "     Search :"))
        self.label_8.setText(_translate("MainWindow", "Paid :"))
        self.lineEdit_6.setPlaceholderText(_translate("MainWindow", "Only int value"))
        self.label.setText(_translate("MainWindow", "Grand Total :"))
        self.pushButton_2.setText(_translate("MainWindow", "Close"))
        self.label_11.setText(_translate("MainWindow", "Discount % :"))
        self.pushButton.setText(_translate("MainWindow", "Save"))
        self.label_12.setText(_translate("MainWindow", "After Discount :"))
        self.pushButton_3.setText(_translate("MainWindow", "Calculate"))
        self.pushButton_4.setText(_translate("MainWindow", "Clear"))

        self.lineEdit.setFocus()

        self.pushButton_3.setDefault(True)
        self.pushButton_2.setDefault(True)
        self.pushButton.setDefault(True)

        item_input_dict = {}
        model = QtGui.QStandardItemModel()
        model.setHorizontalHeaderLabels(["Code", "item name","Sale Price", "Qty", "Total"])
        checkdata = order_database().all_unpaid_order(True, False)
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
        self.lineEdit.setCompleter(self.completer)

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
                self.lineEdit.setText(text)
                dict_values = item_input_dict[text]
                self.lineEdit_2.setText(text)
                self.lineEdit_6.clear()
                self.lineEdit_6.setFocus()
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
                    itemqty.setFlags(itemqty.flags() & ~QtCore.Qt.ItemIsEditable)

                    total = int(row[3]) * int(row[4])
                    itemtotal = QtGui.QStandardItem(str(total))
                    itemtotal.setFlags(itemtotal.flags() & ~QtCore.Qt.ItemIsEditable)

                    model.appendRow([codeno, itemname, itemprice, itemqty, itemtotal])
                self.update_grand_total()

        def block_leading_zero(text):
            if text.startswith("0") and len(text) > 1:
                # Remove leading zero
                self.lineEdit_6.setText(text.lstrip("0"))

        def strip_spinbox_leading_zero(text):
            if text.startswith("0") and len(text) > 1:
                # Remove leading zeros and update spinbox value
                new_value = int(text.lstrip("0"))
                self.spinBox.setValue(new_value)


        self.completer.activated[str].connect(on_completer_activated)
        self.lineEdit_6.textChanged.connect(block_leading_zero)
        # After creating the spinBox...
        self.spinBox.lineEdit().textChanged.connect(strip_spinbox_leading_zero)
        self.pushButton_4.clicked.connect(self.clear_every_thing)
        self.pushButton_2.clicked.connect(lambda: self.close_button())
        self.pushButton_3.clicked.connect(self.calculator)
        self.pushButton_4.setDefault(True)
        self.pushButton_3.setDefault(True)
        self.pushButton_2.setDefault(True)
        self.pushButton.setDefault(True)

        self.tableView.setModel(model)
        self.table_model = model  # Save reference for reuse in Add function
        self.tableView.setColumnWidth(0, 60)   # Code column width
        self.tableView.setColumnWidth(1, 250)
        self.tableView.setColumnWidth(2, 70)
        self.tableView.setColumnWidth(3, 70)
        self.tableView.setColumnWidth(4, 70)
        header = self.tableView.horizontalHeader()
        header.setSectionResizeMode(QHeaderView.Fixed)
        

    #   Close to Main Window
    def close_button(self):
        main_page(self.centralwidget, self.username, self.usertype).close_function()

    #Enter key
    def keyPressEvent(self, event):
        if event.key() in (QtCore.Qt.Key_Return, QtCore.Qt.Key_Enter):
            focus_widget = self.focusWidget()
            if isinstance(focus_widget, QtWidgets.QPushButton):
                focus_widget.click()

    #   Clear everything
    def clear_every_thing(self):
        self.lineEdit.clear()
        self.lineEdit_7.clear()
        self.lineEdit_6.clear()
        self.table_model.removeRows(0, self.table_model.rowCount())
        self.lcdNumber.display(0)
        self.lineEdit.setFocus()
        self.spinBox.setProperty("value", 0)

    #   Calculator
    def calculator(self):
        grandtotal = self.lcdNumber.value()
        discountratio = self.spinBox.text()
        if grandtotal and discountratio:
            checkdiscount = int(grandtotal) * (int(discountratio) / 100)
            afterdiscountvalue = int(grandtotal) - int(checkdiscount)
            self.lineEdit_7.setText(str(afterdiscountvalue))
        else:
            self.mainwindow.setEnabled(False)
            self.msg_box = QMessageBox(self.mainwindow)
            self.msg_box.setWindowTitle('Empty')
            self.msg_box.setIcon(QMessageBox.Critical)
            self.msg_box.setText('Grand total & discount required')
            self.msg_box.setStandardButtons(QMessageBox.Ok)
            self.msg_box.exec_()
            self.mainwindow.setEnabled(True)
            self.lineEdit.setFocus()


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

    #   Save Bill
    def save_bill(self):
        orderno = self.lineEdit_2.text()
        cash = self.lineEdit_6.text()
        discount = self.spinBox.text()
        afterdiscout = self.lineEdit_7.text()
        grandtotal = self.lcdNumber.value()
        if orderno and cash and discount and afterdiscout:
            if int(cash) >= int(afterdiscout):
                savebill = order_database().save_bill_database(orderno, cash, discount, self.userid)
                if savebill == True:
                    baqiamount = int(cash) - int(afterdiscout)
                    one_outtext = "Grand Total: " + str(grandtotal) + "\n"
                    two_outtext = "Discount %: " + str(discount) + "\n"
                    three_outtext = "After Discount: " + str(afterdiscout) + "\n"
                    four_outtext = "Cash paid: " + str(cash) + "\n"
                    five_outtext = "Cash back: " + str(baqiamount)
                    output_result = str(one_outtext) + str(two_outtext) + str(three_outtext) + str(four_outtext) + str(five_outtext)
                    self.mainwindow.setEnabled(False)
                    self.msg_box = QMessageBox(self.mainwindow)
                    self.msg_box.setWindowTitle('Saved')
                    self.msg_box.setIcon(QMessageBox.Information)
                    self.msg_box.setText(str(output_result))
                    self.msg_box.setStandardButtons(QMessageBox.Ok)
                    self.msg_box.exec_()
                    self.mainwindow.setEnabled(True)
                    self.clear_every_thing()
                elif savebill == False:
                    self.mainwindow.setEnabled(False)
                    self.msg_box = QMessageBox(self.mainwindow)
                    self.msg_box.setWindowTitle('Error')
                    self.msg_box.setIcon(QMessageBox.Critical)
                    self.msg_box.setText('Contact admin, database connection lost')
                    self.msg_box.setStandardButtons(QMessageBox.Ok)
                    self.msg_box.exec_()
                    self.mainwindow.setEnabled(True)
                    self.lineEdit.setFocus()
            
            elif int(cash) < int(afterdiscout):
                baqiamount = int(afterdiscout) - int(cash)
                one_outtext = "Grand Total: " + str(grandtotal) + "\n"
                two_outtext = "Discount %: " + str(discount) + "\n"
                three_outtext = "After Discount: " + str(afterdiscout) + "\n"
                four_outtext = "Cash paid: " + str(cash) + "\n"
                five_outtext = "Remain amount: " + str(baqiamount)
                output_result = str(one_outtext) + str(two_outtext) + str(three_outtext) + str(four_outtext) + str(five_outtext)
                self.mainwindow.setEnabled(False)
                self.msg_box = QMessageBox(self.mainwindow)
                self.msg_box.setWindowTitle('Payment issue')
                self.msg_box.setIcon(QMessageBox.Critical)
                self.msg_box.setText(str(output_result))
                self.msg_box.setStandardButtons(QMessageBox.Ok)
                self.msg_box.exec_()
                self.mainwindow.setEnabled(True)
                self.lineEdit.setFocus()
            
        else:
            self.mainwindow.setEnabled(False)
            self.msg_box = QMessageBox(self.mainwindow)
            self.msg_box.setWindowTitle('Empty')
            self.msg_box.setIcon(QMessageBox.Critical)
            self.msg_box.setText('Order no , cash & after discount total required')
            self.msg_box.setStandardButtons(QMessageBox.Ok)
            self.msg_box.exec_()
            self.mainwindow.setEnabled(True)
            self.lineEdit.setFocus()



"""
    #   Remove From cart
    def handle_table_click(self, index):
        row = index.row()
        col = index.column()

        # Assuming "Remove" is in column 5
        if col == 5:
            item_code = self.table_model.item(row, 0).text()
            orderno = self.lineEdit_2.text()
            deleteitemdetails = order_database().delete_order_details(item_code, orderno)
            if deleteitemdetails == False:
                self.mainwindow.setEnabled(False)
                self.msg_box = QMessageBox(self.mainwindow)
                self.msg_box.setWindowTitle('Error')
                self.msg_box.setIcon(QMessageBox.Critical)
                self.msg_box.setText('Contact admin, database connection lost')
                self.msg_box.setStandardButtons(QMessageBox.Ok)
                self.msg_box.exec_()
                self.mainwindow.setEnabled(True)
            elif deleteitemdetails == True:
                self.table_model.removeRow(row)
                self.lineEdit.setFocus()
                self.update_grand_total()

                
    deletebutton = QtGui.QStandardItem("Delete")
    deletebutton.setFlags(deletebutton.flags() & ~QtCore.Qt.ItemIsEditable)

    self.button_delegate = ButtonDelegate(self.tableView)
    self.tableView.setItemDelegateForColumn(5, self.button_delegate)

    # Connect the delegate's clicked signal
    self.button_delegate.clicked.connect(self.handle_table_click)


"""

