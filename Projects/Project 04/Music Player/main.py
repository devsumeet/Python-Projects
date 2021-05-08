from tkinter import *
from tkinter import filedialog
from pygame import mixer

class MusicPlayer:
    def __init__(self, window ):
        window.geometry('320x100')
        window.title('Music Player')
        window.resizable(0,0)
        load = Button(window, bg='#000000', fg='white',text = 'Load',  width = 10, font = ('Times', 10), command = self.load)
        play = Button(window, bg='#004000', fg='white',text = 'Play',  width = 10,font = ('Times', 10), command = self.play)
        pause = Button(window,bg='#880000', fg='white',text = 'Pause',  width = 10, font = ('Times', 10), command = self.pause)
        stop = Button(window, bg='#090000', fg='white', text = 'Stop',  width = 10, font = ('Times', 10), command = self.stop)
        load.place(x=20,y=20)
        play.place(x=120,y=20)
        pause.place(x=220,y=20)
        stop.place(x=120,y=60)
        self.music_file = False
        self.playing_state = False
    def load(self):
        self.music_file = filedialog.askopenfilename()
    def play(self):
        if self.music_file:
            mixer.init()
            mixer.music.load(self.music_file)
            mixer.music.play()
    def pause(self):
        if not self.playing_state:
            mixer.music.pause()
            self.playing_state=True
        else:
            mixer.music.unpause()
            self.playing_state = False
    def stop(self):
        mixer.music.stop()
root = Tk()
app= MusicPlayer(root)
root.mainloop()