from rotation_utility import *
from load_files import *
from PIL import Image
import tkinter as tk
import time

if not os.path.isdir('output/screens'):
    os.mkdir('output/screens')

gif_save_path = "./output/screens/"

gif_path = "./output/gifs/"

gif_type = loadFiles(gif_path)
filtered_gifs = filterFiles(gif_path, gif_type)

class Screen:
    def __init__(self):
        self.root = tk.Tk()
        self.root.geometry("1080x720")

        self.root.wm_overrideredirect(True)

        self.main_frame = tk.Frame(self.root)
        self.main_frame.pack(fill = "both", expand = True)

        
        self.gif_frames = []
        self.images = []
        self.root.mainloop()

    def animation(self):
        gif_files = next(os.walk(gif_path))
        for counter in len(gif_files):
            gif_name = "test" + str(counter) + ".gif"
            gif = Image.open(gif_path + gif_name)
            self.number_of_frames = gif.n_frames

            for counter in range(self.number_of_frames):
                gif.seek(counter)
                gif.save(os.path.join('gif_save_path',))
                self.gif_frames.append()

Screen()