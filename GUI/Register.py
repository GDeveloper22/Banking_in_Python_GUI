import threading
import time
import tkinter as tk
from tkinter import Button, Label, Entry, Checkbutton, IntVar, Text
from PIL import Image, ImageTk, ImageOps
from Commands import *
import keyboard

# block keys
keyboard.block_key('win')
keyboard.block_key('alt')
keyboard.block_key('ctrl')
keyboard.block_key('esc')
keyboard.block_key('tab')

global acc_num_g, acc_stat_n


def regi():
    try:
        def regist_config(window):
            window.geometry("650x800+715+120")
            window.overrideredirect(True)

        regist = tk.Tk()
        regist_config(regist)

        # logo image
        def r_logo_img():
            i_open = Image.open('..\\img\\logo.png')
            i_exp = ImageOps.expand(i_open, border=100, fill='black')
            img = ImageTk.PhotoImage(image=i_exp.resize((180, 180)))
            return img

        # placing image in label
        r_imge = r_logo_img()
        r_logo_label = Label(image=r_imge, height=130, width=120)
        r_logo_label.place(x=260, y=30)

        # Bank Name label
        Bank_Name = Label(regist, text="Swizz Bank", fg='Black', font=("Arial", 15))
        Bank_Name.place(x=275, y=140)

        # first name
        fn = Label(regist, text="First Name", fg='Black', font=("Arial", 12))
        fn.place(x=65, y=205)

        fn_b = Entry(regist, fg='Black', font=("Arial", 12))
        fn_b.place(x=160, y=205)

        # middle name
        mdn = Label(regist, text="Middle Name\t\t\t   Left empty if you don't have", fg='Black', font=("Arial", 12))
        mdn.place(x=48, y=245)

        md_b = Entry(regist, fg='Black', font=("Arial", 12))
        md_b.place(x=160, y=245)

        # last name
        ltn = Label(regist, text="Last Name", fg='Black', font=("Arial", 12))
        ltn.place(x=65, y=285)

        lt_b = Entry(regist, fg='Black', font=("Arial", 12))
        lt_b.place(x=160, y=285)

        # dob shows the watermark of date format.
        dob = Label(regist, text="DOB(YYYY-MM-DD)", fg='Black', font=("Arial", 11))
        dob.place(x=8, y=320)

        dob_b = Entry(regist, fg='Black', font=("Arial", 12))
        dob_b.place(x=160, y=320)

        # age (it will be placed automatically after typing the date of birth), it will be read only
        age = Label(regist, text="Age\t\t\t     Calculated on base of Birth date", fg='Black', font=("Arial", 12))
        age.place(x=112, y=355)

        age_b = Entry(regist, fg='Black', font=("Arial", 12), state='disabled')
        age_b.place(x=160, y=355)

        # gender
        gend = Label(regist, text="Gender\t\t\t          Male, Female, Other", fg='Black', font=("Arial", 12))
        gend.place(x=90, y=395)

        gend_b = Entry(regist, fg='Black', font=("Arial", 12))
        gend_b.place(x=160, y=395)

        # init deposit
        inidep = Label(regist, text="Initial Deposit\t\t\t   Min Deposit $100", fg='Black', font=("Arial", 12))
        inidep.place(x=47, y=435)

        inidep_b = Entry(regist, fg='Black', font=("Arial", 12))
        inidep_b.place(x=160, y=435)

        # acc type
        ac_type = Label(regist, text="Account Type\t\t\t   Checkins, Savings, Money Market", fg='Black', font=("Arial", 12))
        ac_type.place(x=47, y=475)

        ac_type_b = Entry(regist, fg='Black', font=("Arial", 12))
        ac_type_b.place(x=160, y=475)

        # emp status
        emp = Label(regist, text="Employment status\t\t\t            Student, Self-employed, Job, Unemployed", fg='Black', font=("Arial", 12))
        emp.place(x=10, y=515)

        emp_b = Entry(regist, fg='Black', font=("Arial", 12))
        emp_b.place(x=160, y=515)

        # pin
        Password = Label(regist, text="Password\t\t\t                Must be of 5- 10 digits only", fg='Black', font=("Arial", 12))
        Password.place(x=69, y=555)

        pwd_box = Entry(regist, fg='Black', font=("Arial", 12), show='*')
        pwd_box.place(x=160, y=555)

        # email
        Password = Label(regist, text="Email\t\t\t         Format: abc@gmail.com", fg='Black', font=("Arial", 12))
        Password.place(x=98, y=595)

        eml_box = Entry(regist, fg='Black', font=("Arial", 12))
        eml_box.place(x=160, y=595)

        # phone
        phn = Label(regist, text="Phone Number\t\t\t       Type only number without countrycode", fg='Black', font=("Arial", 12))
        phn.place(x=35, y=635)

        phn_box = Entry(regist, fg='Black', font=("Arial", 12))
        phn_box.place(x=160, y=635)

        # T&C required
        var_tc = IntVar()
        tc = Checkbutton(variable=var_tc, text="Please agree with our 'TERMS AND CONDITIONS'", fg='Black', font=("Helvetica", 10))
        tc.place(x=155, y=685)

        # register, close buttons
        # button image
        def r_butt_img(image, x=95, y=45):
            i_open = Image.open(f'..\\img\\{image}')
            i_exp = ImageOps.expand(i_open)
            img = ImageTk.PhotoImage(image=i_exp.resize((x, y)))
            return img

        # commands
        # verify data and save in database.
        # register
        def reg_success(window):
            vals = details_verify()
            if vals is None:
                pass
            else:
                if vals[0] is True:
                    a = show_details(regist, vals)
                    if a:
                        save_details(vals, acc_num_g, acc_stat_n)
                        print("Account Registration Successful...")
                        window.destroy()
                        return os.system('__init__.py')

        # reg_cancel
        def reg_cancel(window):
            print("Registration cancelled...")
            window.destroy()
            return os.system('__init__.py')

        regi_ = r_butt_img('Register.png', 110, 45)
        canc_ = r_butt_img('CANCEL.png', 110, 45)

        reg_b = Button(image=regi_, borderwidth=0, command=lambda: reg_success(regist))
        reg_b.place(x=175, y=730)

        canc_b = Button(image=canc_, borderwidth=0, command=lambda: reg_cancel(regist))
        canc_b.place(x=340, y=730)

        def details_verify():
            fn_f = fn_verify(str(fn_b.get()))
            md_f = mn_verify(str(md_b.get()))
            ln_f = ln_verify(str(lt_b.get()))
            dob_f = dob_verify(str(dob_b.get()))
            age_f = age_calc(str(dob_b.get()))
            gend_f = gend_v(str(gend_b.get()))
            inidep_f = ini_dep(inidep_b.get(), 100)
            acc_typ_f = toacc_v(str(ac_type_b.get()))
            emp_stat_f = employment(str(emp_b.get()))
            pass_f = pin(str(pwd_box.get()))
            email_f = email_v(str(eml_box.get()))
            phn_f = phone(phn_box.get())
            chb_f = var_tc.get()
            # print(fn_f, md_f, ln_f, dob_f, age_f, gend_f, inidep_f, acc_typ_f, emp_stat_f, pass_f, email_f, phn_f, chb_f)
            try:
                if (fn_f[0] and md_f[0] and ln_f[0] and dob_f[0] and age_f[0] and gend_f[0] and inidep_f[0] and acc_typ_f[0] and emp_stat_f[0] and pass_f[0] and email_f[0] and phn_f[0]) is True and chb_f == 1:
                    age_b.config(state='normal')
                    age_b.insert(0, str(age_f[1]))
                    age_b.config(state='disabled')
                    regist.update()
                    time.sleep(2)
                    return True, fn_f, md_f, ln_f, dob_f, age_f, gend_f, inidep_f, acc_typ_f, emp_stat_f, pass_f, email_f, phn_f, chb_f
                else:
                    if fn_f[0] is False or md_f[0] is False or ln_f[0] is False:
                        if fn_f[0] is False:
                            messagebox.showwarning(title="Value Error", message="Enter valid First name")
                        elif md_f[0] is False:
                            messagebox.showwarning(title="Value Error", message="Enter valid Middle name")
                        else:
                            messagebox.showwarning(title="Value Error", message="Enter valid Last name")
                    elif dob_f[0] is False:
                        messagebox.showwarning(title="Value Error", message="Enter valid Date of Birth")
                    elif age_f[0] is False:
                        messagebox.showwarning(title="Value Error", message="Enter valid date of birth to calculate age")
                    elif gend_f[0] is False:
                        messagebox.showwarning(title="Value Error", message="Enter valid gender from given options")
                    elif inidep_f[0] is False:
                        messagebox.showwarning(title="Value Error", message="Deposit amount must be more than $100")
                    elif acc_typ_f[0] is False:
                        messagebox.showwarning(title="Value Error", message="Choose valid account type from the options")
                    elif emp_stat_f[0] is False:
                        messagebox.showwarning(title="Value Error", message="Choose valid employment status")
                    elif pass_f[0] is False:
                        messagebox.showwarning(title="Value Error", message="Password must be 5-10 digits")
                    elif email_f[0] is False:
                        messagebox.showwarning(title="Value Error", message="Enter valid email with proper format")
                    elif phn_f[0] is False:
                        messagebox.showwarning(title="Value Error", message="Phone number must be of 10 digits only")
                    elif chb_f == 0:
                        messagebox.showwarning(title="Value Error", message="Please accept terms and conditions")
                    return False, fn_f, md_f, ln_f, dob_f, age_f, gend_f, inidep_f, acc_typ_f, emp_stat_f, pass_f, email_f, phn_f, chb_f
            except Exception as e:
                print(e)
                messagebox.showwarning(title="Empty entry", message="Please enter values")

        # show details after registering
        def show_details(window, data):
            global acc_num_g, acc_stat_n
            try:
                for widgets in window.winfo_children():
                    widgets.destroy()
                window.update()

                Bank_Name_n = Label(window, text="SWIZZ BANK", fg='Black', font=("Arial Black", 17))
                Bank_Name_n.place(x=230, y=50)

                detail_lbl = Text(window, height=30, width=67, borderwidth=0, font=('Arial', 12))
                detail_lbl.place(x=30, y=100)
                # acc gen
                acc_num_gen = gen_acc()
                acc_num_g = acc_num_gen
                # acc stat
                acc_stat_ = Acc_stat_v()
                acc_stat_n = acc_stat_

                detail_lbl.insert(tk.INSERT, f"""FIRST NAME: {data[1][1]}\n\nMIDDLE NAME: {data[2][1]}\n\nLAST NAME: {data[3][1]}\n\nDATE OF BIRTH: {data[4][1]}\n\nAGE:{data[5][1]}\n\nGENDER: {data[6][1]}
                \nINITIAL DEPOSIT AMOUNT: ${data[7][1]}\n\nACCOUNT TYPE: {data[8][1]}\n\nEMPLOYMENT STATUS: {data[9][1]}\n\nPASSWORD: {data[10][1]}\n\nEMAIL: {data[11][1]}\n\nPHONE NUMBER: {data[12][1]}
                \nACCOUNT NUMBER: {acc_num_gen[1]}\n\nACCOUNT STATUS:{acc_stat_[1]}\n\nTERMS AND CONDITIONS: AGREED""")
                detail_lbl.config(state='disabled')

                def timer():
                    timer_ = Label(window, text="", borderwidth=0, font=('Arial Black', 13))
                    timer_.place(x=165, y=700)
                    for i in range(20, -1, -1):
                        timer_.config(text=f"Please check the details\nWindow will be closed after {i} sec")
                        time.sleep(1)
                        window.update()
                    time.sleep(0.5)
                timer()
                # threading.Thread(target=timer, daemon=False).start()
                return True
            except Exception as e:
                print(e)

        regist.mainloop()  # winding the tkinter window
    except KeyboardInterrupt as e:
        print(e)
        change(0, False)


regi()
