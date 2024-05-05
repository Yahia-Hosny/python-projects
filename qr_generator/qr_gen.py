from tkinter import * 
import pyqrcode as qr 
from PIL import ImageTk , Image 
from tkinter import ttk


def generate():
    link_name = name_entry.get()
    link = link_entry.get()
    file_name=link_name+".png"
    url = qr.create(link)
    url.png(file_name,scale=8)
    image_1 = ImageTk.PhotoImage(Image.open(file_name))
    image_label = Label(image=image_1)
    image_label.image= image_1 
    canvas.create_window(200 , 450 , window=image_label)


root = Tk () 

style = ttk.Style()
style.configure('Custom.TEntry', foreground='black', background='lightgray')

canvas = Canvas(root ,width=400 ,height=600)
canvas.pack()

app_label= Label(root , text="QR code generator" , fg='blue' , font= ("Arial",30))
canvas.create_window(200,50,window=app_label)

name_label =Label(root , text="Link name: " )
link_label =Label(root , text="Link: " )

canvas.create_window(200,100,window=name_label)
canvas.create_window(200,160,window=link_label)

name_entry = ttk.Entry(root, style='Custom.TEntry')
link_entry = ttk.Entry(root, style='Custom.TEntry')
canvas.create_window(200,130,window=name_entry)
canvas.create_window(200,180,window=link_entry)

button = Button(root , text="Generate QR" , command= generate)
canvas.create_window(200,230, window=button)

root.mainloop()