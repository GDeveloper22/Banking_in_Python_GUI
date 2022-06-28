import os
import tkinter as tk
from tkinter import Button, Label, Entry, messagebox
from PIL import Image, ImageTk, ImageOps
from Dataset.Dataset_init import rasp
import datetime
import pytz
import keyboard
from Commands import change

# block keys
keyboard.block_key('win')
keyboard.block_key('alt')
keyboard.block_key('ctrl')
keyboard.block_key('esc')
keyboard.block_key('tab')


def log_screen():
    try:
        def root_config(window):
            window.geometry("400x400+700+300")
            window.overrideredirect(True)

        root = tk.Tk()
        root_config(root)

        # logo image
        def logo_img():
            i_open = Image.open('..\\img\\logo.png')
            i_exp = ImageOps.expand(i_open, border=100, fill='black')
            img = ImageTk.PhotoImage(image=i_exp.resize((180, 180)))
            return img

        # placing image in label
        imge = logo_img()
        logo_label = Label(image=imge, height=130, width=120)
        logo_label.place(x=150, y=30)

        # Bank Name label
        Bank_Name = Label(root, text="Swizz Bank", fg='Black', font=("Arial", 15))
        Bank_Name.place(x=162, y=140)

        # User Id
        U_ID = Label(root, text="Account Number", fg='Black', font=("Arial", 12))
        U_ID.place(x=20, y=200)

        # Id insert box
        U_ID_box = Entry(root, fg='Black', font=("Arial", 12))
        U_ID_box.place(x=160, y=200)

        # Password
        Password = Label(root, text="Password", fg='Black', font=("Arial", 12))
        Password.place(x=64, y=235)

        # password insert box
        pwd_box = Entry(root, fg='Black', font=("Arial", 12), show='*')
        pwd_box.place(x=160, y=235)

        # register, close and login buttons
        # button image
        def butt_img(image, x=95, y=45):
            i_open = Image.open(f'..\\img\\{image}')
            i_exp = ImageOps.expand(i_open)
            img = ImageTk.PhotoImage(image=i_exp.resize((x, y)))
            return img

        login = butt_img('LOGIN.png')
        register = butt_img('Register.png', 110, 45)
        close = butt_img('CLOSE.png')

        # login
        def log_in(window):
            uid = U_ID_box.get()
            pwd_ = pwd_box.get()
            if uid == '' or pwd_ == '':
                messagebox.showwarning(message="Account number or password can't be empty.")
            else:
                try:
                    rasp.get_log_detail(uid, pwd_)
                    if int(rasp.data[0][0]) == int(uid) and int(rasp.data[0][1]) == int(pwd_):
                        print("Log in Successful")
                        # updating the global var
                        change(uid, True)
                        # changing current status to login as true and adding the last login value as current time
                        rasp.set_data('CURR_LOGIN', 'YES', int(uid))
                        rasp.set_data('LAST_LOGIN', str(datetime.datetime.now(pytz.timezone("America/Toronto")).strftime("%Y-%m-%d %H:%M:%S %Z")), int(uid))
                        # releasing the window and opening the home
                        window.destroy()
                        os.system('Home.py')
                except Exception as e:
                    messagebox.showinfo(title="Error!", message="User with this Account number and password not found.")
                    print(e)

        # close
        def close_(window):
            try:
                rasp.insert_rec.close()
                change(0, False)
                print("closing...")
                return window.destroy()
            except AttributeError as e:
                print(f"Error: {e}\nForce closing...")
                return window.destroy()

        # register@login
        def regis(window):
            window.destroy()
            print("Registering")
            os.system('Register.py')

        log = Button(image=login, borderwidth=0, command=lambda: log_in(root))
        log.place(x=100, y=280)

        close_b = Button(image=close, borderwidth=0, command=lambda: close_(root))
        close_b.place(x=220, y=280)

        register_b = Button(image=register, borderwidth=0, command=lambda: regis(root))
        register_b.place(x=150, y=340)

        root.mainloop()  # winding the tkinter window
    except KeyboardInterrupt as e:
        print(e)
        change(0, False)
