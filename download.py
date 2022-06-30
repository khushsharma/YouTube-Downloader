from os import path
from tkinter import *
from tkinter import filedialog
from turtle import color
from moviepy import *
from moviepy.editor import VideoFileClip
from pytube import YouTube
from custombutton import RoundedButton
from turtle import color

def changeOnHover(button, colorOnHover, colorOnLeave):
  
    # adjusting backgroung of the widget
    # background on entering widget
    button.bind("<Enter>", func=lambda e: button.config(
        background=colorOnHover))
  
    # background color on leving widget
    button.bind("<Leave>", func=lambda e: button.config(
        background=colorOnLeave))

def select_path():
    # allow user to select path from the explorer
    path = filedialog.askdirectory()
    path_label.configure(text=path)


def download_file():
    #get user path
    get_link = link_field.get()
    #get selected path
    user_path = path_label.cget("text")
    #download Video
    mp4_video = YouTube(get_link).streams.get_highest_resolution().download()
    vid_clip = VideoFileClip(mp4_video)
    vid_clip.close()

screen = Tk()
title = screen.title('YouTube Downloader')
canvas = Canvas(screen,width = 600,height= 600 )
canvas.pack()


#image logo
logo_img = PhotoImage(file='yt.png')
#resize
logo_img = logo_img.subsample(3,3)
canvas.create_image(300,150,image = logo_img)

#link fields
link_field = Entry(screen,width=60)
link_label = Label(screen,text="Enter the Download link" ,font=('Arial ' ,15))


#select path for saving file
path_label = Label(screen,text="Select Path For Download",font=('Arial ' ,15))
#select_btn = Button(screen , text = "Select" ,font=('Arial ' ,20),command=select_path)
select_btn = RoundedButton(screen, text="Select", border_radius=5, padding=20, command=select_path, color="#bfe3e1" ,fsize=20)
#effects
changeOnHover(select_btn,'#8aa2a1','#bfe3e1')
#Add to window
canvas.create_window(300,350 ,window= path_label)
canvas.create_window(300,400 ,window=select_btn)


#Add widgests to window
canvas.create_window(300,270 ,window = link_label)
canvas.create_window(300,300 ,window = link_field)

# download buttons
#download_btn = Button(screen , text="Download the File" ,font=('Arial ' ,20) , command= download_file)
download_btn = RoundedButton(screen, text="Download the File", border_radius=5, padding=20, command=download_file, color="#bfe3e1" ,fsize=20)
#effects for button
changeOnHover(download_btn,'#8aa2a1','#bfe3e1')

#Add to canvas
canvas.create_window(300,450,window = download_btn)

screen.mainloop()

