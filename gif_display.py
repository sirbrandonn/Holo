from load_files import loadFiles
from PIL import Image
from skimage import img_as_ubyte
from skimage.filters import gaussian
import os
import cv2
import skimage.io as skio
import numpy as np

gif_path = "./output/gifs/"

if not os.path.isdir('./output/smoothed_gifs'):
    os.mkdir('./output/smoothed_gifs')

smoothed_gif_path = "./output/smoothed_gifs/"

file_types = loadFiles(gif_path)

def display_gif():

    gif_number = 1

    for root, dirs, files in os.walk("output/gifs"):
        for name in files:
            path = os.path.join(root, name)

            # Load img using cv2
            cap = cv2.VideoCapture(path)
            ret, gif = cap.read()

            if ret:
                smoothed_gif_array = gaussian(gif, sigma = 5, mode = 'constant', cval = 0.0, multichannel = 'False')
                print(smoothed_gif_array.min(), smoothed_gif_array.max())
                smoothed_gif = Image.fromarray(smoothed_gif_array).convert("RGB")
                smoothed_gif = np.array(smoothed_gif)
                print(type(smoothed_gif))
                skio.imsave('output/smoothed_gifs/' + "gif" + str(gif_number) + ".gif", smoothed_gif)

            gif_number += 1

            cap.release()

if __name__ == "__main__":
    display_gif()