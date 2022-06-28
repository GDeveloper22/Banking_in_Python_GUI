import tkinter as tk
from tkinter import Button, Label, Text
from PIL import Image, ImageTk, ImageOps
import keyboard
from Dataset.Dataset_init import rasp

# block keys
keyboard.block_key('win')
keyboard.block_key('alt')
keyboard.block_key('ctrl')
keyboard.block_key('esc')
keyboard.block_key('tab')


def acc_lst():
    def acc_lst_config(window):
        window.geometry("900x600+620+250")
        window.overrideredirect(True)

    ac_list = tk.Tk()
    acc_lst_config(ac_list)

    # label
    hold_lab = Label(ac_list, text="ACCOUNT HOLDER LIST", fg='Black', font=("Arial Black", 18))
    hold_lab.place(x=20, y=10)

    # image buttons
    def butt_img(image, x=95, y=45):
        i_open = Image.open(f'..\\img\\{image}')
        i_exp = ImageOps.expand(i_open)
        img = ImageTk.PhotoImage(image=i_exp.resize((x, y)))
        return img

    def l_c(window):
        window.destroy()

    close_list = butt_img('CLOSE.png', 120, 42)
    # close button
    close_b = Button(image=close_list, borderwidth=0, command=lambda: l_c(ac_list))
    close_b.place(x=760, y=7)
    # list
    hold_list = Text(ac_list, fg='Black', font=("Arial", 12), state='normal', borderwidth=2, width=95, height=29)
    hold_list.place(x=20, y=60)
    #  number, name, current balance, account status, email, phone number.
    data = rasp.get_acc_list('ACC_NUM', 'ACC_STATUS', 'FIRST_NAME', 'LAST_NAME', 'EMAIL', 'PHONE_NUM', 'BALANCE')
    data_fetched = ['ACC_NUM', 'ACC_STATUS', 'FIRST_NAME', 'LAST_NAME', 'EMAIL', 'PHONE_NUM', 'BALANCE']
    for i in range(len(data)):
        for j in range(len(data[i])):
            data_fetched.append(data[i][j])
    data_fetched_n = '         '.join(str(e) for e in data_fetched)
    print(data_fetched_n)
    hold_list.insert(tk.INSERT, str(data_fetched_n))
    hold_list.config(state='disabled')
    # wrapping window
    ac_list.mainloop()
# hold_list.insert(tk.INSERT, 'text')  # used to insert the data in the text box, before that change state to normal, and add text and change state back to disable.


acc_lst()
