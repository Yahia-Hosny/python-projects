from tkinter import * 
from tkinter import filedialog
from compress_module import * 
import sys ,os
import re 
script_path = sys.argv[0]

inputname =0
def browse_files():
    filename = filedialog.askopenfilename(initialdir=script_path, title="Select a File", filetypes=(("Text files", "*.txt*"), ("All files", "*.*")))
    if filename:
       filename = os.path.basename(filename)
       file_label.config(text="Selected file: " + filename)
       global inputname 
       inputname = filename 
        

def compression (i,o):
    compress(i,o,9)
    comp_label.config(text="The compress done successfully ")

root = Tk()
root.title("Compression Engine ")



frame=Frame(root)
frame.grid(row=0,column=0)


label_font = ("Helvetica", 10, "bold")
inputfile_label = Label(frame , text="Select File to be compressed : ",font=label_font, bg="#f0f0f0", padx=10, pady=5)
inputfile_label.grid(row=0,column=0)

browse_button = Button(root, text="Browse", command=browse_files ,font=label_font)
browse_button.grid(row=0 , column=1)



enter_button = Button(root, text="Compress", command=lambda :compression(inputname,f"compressed_{inputname}")  ,font=label_font , bg="#f0f0f0", padx=10, pady=5)
enter_button.grid(row=3 , column=1)

file_label = Label(root, text="", font=label_font)
file_label.grid(row = 1 ,column=1)

comp_label= Label(root, text="", font=label_font)
comp_label.grid(row = 4 ,column=1)


root.geometry("500x200")



root.mainloop()
