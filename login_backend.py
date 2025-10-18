from database import database_class
from PyQt5 import QtCore, QtGui, QtWidgets

class login_backend:
    def __init__(self, username, password, mainwindow):
        self.username = username
        self.password = password
        self.mainwindow = mainwindow

    #   check login details
    def check_login_details(self):
        databaseconnection = database_class().user_checking(self.username, self.password)
        if databaseconnection == False:
            return False
        else:
            if databaseconnection == 'Empty':
                return 'Empty'
            else:
                userid = ""
                username = ""
                userpassword = ""
                erp_type = ""
                userstatus = False
                for i in databaseconnection:
                    userid = i[0]
                    username = i[1]
                    userpassword = i[2]
                    userstatus = i[3]
                    erp_type = i[4]

                if userstatus == False:
                    return 'deactive'
                elif userstatus == True:
                    return [erp_type , userid]