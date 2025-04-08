
# This file was generated by the Tkinter Designer by Parth Jadhav
# https://github.com/ParthJadhav/Tkinter-Designer


from pathlib import Path

# from tkinter import *
# Explicit imports to satisfy Flake8
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage
from PIL import Image, ImageTk


OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path("assets/frame0")


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)


window = Tk()

window.geometry("693x454")
window.configure(bg = "#FFFFFF")


canvas = Canvas(
    window,
    bg = "#FFFFFF",
    height = 454,
    width = 693,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge"
)

canvas.place(x = 0, y = 0)
canvas.create_rectangle(
    0.0,
    76.99999999283224,
    694.0000302188128,
    79.0,
    fill="#B02525",
    outline="")

canvas.create_text(
    11.0,
    16.0,
    anchor="nw",
    text="ви: менеджер",
    fill="#B02525",
    font=("Inter", 20 * -1)
)

button_image_1 = ImageTk.PhotoImage(Image.open(relative_to_assets("button_1.png")))
button_1 = Button(
    image=button_image_1,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_1 clicked"),
    relief="flat"
)
button_1.place(
    x=10.0,
    y=88.0,
    width=117.0,
    height=30.0
)

button_image_2 = ImageTk.PhotoImage(Image.open(relative_to_assets("button_2.png")))
button_2 = Button(
    image=button_image_2,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_2 clicked"),
    relief="flat"
)
button_2.place(
    x=294.0,
    y=23.0,
    width=117.0,
    height=30.0
)

button_image_3 = ImageTk.PhotoImage(Image.open(relative_to_assets("button_3.png")))
button_3 = Button(
    image=button_image_3,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_3 clicked"),
    relief="flat"
)
button_3.place(
    x=10.0,
    y=129.0,
    width=117.0,
    height=31.0
)

button_image_4 = ImageTk.PhotoImage(Image.open(relative_to_assets("button_4.png")))
button_4 = Button(
    image=button_image_4,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_4 clicked"),
    relief="flat"
)
button_4.place(
    x=10.0,
    y=208.0,
    width=117.0,
    height=30.0
)

button_image_5 = ImageTk.PhotoImage(Image.open(relative_to_assets("button_5.png")))
button_5 = Button(
    image=button_image_5,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_5 clicked"),
    relief="flat"
)
button_5.place(
    x=10.0,
    y=415.0,
    width=117.0,
    height=30.0
)

button_image_6 = ImageTk.PhotoImage(Image.open(relative_to_assets("button_6.png")))
button_6 = Button(
    image=button_image_6,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_6 clicked"),
    relief="flat"
)
button_6.place(
    x=10.0,
    y=169.0,
    width=117.0,
    height=31.0
)

entry_image_1 = ImageTk.PhotoImage(Image.open(relative_to_assets("entry_1.png")))
entry_bg_1 = canvas.create_image(
    637.0,
    39.5,
    image=entry_image_1
)
entry_1 = Text(
    bd=0,
    bg="#A37B7B",
    fg="#000716",
    highlightthickness=0
)
entry_1.place(
    x=592.0,
    y=27.0,
    width=90.0,
    height=23.0
)

canvas.create_rectangle(
    131.99999996130532,
    -1.0,
    135.0,
    453.999983625632,
    fill="#B02525",
    outline="")

button_image_7 = ImageTk.PhotoImage(Image.open(relative_to_assets("button_7.png")))
button_7 = Button(
    image=button_image_7,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_7 clicked"),
    relief="flat"
)
button_7.place(
    x=147.0,
    y=21.0,
    width=123.0,
    height=32.0
)
window.resizable(False, False)
window.mainloop()
