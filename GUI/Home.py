import time
import tkinter as tk
from tkinter import Button, Label, Entry, Frame, Text
from PIL import Image, ImageTk, ImageOps
from Commands import *
import threading
from Dataset.Dataset_init import rasp
import keyboard

# block keys
keyboard.block_key('win')
keyboard.block_key('alt')
keyboard.block_key('ctrl')
keyboard.block_key('esc')
keyboard.block_key('tab')


def hme():
    try:
        def home_config(window):
            window.geometry("1200x800+350+150")
            window.overrideredirect(True)

        home = tk.Tk()
        home_config(home)

        FrameA = Frame(home, highlightbackground="Black", highlightthickness=5, width=1440, height=150)
        FrameA.pack(padx=5, pady=5)

        # logo image
        def logo_img():
            i_open = Image.open('..\\img\\logo.png')
            i_exp = ImageOps.expand(i_open, border=0, fill='black')
            img = ImageTk.PhotoImage(image=i_exp.resize((150, 150)))
            return img

        # placing image in label
        imge = logo_img()
        logo_label = Label(FrameA, image=imge, height=125, width=125, borderwidth=0)
        logo_label.place(x=30, y=15)

        # Bank Name label
        Bank_Name = Label(FrameA, text="SWIZZ BANK", fg='Black', font=("Arial Black", 19))
        Bank_Name.place(x=160, y=45)

        # button
        # button image
        def home_img(image, x=95, y=45):
            i_open = Image.open(f'..\\img\\{image}')
            i_exp = ImageOps.expand(i_open)
            img = ImageTk.PhotoImage(image=i_exp.resize((x, y)))
            return img

        logout = home_img('LOGOUT.png', 150, 55)
        help_ = home_img('HELP.png', 150, 55)
        active = home_img('GREEN.png', 30, 30)
        inactive = home_img('RED.png', 30, 30)
        clock = home_img('CLOCK.png', 140, 130)

        # command logout
        def u_logout(window):
            active_s.config(image=inactive)
            active_s_l.config(text="Inactive currently")
            window.update()
            # resetting status to the logout as false and changing status
            change(0, False)
            rasp.set_data('CURR_LOGIN', 'NO', int(get_usr))
            time.sleep(0.5)
            window.destroy()
            return os.system('__init__.py')

        # help command
        def help_c(window):
            window.config()
            messagebox.showinfo(title='Support Info', message='For assistance please contact "Swizzbank@gmail.ca".')

        # Logout
        logout_b = Button(FrameA, image=logout, borderwidth=0, command=lambda: u_logout(home))
        logout_b.place(x=1000, y=5)

        # help
        help_b = Button(FrameA, image=help_, borderwidth=0, command=lambda: help_c(home))
        help_b.place(x=1000, y=70)

        # active
        active_s = Label(FrameA, image=active, borderwidth=0)
        active_s.place(x=390, y=45)
        # label
        active_s_l = Label(FrameA, text="Active currently", borderwidth=0, font=('Arial Black', 15))
        active_s_l.place(x=430, y=43)

        # clock
        clk = Label(FrameA, image=clock, borderwidth=0)
        clk.place(x=800, y=5)

        def clock_upd():
            # getting time and date
            t_d = datetime.datetime.now(pytz.timezone('America/Toronto')).strftime('%Y-%m-%d %H:%M:%S %Z')
            date_ = t_d[0:10]
            time_ = t_d[10:19]
            zone = t_d[20:23]
            # time date label
            clok = Label(FrameA, text=f"{date_}\n{time_} {zone}", bg='black', fg='white', borderwidth=0, font=('Arial Black', 10))
            clok.place(x=817, y=45)
            clok.after(100, clock_upd)

        # Account details frame
        FrameB = Frame(home, highlightbackground="Black", highlightthickness=5, width=500, height=390)
        FrameB.place(x=5, y=150)

        # Acc_label
        Acc_label = Label(FrameB, text='ACCOUNT DETAILS', font=("Arial Black", 15), borderwidth=0)
        Acc_label.place(x=130, y=12)
        try:
            with open('Loginfo.txt', 'r') as f:
                get_usr = str(f.readline()).split("=")[1]
                get_logstat = str(f.readline()).split("=")[1]
                get_access = str(f.readline()).split("=")[1]
        except Exception as exc:
            print(exc)
        # it will add the details in the labels only and update the root after wards.
        # First name
        fn_label = Label(FrameB, text=f"First Name: {rasp.get_data('FIRST_NAME', int(get_usr))}", font=("Arial", 13), borderwidth=0)
        fn_label.place(x=90, y=40)

        # middle name
        mn_label = Label(FrameB, text=f"Middle Name: {rasp.get_data('MIDDLE_NAME', int(get_usr))}", font=("Arial", 13), borderwidth=0)
        mn_label.place(x=65, y=70)

        # last name
        ln_label = Label(FrameB, text=f"Last Name: {rasp.get_data('LAST_NAME', int(get_usr))}", font=("Arial", 13), borderwidth=0)
        ln_label.place(x=85, y=100)

        # DOB
        dob_label = Label(FrameB, text=f"Date of Birth: {rasp.get_data('DOB', int(get_usr))}", font=("Arial", 13), borderwidth=0)
        dob_label.place(x=75, y=127)

        # Age
        age_label = Label(FrameB, text=f"Age: {rasp.get_data('AGE', int(get_usr))}", font=("Arial", 13), borderwidth=0)
        age_label.place(x=145, y=150)

        # Gender
        gender_label = Label(FrameB, text=f"Gender: {rasp.get_data('GENDER', int(get_usr))}", font=("Arial", 13), borderwidth=0)
        gender_label.place(x=118, y=175)

        # Phone NUmber
        pn_label = Label(FrameB, text=f"Phone No: {rasp.get_data('PHONE_NUM', int(get_usr))}", font=("Arial", 13), borderwidth=0)
        pn_label.place(x=98, y=205)

        # email
        eml_label = Label(FrameB, text=f"Email: {rasp.get_data('EMAIL', int(get_usr))}", font=("Arial", 13), borderwidth=0)
        eml_label.place(x=133, y=235)

        # emp Status
        emp_label = Label(FrameB, text=f"Employment Status: {rasp.get_data('EMPLOYMENT_STATUS', int(get_usr))}", font=("Arial", 13), borderwidth=0)
        emp_label.place(x=18, y=260)

        # Account Type
        act_label = Label(FrameB, text=f"Account Type: {rasp.get_data('ACC_TYPE', int(get_usr))}", font=("Arial", 13), borderwidth=0)
        act_label.place(x=68, y=290)

        # Acc status
        acc_label = Label(FrameB, text=f"Account Status: {rasp.get_data('ACC_STATUS', int(get_usr))}", font=("Arial", 13), borderwidth=0)
        acc_label.place(x=58, y=320)

        FrameC = Frame(home, highlightbackground="Black", highlightthickness=5, width=1190, height=295)
        FrameC.place(x=5, y=500)

        # Account Activity
        acc_act_lab = Label(FrameC, text="ACCOUNT ACTIVITY", font=("Arial Black", 13), borderwidth=0)
        acc_act_lab.place(x=10, y=5)

        acc_act_ent = Text(FrameC, width=145, height=13, state='disabled', borderwidth=0)
        acc_act_ent.place(x=10, y=35)

        # insert data
        acc_act_ent.config(state='normal')
        acc_act_ent.insert(tk.INSERT, str(rasp.get_data('ACTIVITY', int(get_usr))))
        acc_act_ent.config(state='disabled')

        FrameD = Frame(home, highlightbackground="Black", highlightthickness=5, width=150, height=355)
        FrameD.place(x=500, y=150)

        # Modify Account
        Mfy_acc = home_img("MODIFY ACCOUNT.png", 120, 60)
        mfy = Button(FrameD, image=Mfy_acc, borderwidth=0, command=lambda: modify_menu(home))
        mfy.place(x=5, y=45)

        # Close Account
        cl_acc = home_img("CLOSE ACCOUNT.png", 120, 60)
        cl_b = Button(FrameD, image=cl_acc, borderwidth=0, command=lambda: acc_close_r(home))
        cl_b.place(x=5, y=135)

        # Account holder list
        ac_hdl_acc = home_img("ACC HOLDER LIST.png", 120, 60)
        ac_hdl_acc_b = Button(FrameD, image=ac_hdl_acc, borderwidth=0, command=lambda: acc_lst(home))
        ac_hdl_acc_b.place(x=5, y=225)
        try:
            if int(get_usr) != int(get_access):
                ac_hdl_acc_b.destroy()
        except Exception as e:
            print(e)

        def r_update():
            fn_label.config(text=f"First Name: {str(rasp.get_data('FIRST_NAME', int(get_usr)))}")
            mn_label.config(text=f"Middle Name: {str(rasp.get_data('MIDDLE_NAME', int(get_usr)))}")
            ln_label.config(text=f"Last Name: {str(rasp.get_data('LAST_NAME', int(get_usr)))}")
            dob_label.config(text=f"Date of Birth: {str(rasp.get_data('DOB', int(get_usr)))}")
            age_label.config(text=f"Age: {str(rasp.get_data('AGE', int(get_usr)))}")
            gender_label.config(text=f"Gender: {str(rasp.get_data('GENDER', int(get_usr)))}")
            pn_label.config(text=f"Phone No: {str(rasp.get_data('PHONE_NUM', int(get_usr)))}")
            eml_label.config(text=f"Email: {str(rasp.get_data('EMAIL', int(get_usr)))}")
            emp_label.config(text=f"Employment Status: {str(rasp.get_data('EMPLOYMENT_STATUS', int(get_usr)))}")
            act_label.config(text=f"Account Type: {str(rasp.get_data('ACC_TYPE', int(get_usr)))}")
            acc_label.config(text=f"Account Status: {str(rasp.get_data('ACC_STATUS', int(get_usr)))}")
            acc_act_ent.config(state='normal')
            acc_act_ent.delete(1.0, "end")
            acc_act_ent.insert(tk.INSERT, str(rasp.get_data('ACTIVITY', int(get_usr))))
            acc_act_ent.config(state='disabled')
            acc_bal_label.config(text=f"ACCOUNT BALANCE: ${str(rasp.get_data('BALANCE', int(get_usr)))}")
            return True

        def modify_menu(window):
            window.destroy()
            os.system('Modification.py')
            os.system('Home.py')

        # deposit frame
        def deposit(window, data, ac_no):
            try:
                x = str(rasp.get_data('ACC_STATUS', int(get_usr)))
                print(x)
                if x == 'Active':
                    x = ini_dep(data.get(), 1)
                    if x[0] is True:
                        rasp.set_bal('BALANCE', x[1], ac_no)
                        r_update()
                        window.update()
                    else:
                        messagebox.showerror(title="Warning", message="Enter proper Deposit amount")
                else:
                    messagebox.showerror(title="Warning", message="Account Inactive")
            except Exception as e:
                print(e)

        FrameE = Frame(home, highlightbackground="Black", highlightthickness=5, width=280, height=200)
        FrameE.place(x=645, y=150)

        Dep_label = Label(FrameE, text="DEPOSIT", font=("Arial Black", 15), borderwidth=0)
        Dep_label.place(x=80, y=10)

        damt_label = Label(FrameE, text="Amount", font=("Arial", 15), borderwidth=0)
        damt_label.place(x=5, y=65)

        dmt_entry = Entry(FrameE, fg='Black', font=("Arial", 12))
        dmt_entry.place(x=80, y=67)

        dbut = home_img("DEPOSIT.png", 115, 60)
        dbutt = Button(FrameE, image=dbut, borderwidth=0, command=lambda: deposit(home, dmt_entry, get_usr))
        dbutt.place(x=80, y=110)

        # withdraw frame
        def withdraw(window, data, ac_no):
            try:
                if str(rasp.get_data('ACC_STATUS', int(get_usr))) == 'Active':
                    x = ini_dep(data.get(), 1)
                    a = messagebox.askquestion(title="Verification", message="Are you sure")
                    if a == 'no':
                        return None
                    else:
                        if x[0] is True:
                            if int(x[1]) < int(rasp.get_data('BALANCE', int(get_usr))) and int(rasp.get_data('BALANCE', int(get_usr))) - int(x[1]) >= 1:
                                rasp.set_bal_with('BALANCE', x[1], ac_no)
                                r_update()
                                window.update()
                        else:
                            messagebox.showerror(title="Warning", message="Enter proper Withdrawal amount")
                else:
                    messagebox.showerror(title="Warning", message="Account Inactive")
            except Exception as e:
                print(e)

        FrameF = Frame(home, highlightbackground="Black", highlightthickness=5, width=275, height=200)
        FrameF.place(x=920, y=150)

        with_label = Label(FrameF, text="WITHDRAW", font=("Arial Black", 15), borderwidth=0)
        with_label.place(x=70, y=10)

        wamt_label = Label(FrameF, text="Amount", font=("Arial", 15), borderwidth=0)
        wamt_label.place(x=3, y=65)

        wmt_entry = Entry(FrameF, fg='Black', font=("Arial", 12))
        wmt_entry.place(x=76, y=67)

        wbut = home_img("WITHDRAW.png", 130, 60)
        wbutt = Button(FrameF, image=wbut, borderwidth=0, command=lambda: withdraw(home, wmt_entry, get_usr))
        wbutt.place(x=75, y=110)

        # Balance frame
        FrameG = Frame(home, highlightbackground="Black", highlightthickness=5, width=550, height=160)
        FrameG.place(x=645, y=345)

        bal_label = Label(FrameG, text="BALANCE", font=("Arial Black", 15), borderwidth=0)
        bal_label.place(x=180, y=10)

        acc_nu_label = Label(FrameG, text=f"ACCOUNT NUMBER: {rasp.get_data('ACC_NUM', int(get_usr))}", font=("Arial", 15), borderwidth=0)
        acc_nu_label.place(x=20, y=55)

        acc_bal_label = Label(FrameG, text=f"ACCOUNT BALANCE: ${rasp.get_data('BALANCE', int(get_usr))}", font=("Arial", 15), borderwidth=0)
        acc_bal_label.place(x=18, y=95)

        # clock threads
        clc_threads = threading.Thread(target=clock_upd, daemon=False)

        # home.withdraw() # to hide window
        # home.deiconify() # to reveal it again

        # initializing the process and threads
        clc_threads.start()
        home.mainloop()
    except KeyboardInterrupt as e:
        print(e)
        rasp.set_data('CURR_LOGIN', 'NO', int(get_usr))
        change(0, False)


hme()
