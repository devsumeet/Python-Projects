from tkinter import *
from pytube import YouTube

root = Tk()
root.geometry('500x300')
root.resizable(0,0)
root.title("YouTube Video Downloader")

Label(root,text = 'Youtube Video Downloader', fg='red', font ='arial 20 bold').pack()

link = StringVar()

Label(root, text = 'Paste Link Here:', fg='blue', font = 'arial 15 bold').place(x= 160 , y = 60)
link_enter = Entry(root, width = 70,textvariable = link).place(x = 32, y = 90)


def Downloader():
     
    url =YouTube(str(link.get()))
    video = url.streams.first()
    video.download()
    Label(root, text = 'DOWNLOADED', fg='blue', font = 'arial 15').place(x= 180 , y = 210)  

Button(root,text = 'DOWNLOAD', font = 'arial 15 bold' ,bg = 'blue', padx = 2, command = Downloader).place(x=180 ,y = 150)

root.mainloop()