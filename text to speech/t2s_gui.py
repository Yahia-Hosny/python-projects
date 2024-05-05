from tkinter import  * 
from tkinter import filedialog
from gtts import gTTS
import os ,sys 


script_path = sys.argv[0]
inputname =0

def t2s(text , lang):
    output = gTTS(text=text ,lang=lang,slow=False)
    output.save('fileoutput.mp3')
    os.system("start fileoutput.mp3")



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


in_label=Label(frame,text="Enter text :  ",font=font_1)
in_label.grid(row=2 ,column=0)

in_entry =Entry(frame)
in_entry.grid(row=2 ,column=1)


file_label = Label(frame, text="", font=font_1)
file_label.grid(row = 3 ,column=1)

button =Button(frame,text="Convert",font=font_1,command=lambda:t2s(in_entry.get() , lang.get() ) )
button.grid(row = 3 ,column=1 )


root.geometry("250x200")

root.mainloop()
