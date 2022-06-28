from tkinter import messagebox
import MySQLdb as Sql
import time
import datetime
import pytz


class Dataset:
    def __init__(self, host, user, password, data_base):
        self.host = host
        self.user = user
        self.password = password
        self.data_base = data_base
        self.mydb = ""
        self.s = 0
        self.e = 0
        self.data = None
        self.insert_rec = None
        self.database_conn()

    def database_conn(self):
        self.s = time.time()
        try:
            self.mydb = Sql.connect(self.host, self.user, self.password, self.data_base, connect_timeout=3)
            self.insert_rec = self.mydb.cursor()
            self.e = time.time()
            if self.mydb:
                print('success..\nConnection time: {:0.4f} sec'.format(self.e-self.s))
                return True
        except Exception as e:
            print('Failed...', e)
            messagebox.showerror(title="Connection Error", message="DATABASE CONNECTION ERROR\n PLEASE TRY AGAIN...")
            return self.database_conn()

    def colum_set(self):
        try:
            self.insert_rec.execute("""CREATE TABLE Bank (FIRST_NAME VARCHAR(100), MIDDLE_NAME VARCHAR(100),
                   LAST_NAME VARCHAR(100), DOB DATE, AGE INT, GENDER CHAR(10),
                  INIT_DEP INT, ACC_TYPE CHAR(50), EMPLOYMENT_STATUS VARCHAR(100),
                  PASSWORD INT, EMAIL VARCHAR(50), PHONE_NUM BIGINT, CURR_LOGIN CHAR(50), ACC_STATUS CHAR(10), ACC_NUM INT, LAST_LOGIN VARCHAR(100), ACTIVITY varchar(100000));""")
            self.insert_rec.execute("COMMIT;")
            print("Columns created and committed successfully...")
        except Exception as e:
            print("Exception:", e)

    # getters
    def get_data(self, col, acc_num):
        self.insert_rec.execute(f"SELECT {col} FROM Bank WHERE ACC_NUM={acc_num};")
        self.data = self.insert_rec.fetchall()[0][0]  # fetching output of last statement and printing the 1st element of 1st element.
        return self.data

    # get acc_num and pwd
    def get_log_detail(self, acc, pwd):
        self.insert_rec.execute(f"SELECT ACC_NUM, PASSWORD FROM Bank WHERE ACC_NUM={acc} AND PASSWORD={pwd};")
        self.data = self.insert_rec.fetchall()

    def get_acc(self):
        self.insert_rec.execute("SELECT ACC_NUM FROM Bank;")
        self.data = self.insert_rec.fetchall()

    # setters
    def set_data(self, col, data, acc_no):
        self.insert_rec.execute(f"UPDATE Bank SET {col}='{data}' WHERE ACC_NUM={acc_no};")
        self.insert_rec.execute("COMMIT;")

    def set_bal(self, col, data, acc_no):
        try:
            old_act = str(self.get_data("ACTIVITY", int(acc_no)))
            tme = str(datetime.datetime.now(pytz.timezone("America/Toronto")).strftime("%Y-%m-%d %H:%M:%S %Z"))
            self.insert_rec.execute(f"UPDATE Bank SET {col}={int(self.get_data('BALANCE', int(acc_no))) + int(data)} WHERE ACC_NUM={acc_no};")
            self.insert_rec.execute(f"UPDATE Bank SET ACTIVITY='{old_act}\n${str(data)} was deposited on {tme}';")
            self.insert_rec.execute("COMMIT;")
            return True
        except Exception as e:
            print(e)

    def upd_act(self, data, acc_no):
        try:
            old_act = str(self.get_data("ACTIVITY", int(acc_no)))
            tme = str(datetime.datetime.now(pytz.timezone("America/Toronto")).strftime("%Y-%m-%d %H:%M:%S %Z"))
            self.insert_rec.execute(f"UPDATE Bank SET ACTIVITY='{old_act}\nYour {str(data)} was changed on {tme}';")
            self.insert_rec.execute("COMMIT;")
            return True
        except Exception as e:
            print(e)

    def set_bal_with(self, col, data, acc_no):
        try:
            old_act = str(self.get_data("ACTIVITY", int(acc_no)))
            tme = str(datetime.datetime.now(pytz.timezone("America/Toronto")).strftime("%Y-%m-%d %H:%M:%S %Z"))
            self.insert_rec.execute(f"UPDATE Bank SET {col}={int(self.get_data('BALANCE', int(acc_no))) - int(data)} WHERE ACC_NUM={acc_no};")
            self.insert_rec.execute(f"UPDATE Bank SET ACTIVITY='{old_act}\n${str(data)} was Withdrawn on {tme}';")
            self.insert_rec.execute("COMMIT;")
            return True
        except Exception as e:
            print(e)

    def get_acc_list(self, col1, col2, col3, col4, col5, col6, col7):
        try:
            self.insert_rec.execute(f"SELECT {col1}, {col2}, {col3}, {col4}, {col5}, {col6}, {col7} FROM Bank;")
            self.data = self.insert_rec.fetchall()
            return self.data
        except Exception as e:
            print(e)
    # DELETE FROM Bank WHERE ACC_NUM=;


rasp = Dataset('Host or ipaddress', 'User', 'Password', 'Database')


"""# FIRST NAME
rasp.get_data('FIRST_NAME')
print(rasp.data)
# MIDDLE NAME
rasp.get_data('MIDDLE_NAME')
print(rasp.data)
# LAST NAME
rasp.get_data('LAST_NAME')
print(rasp.data)
# DATE OF BIRTH
rasp.get_data('DOB')
print(rasp.data)
# AGE
rasp.get_data('AGE')
print(rasp.data)
# GENDER
rasp.get_data('GENDER')
print(rasp.data)
# INIT_DEP
rasp.get_data('INIT_DEP')
print(rasp.data)
# ACC_TYPE
rasp.get_data('ACC_TYPE')
print(rasp.data)
# EMPLOYMENT STATUS
rasp.get_data('EMPLOYMENT_STATUS')
print(rasp.data)
# PASSWORD
rasp.get_data('PASSWORD')
print(rasp.data)
# EMAIL
rasp.get_data('EMAIL')
print(rasp.data)
# PHONE NUMBER
rasp.get_data('PHONE_NUM')
print(rasp.data)
# CURRENT LOGIN
rasp.get_data('CURR_LOGIN')
print(rasp.data)
# ACCOUNT STATUS
rasp.get_data('ACC_STATUS')
print(rasp.data)
# ACCOUNT NUMBER
rasp.get_data('ACC_NUM')
print(rasp.data)
# LAST LOGGED IN
rasp.get_data('LAST_LOGIN')
print(rasp.data)

# change the data
rasp.set_data("FIRST_NAME", "abc")
rasp.get_data('FIRST_NAME')
print(rasp.data)
"""
