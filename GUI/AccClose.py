import tkinter as tk
from tkinter import Button, Label, Entry, messagebox
from PIL import Image, ImageTk, ImageOps
import keyboard
from Dataset.Dataset_init import rasp
from Commands import change_close, change

# block keys
keyboard.block_key('win')
keyboard.block_key('alt')
keyboard.block_key('ctrl')
keyboard.block_key('esc')
keyboard.block_key('tab')


def acc_cl():
    try:
        def ac_close_config(window):
            window.geometry("450x250+750+350")
            window.overrideredirect(True)

        ac_close = tk.Tk()
        ac_close_config(ac_close)

        # logo image
        def logo_img():
            i_open = Image.open('..\\img\\logo.png')
            i_exp = ImageOps.expand(i_open, border=0)
            img = ImageTk.PhotoImage(image=i_exp.resize((150, 150)))
            return img

        # placing image in label
        mge = logo_img()
        logo_label = Label(image=mge, height=130, width=110)
        logo_label.place(x=180, y=12)

        # Password
        Password = Label(ac_close, text="PIN", fg='Black', font=("Arial Black", 12))
        Password.place(x=100, y=130)

        # password insert box
        pwd_box = Entry(ac_close, fg='Black', font=("Arial", 12), show='*')
        pwd_box.place(x=160, y=135)

        # buttons
        def butt_img(image, x=95, y=45):
            i_open = Image.open(f'..\\img\\{image}')
            i_exp = ImageOps.expand(i_open)
            img = ImageTk.PhotoImage(image=i_exp.resize((x, y)))
            return img

        canc = butt_img('CANCEL REQUEST.png', 156, 51)
        close_req = butt_img('CLOSE ACC REQUEST.png', 155, 50)

        with open('Loginfo.txt', 'r') as f:
            get_usr = str(f.readline()).split("=")[1]

        def cls_req_butt(window):
            try:
                if int(pwd_box.get()) == int(rasp.get_data('PASSWORD', int(get_usr))):
                    rasp.insert_rec.execute(f"DELETE FROM Bank WHERE ACC_NUM={int(get_usr)};")
                    rasp.insert_rec.execute('COMMIT;')
                    window.destroy()
                    change_close(0, False, True)
                    return True
                else:
                    messagebox.showerror(title="Data Error", message="Password incorrect")
            except Exception as e:
                print(e)
                messagebox.showerror(title="Data Error", message="Please enter password")

        def cls_cnc(window):
            print("Request cancelled")
            window.destroy()

        canc_b = Button(image=canc, borderwidth=0, command=lambda: cls_cnc(ac_close))
        canc_b.place(x=60, y=180)

        close_req_b = Button(image=close_req, borderwidth=0, command=lambda: cls_req_butt(ac_close))
        close_req_b.place(x=240, y=180)

        ac_close.mainloop()
    except KeyboardInterrupt as e:
        print(e)
        change(0, False)


acc_cl()
