from tkinter import * 
from tkinter import filedialog , ttk
import sys ,os
from pytube import YouTube
from moviepy.editor import *
import shutil
import threading
import time 
import random as rn



script_path = sys.argv[0]

def download_progress(stream, chunk, remaining):
    total_size = stream.filesize
    bytes_downloaded = total_size - remaining
    download_percentage = (bytes_downloaded / total_size) * 100
    progress_bar['value'] = download_percentage
    root.update_idletasks()  

def download():
    global progress_bar  
    progress_window = Toplevel(root)
    progress_window.title("Download Progress")
    progress_window.geometry("300x100")

    
    progress_bar = ttk.Progressbar(progress_window, orient=HORIZONTAL, length=200, mode='determinate')
    progress_bar.pack(pady=10)

    start_time = time.time()  
    video_path = url_entry.get()
    file_path = path_label.cget("text")
    download_label=Label(text="Downloading.....")
    canvas.create_window(200,280,window=download_label)
    progress_bar.start(10) 
    mp4=YouTube(video_path,on_progress_callback=download_progress).streams.get_highest_resolution().download()  
    video_clip = VideoFileClip(mp4)
    if format.get() == "MP3" :
#code for mb3 
        audio_file =video_clip.audio
        audio_file.write_audiofile(f"audio.mp3")
        audio_file.close()
        shutil.move('audio.mp3',file_path)
#code for mb3 

    video_clip.close()
    end_time = time.time()  
    time_taken = end_time - start_time  
    progress_window.destroy()

    shutil.move(mp4,file_path)
    download_label.config(text="Download complete")
    return time_taken

def start_download():
    download_thread = threading.Thread(target=lambda: download())
    download_thread.start()




def browse_files():
    path = filedialog.askdirectory(initialdir=script_path, title="Select a Path")
    if path:
       path_label.config(text=path)
        
root = Tk() 
root.title("Video Downloader")

style = ttk.Style()
style.configure('Custom.TEntry', foreground='black', background='lightgray')
style.configure('Custom.TButton', foreground='black', background='lightgray', font=('Arial', 10, 'bold'))


canvas=Canvas(root,width=400 , height=300 )
canvas.pack()

app_label= Label(root,text="Video Downloader",fg='blue' , font=("Arila",20))
canvas.create_window(200,20,window=app_label)


url_label=Label(root,text="Enter Video URL")
url_entry = ttk.Entry(root, style='Custom.TEntry')
canvas.create_window(200,80,window=url_label)
canvas.create_window(200,100,window=url_entry)


path_label=Label(root,text="Select path to download")
path_button=ttk.Button(root,text="Select",style='Custom.TButton',command=browse_files)

canvas.create_window(200,150,window=path_label)
canvas.create_window(200,170,window=path_button) 

global format 
format = StringVar(value="MP4")

radio1 = Radiobutton(root,text="MP4",variable= format , value="MP4"  )
radio2 = Radiobutton(root ,text="MP3" ,variable= format, value="MP3" )
canvas.create_window(200,210,window=radio1) 
canvas.create_window(150,210,window=radio2) 


download_button=ttk.Button(root,text="Download",style='Custom.TButton',command=start_download)
canvas.create_window(200,250,window=download_button) 




root.mainloop()