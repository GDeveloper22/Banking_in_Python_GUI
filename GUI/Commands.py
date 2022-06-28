import datetime
from Dataset.Dataset_init import rasp
from tkinter import simpledialog, messagebox
import pytz
import random
import os


# Details verification
# first name
def fn_verify(data):
    try:
        fn_v = data
        if fn_v not in ["", " "]:
            if fn_v.isalpha():
                return True, fn_v
            else:
                print("Name must be alphabetical")
                return False, fn_v
    except Exception as e:
        print(e)


# middle name
def mn_verify(data):
    try:
        mn_v = data
        if mn_v.isalpha() or mn_v in ["", " "]:
            return True, mn_v
        else:
            print("Name must be alphabetical")
            return False, mn_v
    except Exception as e:
        print(e)


# last name
def ln_verify(data):
    try:
        ln_v = data
        if ln_v not in ["", " "]:
            if ln_v.isalpha():
                return True, ln_v
            else:
                print("Name must be alphabetical")
                return False, ln_v
    except Exception as e:
        print(e)


# dob
def dob_verify(data):
    try:
        dob_v = data
        dt = datetime.date.today()
        if (int(dob_v[0:4]) <= int(dt.year)) and (len(dob_v) == 10):
            if (dob_v[4] == "-") and (dob_v[7] == "-"):
                if int(dob_v[5:7]) <= 12 and (int(dob_v[8:10]) <= 30) or (int(dob_v[8:10]) <= 31):
                    return True, dob_v
        else:
            return False, dob_v
    except Exception as e:
        print(e)


# age set automatically acc to dob
def age_calc(data):
    age_c = data
    try:
        dt = datetime.date.today()
        age_v = int(dt.year) - int(age_c[0:4]) - (((int(dt.month)), int(dt.day)) < ((int(age_c[5:7])), int(age_c[
                                                                                                           8:10])))  # Subtract today's year to birth year, then compare current month & birthdate to birth month and birthdate
        return True, age_v
    except Exception as e:
        print("Error!!!, ", e)


# gender
def gend_v(data):
    gend_ = data
    try:
        if gend_.capitalize() in ("Male", "Female", "Other"):
            return True, gend_
        else:
            print("please enter valid gender")
            return False, gend_
    except Exception as e:
        print("Error!!!, ", e)


# initial deposit
def ini_dep(data, i):
    try:
        inidep_v = data
        if inidep_v.isnumeric() and int(inidep_v) >= i:
            return True, inidep_v
        else:
            return False, inidep_v
    except Exception as e:
        print("Error!!!, ", e)


# acc type
def toacc_v(data):
    try:
        acc_type = data
        if acc_type.capitalize() in ("Checkins", "Savings", "Money market"):
            return True, acc_type
        else:
            return False, acc_type
    except Exception as e:
        print("Error!!!, ", e)


# emp status
def employment(data):
    try:
        emp_status_v = data
        if emp_status_v.capitalize() in ("Student", "Self-employed", "Job", "Unemployed"):
            return True, emp_status_v
        else:
            return False, emp_status_v
    except Exception as e:
        print("Error!!!, ", e)


# password
def pin(data):
    acc_pin_v = data
    try:
        if acc_pin_v.isnumeric():
            if 5 <= len(acc_pin_v) <= 10:
                return True, acc_pin_v
            else:
                return False, acc_pin_v
    except Exception as e:
        print("Error!!!, ", e)


# acc status
def Acc_stat_v():
    accstatus_b = "Active"
    return True, accstatus_b


# email
def email_v(data):
    try:
        email_suffix = ["gmail.com", "yahoo.com", "hotmail.com", "aol.com", "hotmail.co.uk", "hotmail.fr", "msn.com",
                        "yahoo.fr", "wanadoo.fr", "orange.fr", "comcast.net", "yahoo.co.uk", "yahoo.com.br",
                        "yahoo.co.in", "live.com", "rediffmail.com",
                        "free.fr", "gmx.de", "web.de", "yandex.ru", "ymail.com", "libero.it", "outlook.com",
                        "outlook.ca", "uol.com.br", "bol.com.br", "mail.ru", "cox.net", "hotmail.it", "sbcglobal.net",
                        "sfr.fr", "live.fr", "verizon.net", "live.co.uk", "googlemail.com",
                        "yahoo.es", "ig.com.br", "live.nl", "bigpond.com", "terra.com.br", "yahoo.it", "neuf.fr",
                        "yahoo.de", "alice.it", "rocketmail.com", "att.net", "laposte.net", "facebook.com",
                        "bellsouth.net", "yahoo.in", "hotmail.es", "charter.net",
                        "yahoo.ca", "yahoo.com.au", "rambler.ru", "hotmail.de", "tiscali.it", "shaw.ca", "yahoo.co.jp",
                        "sky.com", "earthlink.net", "optonline.net", "freenet.de", "t-online.de", "aliceadsl.fr",
                        "virgilio.it", "home.nl", "qq.com", "telenet.be",
                        "me.com", "yahoo.com.ar", "tiscali.co.uk", "yahoo.com.mx", "voila.fr", "gmx.net", "mail.com",
                        "planet.nl", "tin.it", "live.it", "ntlworld.com", "arcor.de", "yahoo.co.id", "frontiernet.net",
                        "hetnet.nl", "live.com.au", "yahoo.com.sg",
                        "zonnet.nl", "club-internet.fr", "juno.com", "optusnet.com.au", "blueyonder.co.uk",
                        "bluewin.ch", "skynet.be", "sympatico.ca", "windstream.net", "mac.com", "centurytel.net",
                        "chello.nl", "live.ca", "aim.com", "bigpond.net.au"]
        email = data
        if "@" in email:
            if email.split("@", 2)[1] in email_suffix:
                sp_c = ["!", "@", "#", "$", "%", "^", "&", "*", "(", ")", "_", "+"]
                if not (any(em in email.split("@", 2)[0] for em in sp_c)):
                    return True, email
        else:
            print("Enter proper email...")
            return False, email
    except Exception as e:
        print("Error!!!, ", e)


# phone number
def phone(data):
    try:
        phn_v = data
        if len(phn_v) == 10:
            if phn_v.isnumeric():
                return True, phn_v
        return False, phn_v
    except Exception as e:
        print("Error!!!, ", e)


# acc number gen
def gen_acc():
    try:
        acc_list = []
        rasp.get_acc()
        x = rasp.data
        for i in range(len(x)):
            for j in range(len(x[i])):
                acc_list.append(x[i][j])
        while True:
            acc_no = random.randint(111111111, 999999999)
            if acc_no not in acc_list:
                return True, acc_no
    except Exception as e:
        print("Error!!!, ", e)


# save in database
def save_details(data, acc_num, stat):
    try:
        print(data)
        print(str(data[1][1]), str(data[2][1]), str(data[3][1]), data[4][1], str(data[5][1]), str(data[6][1]), int(data[7][1]), str(data[8][1]), str(data[9][1]), int(data[10][1]), str(data[11][1]), int(data[12][1]), stat[1], str(acc_num[1]), str(data[7][1]))
        # Inserting the values of new user
        rasp.insert_rec.execute(f""" INSERT INTO Bank(FIRST_NAME, MIDDLE_NAME, LAST_NAME, DOB, AGE, GENDER, INIT_DEP, ACC_TYPE,
            EMPLOYMENT_STATUS, PASSWORD, EMAIL, PHONE_NUM, CURR_LOGIN, ACC_STATUS, ACC_NUM, LAST_LOGIN, ACTIVITY, BALANCE) 
            VALUES('{str(data[1][1])}', '{str(data[2][1])}', '{str(data[3][1])}', '{data[4][1]}', {int(data[5][1])}, '{str(data[6][1])}', {int(data[7][1])}, '{str(data[8][1])}', '{str(data[9][1])}', {str(data[10][1])}, 
            '{str(data[11][1])}', {int(data[12][1])}, 'No', '{stat[1]}', {int(acc_num[1])}, 'None', 'ACCOUNT CREATED ON {datetime.datetime.now(pytz.timezone('America/Toronto')).strftime('%Y-%m-%d %H:%M:%S %Z')}\nDEPOSITED {str(data[7][1])}', {int(data[7][1])});""")
        rasp.mydb.commit()
        print("Details saved and committed successfully....")
        return True
    except Exception as e:
        print(f"Error occurred, {e}  Retrying...")


# commands
def change(id_, islog):
    lines = [f"User={id_}", f"is_logged={islog}", f"Ultra_access=156854735"]
    with open("Loginfo.txt", 'w') as f:
        f.writelines('\n'.join(lines))


def change_close(id_, islog, val):
    lines = [f"User={id_}", f"is_logged={islog}", f"Ultra_access=156854735", f"Closed={val}"]
    with open("Loginfo.txt", 'w') as f:
        f.writelines('\n'.join(lines))


# Acc Holder list
def acc_lst(window):
    window.withdraw()
    os.system('AccHodl.py')
    window.deiconify()


# Acc Holder list
def acc_close_r(window):
    try:
        window.withdraw()
        os.system('AccClose.py')
        with open('Loginfo.txt', 'r') as f:
            get_close = str(f.readlines()[1]).split("=")[1]
        if not get_close:
            window.deiconify()
            window.destroy()
            os.system('__init__.py')
        else:
            window.deiconify()
    except Exception as e:
        print(e)


def data_mod(col, acc_no):
    try:
        if col == 'FIRST_NAME':
            name = 'First name'
            while True:
                data = simpledialog.askstring(f'{name} Modification', name)
                fnx = fn_verify(data)
                if data is None:
                    return False
                elif fnx[0] is not True:
                    messagebox.showerror(title='Invalid data', message='Please enter valid Name...')
                else:
                    # save data in the database and return to modification
                    rasp.set_data(col, data, acc_no)
                    rasp.upd_act(name, acc_no)
                    return True
        elif col == 'MIDDLE_NAME':
            name = 'Middle name'
            while True:
                data = simpledialog.askstring(f'{name} Modification', name)
                mnx = mn_verify(data)
                if data is None:
                    return False
                elif mnx[0] is not True:
                    messagebox.showerror(title='Invalid data', message='Please enter valid Name...')
                else:
                    # save data in the database and return to modification
                    rasp.set_data(col, data, acc_no)
                    rasp.upd_act(name, acc_no)
                    return True
        elif col == 'LAST_NAME':
            name = 'Last name'
            while True:
                data = simpledialog.askstring(f'{name} Modification', name)
                lnx = ln_verify(data)
                if data is None:
                    return False
                elif lnx[0] is not True:
                    messagebox.showerror(title='Invalid data', message='Please enter valid Name...')
                else:
                    # save data in the database and return to modification
                    rasp.set_data(col, data, acc_no)
                    rasp.upd_act(name, acc_no)
                    return True
        elif col == 'GENDER':
            name = 'Gender'
            while True:
                data = simpledialog.askstring(f'{name} Modification', name)
                gndx = gend_v(data)
                if data is None:
                    return False
                elif gndx[0] is not True:
                    messagebox.showerror(title='Invalid data', message='Enter valid gender\n Male, Female or Other...')
                else:
                    # save data in the database and return to modification
                    rasp.set_data(col, data, acc_no)
                    rasp.upd_act(name, acc_no)
                    return True
        elif col == 'EMAIL':
            name = 'Email'
            while True:
                data = simpledialog.askstring(f'{name} Modification', name)
                emailx = email_v(data)
                if data is None:
                    return False
                if emailx[0] is not True:
                    messagebox.showerror(title='Invalid data', message='Enter valid email with format "abc@gmail.com"...')
                else:
                    # save data in the database and return to modification
                    rasp.set_data(col, data, acc_no)
                    return True
        elif col == 'PHONE_NUM':
            name = 'Phone number'
            while True:
                data = simpledialog.askstring(f'{name} Modification', name)
                phnx = phone(data)
                if data is None:
                    return False
                elif phnx[0] is not True:
                    messagebox.showerror(title='Invalid data', message='Enter valid phone number or 10 digits only...')
                else:
                    # save data in the database and return to modification
                    rasp.set_data(col, data, acc_no)
                    rasp.upd_act(name, acc_no)
                    return True
        elif col == 'DOB':
            name = 'Date of Birth'
            while True:
                data = simpledialog.askstring(f'{name} Modification', name)
                dobx = dob_verify(data)
                if data is None:
                    return False
                elif dobx[0] is not True:
                    messagebox.showerror(title='Invalid data', message='Enter valid birth date\nFormat: YYYY-MM-DD...')
                else:
                    # run the age function and update the age also
                    # save data in the database and return to modification
                    rasp.set_data(col, data, acc_no)
                    rasp.upd_act(name, acc_no)
                    return True
        elif col == 'EMPLOYMENT_STATUS':
            name = 'Employment Status'
            while True:
                data = simpledialog.askstring(f'{name} Modification', name)
                empx = employment(data)
                if data is None:
                    return False
                elif empx[0] is not True:
                    messagebox.showerror(title='Invalid data', message='Enter valid Employment status...')
                else:
                    # save data in the database and return to modification
                    rasp.set_data(col, data, acc_no)
                    rasp.upd_act(name, acc_no)
                    return True
        elif col == 'ACC_STATUS':
            name = 'Account Status'
            while True:
                data = simpledialog.askstring(f'{name} Modification', name)
                if data is None:
                    return False
                elif str(data) not in ['Active', 'Inactive']:
                    messagebox.showerror(title='Invalid data', message='Enter valid Account status from "Active" or "Inactive"...')
                else:
                    # save data in the database and return to modification
                    rasp.set_data(col, data, acc_no)
                    rasp.upd_act(name, acc_no)
                    return True
        elif col == 'PASSWORD':
            name = 'Pin'
            while True:
                data = simpledialog.askstring(f'{name} Modification', name)
                passx = pin(data)
                if data is None:
                    return False
                elif passx[0] is not True:
                    messagebox.showerror(title='Invalid data', message='Enter valid Password...')
                else:
                    # save data in the database and return to modification
                    rasp.set_data(col, data, acc_no)
                    rasp.upd_act(name, acc_no)
                    return True
    except Exception as e:
        print("Error Occurred!!!", e)

# update Bank set PASSWORD=123456  WHERE ACC_NUM=123456789;
