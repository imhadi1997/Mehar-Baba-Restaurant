import mysql.connector as mysql
import locale
import datetime

locale.setlocale(locale.LC_ALL, 'C')


class database_class:
    #   init
    def __init__(self):
        self.dbhostname =  "localhost"
        self.databaseusername = "root"
        self.dbpassword = "...ppptkinter"
        self.dbname = "mehar_baba"
        try:
            self.conn = mysql.connect(
                    host = self.dbhostname,
                    username = self.databaseusername,
                    password = self.dbpassword,
                    database = self.dbname
                    )
            self.pointer = self.conn.cursor(buffered=True)
        except:
            pass

    #   DataBase Connection
    def database_connection_check(self):
        try:
            self.conn = mysql.connect(
                host = self.dbhostname,
                username = self.databaseusername,
                password = self.dbpassword,
                database = self.dbname
                )
            self.pointer = self.conn.cursor(buffered=True)
            return True
        except:
            return False
        
            
    #   USer Check
    def user_checking(self, user, password):
        a = database_class().database_connection_check()
        if a == True:
            u = user
            p = password
            query = """SELECT users.*, erp_type.name 
                        FROM users
                        LEFT JOIN erp_type ON users.type = erp_type.type_id 
                        WHERE users.user=%s AND users.password=%s AND users.activation=%s"""
            self.pointer.execute(query, [u, p, True])
            details = self.pointer.fetchall()
            if details == []:
                return "Empty"
            else:
                return details
        else:
            return False
        

#   Menu DataBase
class menu_database(database_class):
    def __init__(self):
        super().__init__()

    #   Master Input Table - All
    def master_input_table(self):
        databaseconcheck = database_class().database_connection_check()
        if databaseconcheck == True:
            query3 = """SELECT top_level.*
                        FROM top_level
                        ORDER BY top_level.level_id ASC;
                        """
            self.pointer.execute(query3)
            all_dep_ids = self.pointer.fetchall()
            return all_dep_ids
        else:
            return False

    #   Master input Name Edit
    def update_master_input_edit(self, itemname, itemcode):
        databaseconcheck = database_class().database_connection_check()
        if databaseconcheck == True:
            newname = str(itemname).capitalize()
            query = "UPDATE top_level SET name=%s WHERE level_id=%s"
            self.pointer.execute(query, [newname, itemcode])
            self.conn.commit()
            return True
        else:
            return False
        
    #   Save New Master input
    def save_new_master_input_table(self, itemname):
        databaseconcheck = database_class().database_connection_check()
        newempid = menu_database().new_top_level_id()
        if databaseconcheck == True and newempid != False:
            empid = str(newempid)
            name = str(itemname).capitalize()
            query1 = """INSERT INTO top_level(level_id, name)
                        VALUES(%s, %s)"""
            self.pointer.execute(query1, [empid, name])
            self.conn.commit()
            return True
        else:
            return False

    #   New Top Level
    def new_top_level_id(self):
        a = database_class().database_connection_check()
        if a == True:
            ## Get the current maximum order ID
            query = "SELECT MAX(level_id) FROM top_level ORDER BY top_level.level_id ASC;"
            self.pointer.execute(query)
            max_id = self.pointer.fetchone()[0]

            # Increment the maximum order ID to get the next order ID
            if max_id is None:
                new_order_id = '01'
            else:
                new_order_id = str(int(max_id) + 1).zfill(2)

            return new_order_id
        else:
            return False


#   New Main Category
class main_category_database(database_class):
    #   init
    def __init__(self):
        super().__init__()

    #   Existing Main Category
    def existing_main_category(self):
        a = database_class().database_connection_check()
        if a == True:
            #   QUERY
            query3 = """SELECT main_category.*, top_level.name
                        FROM main_category
                        LEFT JOIN top_level ON main_category.level_id = top_level.level_id
                        ORDER BY main_category.cat_id ASC;
                        """
            self.pointer.execute(query3)
            all_dep_ids = self.pointer.fetchall()
            return all_dep_ids
        else:
            return False
        
    #   Update Existing item name
    def update_item_name_table(self, itemname, itemcode):
        a = database_class().database_connection_check()
        if a == True:
            #   QUERY
            newname = str(itemname).capitalize()
            query = "UPDATE main_category SET name=%s WHERE cat_id=%s"
            self.pointer.execute(query, [newname, itemcode])
            self.conn.commit()
            return True
        else:
            return False
        

    #   Save Main Category
    def save_new_main_category(self, name, mastercode):
        a = database_class().database_connection_check()
        newempid = main_category_database().new_main_category_id()
        if a == True and newempid != False:
            itemane = str(name).capitalize()
            query1 = """INSERT INTO main_category(cat_id, level_id, name)
                        VALUES(%s, %s, %s)"""
            self.pointer.execute(query1, [newempid, mastercode, itemane])
            self.conn.commit()
            return True
        else:
            return False


    #   New Item id
    def new_main_category_id(self):
        a = database_class().database_connection_check()
        if a == True:
            ## Get the current maximum order ID
            query = "SELECT MAX(cat_id) FROM main_category ORDER BY main_category.cat_id ASC;"
            self.pointer.execute(query)
            max_id = self.pointer.fetchone()[0]

            # Increment the maximum order ID to get the next order ID
            if max_id is None:
                new_order_id = '001'
            else:
                new_order_id = str(int(max_id) + 1).zfill(3)

            return new_order_id
        else:
            return False


#   Add new item
class add_item_database(database_class):
    #   init
    def __init__(self):
        super().__init__()

    #   Existing Add item
    def existing_add_new_item(self):
        a = database_class().database_connection_check()
        if a == True:
            #   QUERY
            query3 = """SELECT item_table.*, main_category.name, main_category.level_id, top_level.name
                        FROM item_table
                        LEFT JOIN main_category ON item_table.cat_id = main_category.cat_id
                        LEFT JOIN top_level ON main_category.level_id = top_level.level_id
                        ORDER BY item_table.item_id ASC;"""             
            self.pointer.execute(query3)
            all_dep_ids = self.pointer.fetchall()
            return all_dep_ids
        else:
            return False

    #   Change item Name
    def edit_type_of_item_table(self, itemname, itemcode):
        a = database_class().database_connection_check()
        if a == True:
            #   QUERY
            newname = str(itemname).capitalize()
            query = "UPDATE item_table SET name=%s WHERE item_id=%s"
            self.pointer.execute(query, [newname, itemcode])
            self.conn.commit()
            return True
        else:
            return False
        
    #   Edit item sale price
    def edit_item_sale_price_table(self, newprice, itemcode):
        a = database_class().database_connection_check()
        if a == True:
            #   QUERY
            query = "UPDATE item_table SET sale_price=%s WHERE item_id=%s"
            self.pointer.execute(query, [newprice, itemcode])
            self.conn.commit()
            return True
        else:
            return False
        
    #   Save new item type
    def save_new_item_type_table(self, itemname, mainitemcode, saleprice):
        a = database_class().database_connection_check()
        newempid = add_item_database().new_item_id()
        if a == True and newempid != False:
            #   Query
            baraname = str(itemname).capitalize()
            query = 'INSERT INTO item_table(item_id, cat_id, name, sale_price) VALUES(%s, %s, %s, %s)'
            self.pointer.execute(query, [newempid, mainitemcode, baraname, saleprice])
            self.conn.commit()
            return True
        else:
            return False


    #   New item id
    def new_item_id(self):
        a = database_class().database_connection_check()
        if a == True:
            ## Get the current maximum order ID
            query = "SELECT MAX(item_id) FROM item_table ORDER BY item_table.item_id ASC;"
            self.pointer.execute(query)
            max_id = self.pointer.fetchone()[0]

            # Increment the maximum order ID to get the next order ID
            if max_id is None:
                new_order_id = '0001'
            else:
                new_order_id = str(int(max_id) + 1).zfill(4)

            return new_order_id
        else:
            return False


#   Order Class
class order_database(database_class):
    #   init
    def __init__(self):
        super().__init__()

    #   check login details
    def new_order_number(self):
        a = database_class().database_connection_check()
        if a == True:
            now = datetime.datetime.now()
            current_year = now.strftime("%Y")  # Use %Y for the calendar year
            
            # Query to get the most recent order_id for the current year
            query = """
                    SELECT order_id FROM new_order 
                    WHERE order_id LIKE %s
                    ORDER BY LENGTH(order_id) DESC, order_id DESC 
                    LIMIT 1
                    """
            like_pattern = f"mb-{current_year}-%"
            
            # Execute the query and fetch the result
            self.pointer.execute(query, (like_pattern,))
            result = self.pointer.fetchone()
            
            if result:
                # Extract the last order number from the last 'order_id'
                last_order_id = result[0]  # Fetching order_id string
                last_order_number = int(last_order_id.split('-')[-1])  # Get the order number part
                new_order_number = last_order_number + 1
            else:
                # If no orders exist for the current year, start with order number 1
                new_order_number = 1
            
            # Format the new order_id as 'mb-year-order_no'
            new_id = f"mb-{current_year}-{new_order_number}"
            return new_id
        else:
            return False
        

    #   Save New Order database
    def save_new_order_database(self, user, orderdetails):
        a = database_class().database_connection_check()
        newid = order_database().new_order_number()
        if a == True and newid != False:
            now = datetime.datetime.now()
            todaydate = now.strftime("%G-%m-%d")

            now1 = datetime.datetime.now()
            todaytime = now1.strftime("%I:%M %p")

            query = """INSERT INTO new_order(order_id, add_by, add_date, add_time, status)
                        VALUES(%s, %s, %s, %s, %s)"""
            self.pointer.execute(query, [newid, user, todaydate, todaytime, False])
            self.conn.commit()

            for i in orderdetails:
                itemcode = i[0]
                itemprice = i[1]
                itemqty = i[2]

                query1 = """ INSERT INTO order_details(order_id, item_id, price, qty) VALUES(%s, %s, %s, %s)"""
                self.pointer.execute(query1, [newid, itemcode, itemprice, itemqty])
                self.conn.commit()

            return 'Save', newid
        else:
            return False
        
    #   All Pending Orders
    def all_unpaid_order(self, checkone, checktwo): # checkone - True / checktwo - False
        a = database_class().database_connection_check()
        if a == True:
            query = """SELECT new_order.*,
                        users1.user AS user,
                        users2.user AS clear_user
                        FROM
                            new_order
                        LEFT JOIN users AS users1 ON new_order.add_by = users1.id
                        LEFT JOIN users AS users2 ON new_order.clear_by = users2.id
                        WHERE
                            new_order.status = %s AND new_order.discount = %s
                        ORDER BY
                            CAST(SUBSTRING_INDEX(new_order.order_id, '-', 1) AS UNSIGNED) ASC"""
            self.pointer.execute(query, [checkone, checktwo])
            details = self.pointer.fetchall()
            return details
        else:
            return False
        
    #   Order Details
    def order_details_database(self, orderid):
        a = database_class().database_connection_check()
        if a == True:
            query = """SELECT order_details.*,
                          item_table.cat_id, 
                          item_table.name AS item_name,
                          main_category.name AS category_name
                   FROM order_details
                   LEFT JOIN item_table ON order_details.item_id = item_table.item_id
                   LEFT JOIN main_category ON item_table.cat_id = main_category.cat_id
                   WHERE order_details.order_id=%s
                   ORDER BY order_details.id ASC"""
            
            self.pointer.execute(query, [orderid])
            details = self.pointer.fetchall()
            return details
        else:
            return False
        
    #   Delete Item befor punch bill
    def delete_order_details(self, item_code, orderno):
        a = database_class().database_connection_check()
        if a == True:
            query = """DELETE FROM order_details WHERE order_id=%s AND item_id=%s"""
            self.pointer.execute(query, [orderno, item_code])
            self.conn.commit()
            return True
        else:
            return False
        
    #   Save Order Bill
    def save_bill_database(self, orderno, cash, discount, userid):
        a = database_class().database_connection_check()
        if a == True:
            now = datetime.datetime.now()
            todaydate = now.strftime("%G-%m-%d")
            todaytime = now.strftime("%I:%M %p")

            query = """INSERT INTO order_bill(bill_no, paid, discount, clear_date, clear_time, clear_by) VALUES(%s,%s,%s,%s,%s)"""
            self.pointer.execute(query, [orderno, cash, discount, todaydate, todaytime, userid])
            self.conn.commit()

            query1 = """UPDATE new_order SET discount=%s WHERE order_id=%s"""
            self.pointer.execute(query1, [True, orderno])
            self.conn.commit()

            return True
        else:
            return False



