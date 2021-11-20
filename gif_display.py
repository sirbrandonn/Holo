from rotation_utility import *
from load_files import *
from PIL import Image
from skimage.filters import gaussian
from skimage import img_as_ubyte

gif_path = "./output/gifs/"

if not os.path.isdir('output/smoothed_gifs'):
    os.mkdir('output/smoothed_gifs')

smoothed_gif_path = "./output/smoothed_gifs/"

file_types = loadFiles(gif_path)
filtered_files = filterFiles(gif_path, file_types)

gif_number = 1

for root, dirs, files in os.walk("output/gifs"):
    for name in files:
        print(name)
        path = os.path.join(root, name)
        print(path)
        img = Image.open(str(path)).convert('RGB')
        img.show()
        cap = cv2.VideoCapture(path)
        ret, gif = cap.read()
        print(gif)
        
        rgb = cv2.cvtColor(gif, cv2.COLOR_BGR2RGB)

        print(type(rgb))

        cv2.imshow("gif", rgb)
        if ret:
            smoothed_gif_array = img_as_ubyte(gaussian(gif, sigma = 5, mode = 'constant', cval = 0.0, multichannel = 'False'))
            smoothed_gif = Image.fromarray(smoothed_gif_array)
            cv2.imwrite('output/smoothed_gifs/' + "gif" + str(gif_number) + ".gif", smoothed_gif)

        gif_number += 1

        cap.release()
