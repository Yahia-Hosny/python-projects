from tkinter import  * 
from tkinter import filedialog
from gtts import gTTS
import os ,sys 


script_path = sys.argv[0]
inputname =0


def t2s(file , lang):
    text = open(file,'r').read()
    output = gTTS(text=text ,lang=lang,slow=False)
    output.save('fileoutput.mp3')
    os.system("start fileoutput.mp3")


def browse_files():
    filename = filedialog.askopenfilename(initialdir=script_path, title="Select a File", filetypes=(("Text files", "*.txt*"), ("All files", "*.*")))
    if filename:
       filename_short = os.path.basename(filename)
       file_label.config(text="Selected file: " + filename_short)
       global inputname 
       inputname = filename 

root = Tk()


frame =Frame(root)
frame.grid(row=0 , column = 0 )





root.title("Text to Speech" )
font_1 = ("Helvetica", 10, "bold")


lang = StringVar(value="en")
radio1 = Radiobutton(frame,text="English",variable= lang , value="en"  )
radio2 = Radiobutton(frame ,text="Arabic" ,variable= lang, value="ar"  )

radio1.grid(row=0,column=0)
radio2.grid(row=1,column=0)

in_label=Label(frame,text="Select file:",font=font_1)
in_label.grid(row=2 ,column=0)


file_label = Label(frame, text="", font=font_1)
file_label.grid(row = 3 ,column=1)

button =Button(frame,text="Convert",font=font_1, command=lambda:t2s(inputname ,lang.get() ))
button.grid(row = 4 ,column=2 )








browse_button = Button(frame, text="Browse", command=browse_files ,font=font_1)
browse_button.grid(row=2 , column=1 )

root.geometry("300x200")

root.mainloop()

