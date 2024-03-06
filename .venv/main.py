from tkinter import *
from tkinter.colorchooser import askcolor
from tkinter import ttk
import tkinter as tk
from PIL import Image, ImageTk

app = Tk()
app.title("Paint Demo")
app.geometry("1050x570+150+50")
app.configure(bg="#f2f3f5")
app.resizable(False, False)

current_x = 0
current_y = 0
color = 'black'

def locate_xy(work):
    global current_x, current_y

    current_x = work.x
    current_y = work.y

def addLine(work):
    global current_x, current_y

    canvas.create_line((current_x, current_y, work.x, work.y), width=get_current_value(), fill=color,
                       capstyle=ROUND, smooth=TRUE)
    current_x, current_y = work.x, work.y

def show_color(new_color):
    global color

    color = new_color

def new_canvas():
    canvas.delete("all")
    display_palette()

image_icon = PhotoImage(file="paint_img.png")
app.iconphoto(False, image_icon)

eraser_image = Image.open("ereaser.png")
eraser_image = eraser_image.resize((32, 32))
eraser_photo = ImageTk.PhotoImage(eraser_image)

colors = Canvas(app, bg="#ffffff", width=55, height=430, bd=0)
colors.place(x=30, y=60)

Button(app, image=eraser_photo, bg="#f2f3f5", command=new_canvas).place(x=40, y=440)

############ PALETTE OF COLORS ###############

def display_palette():
    id = colors.create_rectangle((16, 16, 41, 41), fill="black")
    colors.tag_bind(id, '<Button-1>', lambda x: show_color("black"))

    id = colors.create_rectangle((16, 56, 41, 81), fill="gray")
    colors.tag_bind(id, '<Button-1>', lambda x: show_color("gray"))

    id = colors.create_rectangle((16, 96, 41, 121), fill="brown4")
    colors.tag_bind(id, '<Button-1>', lambda x: show_color("brown4"))

    id = colors.create_rectangle((16, 136, 41, 161), fill="red")
    colors.tag_bind(id, '<Button-1>', lambda x: show_color("red"))

    id = colors.create_rectangle((16, 176, 41, 201), fill="orange")
    colors.tag_bind(id, '<Button-1>', lambda x: show_color("orange"))

    id = colors.create_rectangle((16, 216, 41, 241), fill="yellow")
    colors.tag_bind(id, '<Button-1>', lambda x: show_color("yellow"))

    id = colors.create_rectangle((16, 256, 41, 281), fill="green")
    colors.tag_bind(id, '<Button-1>', lambda x: show_color("green"))

    id = colors.create_rectangle((16, 296, 41, 321), fill="blue")
    colors.tag_bind(id, '<Button-1>', lambda x: show_color("blue"))

    id = colors.create_rectangle((16, 336, 41, 361), fill="purple")
    colors.tag_bind(id, '<Button-1>', lambda x: show_color("purple"))

display_palette()

canvas = Canvas(app, width=880, height=480, background="white", cursor="hand2")
canvas.place(x=120, y=30)

canvas.bind('<Button-1>', locate_xy)
canvas.bind('<B1-Motion>', addLine)

current_value = tk.DoubleVar()

################# SLIDER ########################

def get_current_value():
    return '{: .2f}'.format(current_value.get())

def slider_changed(event):
    value_label.configure(text=get_current_value())

slider = ttk.Scale(app, from_=0,to=30, orient='horizontal', command=slider_changed, variable=current_value)
slider.place(x=30, y=530)

value_label = ttk.Label(app, text=get_current_value())
value_label.place(x=27, y=550)


app.mainloop()