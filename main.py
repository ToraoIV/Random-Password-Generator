import random
import string
import customtkinter as ctk
import pyperclip
from PIL import Image

copy_img = ctk.CTkImage(Image.open("copy.png"), size=(30, 30))
uppercase_letters = string.ascii_uppercase
lowercase_letters = string.ascii_lowercase
numbers = string.digits
punctuations = r"""?@!#%+-*%"""

root = ctk.CTk()
root.title("Random Password Generator")
root.geometry("400x380")
root.resizable(False, False)

frame1 = ctk.CTkFrame(root, fg_color="transparent")
frame1.pack(side=ctk.TOP, pady=(40,50))
frame2 = ctk.CTkFrame(root, fg_color="transparent")
frame2.pack(side=ctk.TOP)
frame3 = ctk.CTkFrame(root, fg_color="transparent")
frame3.pack(side=ctk.TOP, pady=30)
frame4 = ctk.CTkFrame(root, fg_color="transparent")
frame4.pack(side=ctk.TOP, pady=(0,20))


password_var = ctk.StringVar()
password_var.set("password")

entry = ctk.CTkEntry(frame1, textvariable=password_var, font=("Calibri", 25), justify="center", state="readonly", width=250)
entry.pack(side=ctk.LEFT, padx=10)
copy = ctk.CTkButton(frame1, text="", image=copy_img, width=40, height=40, fg_color="transparent", command= lambda :copy_func())
copy.pack(side=ctk.LEFT, padx=10)

label = ctk.CTkLabel(root, text="Password Length")
label.place(x=45, y=100)

value = ctk.IntVar()

slider = ctk.CTkSlider(frame2, from_=5, to=20, width=330, number_of_steps=15, variable=value)
slider.pack(side=ctk.TOP)

label_leng = ctk.CTkLabel(root, textvariable=value)
label_leng.place(x=340, y=100)

frame_left = ctk.CTkFrame(frame3, fg_color="transparent")
frame_left.pack(side=ctk.LEFT, padx=10)
frame_right = ctk.CTkFrame(frame3, fg_color="transparent")
frame_right.pack(side=ctk.LEFT, padx=10)

uppercase_var = ctk.StringVar(value="on")
checkbox = ctk.CTkCheckBox(frame_left, text="Uppercase (A-Z)", variable=uppercase_var, onvalue="on", offvalue="off")
checkbox.pack(side=ctk.TOP, pady=10, anchor= ctk.W)

lowercase_var = ctk.StringVar(value="on")
checkbox = ctk.CTkCheckBox(frame_right, text="Lowercase (a-z)", variable=lowercase_var, onvalue="on", offvalue="off")
checkbox.pack(side=ctk.TOP, pady=10, anchor= ctk.W)

numbers_var = ctk.StringVar(value="on")
checkbox = ctk.CTkCheckBox(frame_left, text="Numbers (0-9)", variable=numbers_var, onvalue="on", offvalue="off")
checkbox.pack(side=ctk.TOP, pady=10, anchor= ctk.W)

symbol_var = ctk.StringVar(value="on")
checkbox = ctk.CTkCheckBox(frame_right, text="Symbols (?-@!)", variable=symbol_var, onvalue="on", offvalue="off")
checkbox.pack(side=ctk.TOP, pady=10, anchor= ctk.W)


def generate(leng):

    uzunluk = leng

    upper = uppercase_var.get()
    lower = lowercase_var.get()
    numb = numbers_var.get()
    symb = symbol_var.get()

    letters = ""
    password = ""

    if upper == "on":
        letters += uppercase_letters
    if lower == "on":
        letters += lowercase_letters
    if numb == "on":
        letters += numbers
    if symb == "on":
        letters += punctuations

    for x in range(uzunluk):
        random_letter = random.choice(letters)
        password += random_letter

    password_var.set(password)
    print(len(password))

def copy_func():
    pw = entry.get()
    pyperclip.copy(pw)


button = ctk.CTkButton(frame4, text="GENERATE PASSWORD", width=280, height=45, font=("Calibri", 20, "bold"), command= lambda :generate(value.get()))
button.pack(side=ctk.TOP)

root.mainloop()
