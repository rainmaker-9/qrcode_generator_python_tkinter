import tkinter as tk
from tkinter import ttk
from tkinter import colorchooser, messagebox
from tkinter.filedialog import asksaveasfile
import qrcode

app_title = "QR Code Generator in Python"
win = tk.Tk()
win.title(app_title)
width=480
height=120
screenwidth = win.winfo_screenwidth()
screenheight = win.winfo_screenheight()
alignstr = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
win.geometry(alignstr)
win.resizable(width=False, height=False)
qr_default_fg_color = "black"
qr_default_bg_color = "white"

def save():
    files = [('PNG Image', '*.png')]
    return asksaveasfile(filetypes = files, defaultextension = files).name

def choose_fg_color():
  global qr_default_fg_color
  color_code = colorchooser.askcolor(title ="Choose QR Foreground Color")
  qr_default_fg_color = color_code.__getitem__(1)

def choose_bg_color():
  global qr_default_bg_color
  color_code = colorchooser.askcolor(title ="Choose QR Background Color")
  qr_default_bg_color = color_code.__getitem__(1)

def generate_qr():
  input_URL = LineEditURL.get()
  if(input_URL != ''):
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=15,
        border=4,
    )
    qr.add_data(input_URL)
    qr.make(fit=True)
    img = qr.make_image(fill_color=qr_default_fg_color, back_color=qr_default_bg_color)
    img.save(save())
    messagebox.showinfo(app_title, "QR Code generated successfully")
  else:
    messagebox.showerror(app_title, "Please enter URL / Link / Web Address to generate QR Code")

LineEditURL= ttk.Entry(win)
LineEditURL.place(x=30,y=30,width=345,height=25)

BtnGenerate=ttk.Button(win, text = "Generate", command = generate_qr)
BtnGenerate.place(x=380,y=29,width=70,height=27)

BtnBackgroundColor=ttk.Button(win, text = "Choose QR Background Color", command = choose_bg_color)
BtnBackgroundColor.place(x=29,y=60,width=210,height=30)

BtnForegroundColor=ttk.Button(win, text = "Choose QR Foreground Color", command = choose_fg_color)
BtnForegroundColor.place(x=240,y=60,width=210,height=30)

win.mainloop()