#!/usr/bin/env python
# coding: utf-8

# In[4]:


pip install -U pygame --user


# In[1]:


import tkinter as tk
import os
from pygame import mixer


# In[2]:


class MusicPlayer:
    def __init__(self, root):
        self.root = root
        self.root.title("Music Player")
        self.root.geometry("300x100")

        # Initialize Pygame mixer
        mixer.init()

        # Create a variable to store the current playing status
        self.playing = False

        # Create a variable to store the current selected song
        self.current_song = None

        # Create the UI elements
        self.label = tk.Label(root, text="Music Player")
        self.label.pack()

        self.play_button = tk.Button(root, text="Play", command=self.play_music)
        self.play_button.pack()

        self.stop_button = tk.Button(root, text="Stop", command=self.stop_music)
        self.stop_button.pack()

        self.browse_button = tk.Button(root, text="Browse", command=self.browse_music)
        self.browse_button.pack()

    def play_music(self):
        if self.current_song:
            if not self.playing:
                mixer.music.load(self.current_song)
                mixer.music.play()
                self.play_button.config(text="Pause")
                self.playing = True
            else:
                mixer.music.pause()
                self.play_button.config(text="Play")
                self.playing = False

    def stop_music(self):
        mixer.music.stop()
        self.play_button.config(text="Play")
        self.playing = False

    def browse_music(self):
        self.current_song = tk.filedialog.askopenfilename(initialdir=os.getcwd(), title="Select Song",
                                                         filetypes=(("Audio Files", "*.mp3"), ("All Files", "*.*")))
        self.label.config(text=os.path.basename(self.current_song))


# In[3]:


if __name__ == '__main__':
    root = tk.Tk()
    music_player = MusicPlayer(root)
    root.mainloop()


# In[ ]:




