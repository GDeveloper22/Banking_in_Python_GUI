import tkinter as tk
from tkinter import Button, Label
from PIL import Image, ImageTk, ImageOps
from Commands import data_mod, change
import keyboard

# block keys
keyboard.block_key('win')
keyboard.block_key('alt')
keyboard.block_key('ctrl')
keyboard.block_key('esc')
keyboard.block_key('tab')


def mod():
    try:
        def modif_config(window):
            window.geometry("600x500+670+300")
            window.overrideredirect(True)

        modif = tk.Tk()
        modif_config(modif)

        # logo image
        def logo_img():
            i_open = Image.open('..\\img\\logo.png')
            i_exp = ImageOps.expand(i_open, border=100, fill='black')
            img = ImageTk.PhotoImage(image=i_exp.resize((170, 170)))
            return img

        # Modification Name label
        Bank_Name = Label(modif, text="ACCOUNT\nMODIFICATION\nMENU", fg='Black', font=("Helvetica", 18))
        Bank_Name.place(x=20, y=10)
        # placing image in label
        ime = logo_img()
        logo_label = Label(image=ime, height=130, width=120)
        logo_label.place(x=250, y=10)

        # buttons
        def butt_img(image, x=110, y=45):
            i_open = Image.open(f'..\\img\\{image}')
            i_exp = ImageOps.expand(i_open)
            img = ImageTk.PhotoImage(image=i_exp.resize((x, y)))
            return img

        # initializing images
        f_name = butt_img("FIRST NAME.png", 120, 45)
        m_name = butt_img("MID NAME.png", 140, 45)
        l_name = butt_img("LAST NAME.png", 125, 50)
        gender = butt_img("GENDER.png", 120, 50)
        mail = butt_img("EMAIL.png", 120, 50)
        phno = butt_img("PHONE NO.png", 115,  50)
        dob = butt_img("DATE OF BIRTH.png", 140, 50)
        emp_stat = butt_img("EMP STATUS.png", 130, 55)
        acc_stat = butt_img("ACCOUNT STATUS.png", 125, 55)
        pin_chng = butt_img("PIN.png", 105, 50)
        close_m = butt_img("CLOSE MODIFICATION.png", 210, 50)

        # fetching the account info
        try:
            with open('Loginfo.txt', 'r') as f:
                get_usr = str(f.readline()).split("=")[1]
        except Exception as exc:
            print(exc)
        # creating buttons
        f_name_b = Button(image=f_name, borderwidth=0, command=lambda: data_mod('FIRST_NAME', int(get_usr)))
        m_name_b = Button(image=m_name, borderwidth=0, command=lambda: data_mod('MIDDLE_NAME', int(get_usr)))
        l_name_b = Button(image=l_name, borderwidth=0, command=lambda: data_mod('LAST_NAME', int(get_usr)))
        gender_b = Button(image=gender, borderwidth=0, command=lambda: data_mod('GENDER', int(get_usr)))
        mail_b = Button(image=mail, borderwidth=0, command=lambda: data_mod('EMAIL', int(get_usr)))
        phno_b = Button(image=phno, borderwidth=0, command=lambda: data_mod('PHONE_NUM', int(get_usr)))
        dob_b = Button(image=dob, borderwidth=0, command=lambda: data_mod('DOB', int(get_usr)))
        emp_stat_b = Button(image=emp_stat, borderwidth=0, command=lambda: data_mod('EMPLOYMENT_STATUS', int(get_usr)))
        acc_stat_b = Button(image=acc_stat, borderwidth=0, command=lambda: data_mod('ACC_STATUS', int(get_usr)))
        pin_chng_b = Button(image=pin_chng, borderwidth=0, command=lambda: data_mod('PASSWORD', int(get_usr)))
        close_m_b = Button(image=close_m, borderwidth=0, command=lambda: close_mod(modif))

        # packing buttons
        f_name_b.place(x=80, y=160)
        m_name_b.place(x=225, y=160)
        l_name_b.place(x=390, y=160)
        gender_b.place(x=85, y=230)
        mail_b.place(x=242, y=230)
        phno_b.place(x=395, y=230)
        dob_b.place(x=75, y=300)
        emp_stat_b.place(x=235, y=300)
        acc_stat_b.place(x=390, y=300)
        pin_chng_b.place(x=150, y=375)
        close_m_b.place(x=280, y=375)

        # commands
        def close_mod(window):
            window.destroy()

        """ Ask value in messagebox
        name = askstring('Name', 'What is your name?')
        showinfo('Hello!', 'Hi, {}'.format(name))
        """
        modif.mainloop()
    except KeyboardInterrupt as e:
        print(e)
        change(0, False)


mod()
