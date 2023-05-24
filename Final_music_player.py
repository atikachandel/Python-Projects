import tkinter as tk
import os
import pygame
from tkinter import filedialog

class MusicPlayer:
    def __init__(self, root):
        self.root = root
        self.root.title("Music Player")

        # Initialize Pygame mixer
        pygame.mixer.init()

        # Create playlist
        self.playlist = []

        # Create current song index
        self.current_song_index = 0

        # Create GUI elements
        self.create_ui()

    def create_ui(self):
        # Create playlist label
        playlist_label = tk.Label(self.root, text="Playlist")
        playlist_label.pack()

        # Create playlist listbox
        self.playlist_listbox = tk.Listbox(self.root, width=100)
        self.playlist_listbox.pack()

        # Create buttons frame
        buttons_frame = tk.Frame(self.root)
        buttons_frame.pack()

        # Create Add Song button
        add_song_button = tk.Button(buttons_frame, text="Add Song", command=self.add_song)
        add_song_button.pack(side=tk.LEFT)

        # Create Remove Song button
        remove_song_button = tk.Button(buttons_frame, text="Remove Song", command=self.remove_song)
        remove_song_button.pack(side=tk.LEFT)

        # Create Play button
        play_button = tk.Button(buttons_frame, text="Play", command=self.play)
        play_button.pack(side=tk.LEFT)

        # Create Pause button
        pause_button = tk.Button(buttons_frame, text="Pause", command=self.pause)
        pause_button.pack(side=tk.LEFT)

        # Create Stop button
        stop_button = tk.Button(buttons_frame, text="Stop", command=self.stop)
        stop_button.pack(side=tk.LEFT)

    def add_song(self):
        song_path = filedialog.askopenfilename(filetypes=[("MP3 Files", "*.mp3")])

        if song_path:
            song_name = os.path.basename(song_path)
            self.playlist.append(song_path)
            self.playlist_listbox.insert(tk.END, song_name)

    def remove_song(self):
        selected_song_index = self.playlist_listbox.curselection()[0]
        self.playlist_listbox.delete(selected_song_index)
        self.playlist.pop(selected_song_index)

    def play(self):
        if self.playlist:
            song_path = self.playlist[self.current_song_index]
            pygame.mixer.music.load(song_path)
            pygame.mixer.music.play()

    def pause(self):
        if pygame.mixer.music.get_busy():
            pygame.mixer.music.pause()

    def stop(self):
        pygame.mixer.music.stop()

# Create the Tkinter root window
root = tk.Tk()

# Create the MusicPlayer instance
music_player = MusicPlayer(root)

# Run the Tkinter event loop
root.mainloop()
