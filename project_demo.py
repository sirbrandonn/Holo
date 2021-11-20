from image_transformer import ImageTransformer
from rotation_utility import *
from load_files import *
import cv2
import sys
import os
import imageio


# Usage: 
#     Change main function with ideal arguments
#     then
#     python demo.py [name of the image] [degree to rotate] ([ideal width] [ideal height])
#     e.g.,
#     python demo.py images/000001.jpg 360
#     python demo.py images/000001.jpg 45 500 700
#
# Parameters:
#     img_path  : the path of image that you want rotated
#     shape     : the ideal shape of input image, None for original size.
#     theta     : the rotation around the x axis
#     phi       : the rotation around the y axis
#     gamma     : the rotation around the z axis (basically a 2D rotation)
#     dx        : translation along the x axis
#     dy        : translation along the y axis
#     dz        : translation along the z axis (distance to the image)
#
# Output:
#     image     : the rotated image


# ls ../ previous directory
# ls ./ current directory

# Relative file path
path = "./TestFiles/"
output_path = "."

# Input image path
file_types = loadFiles(path)
filtered_files = filterFiles(path, file_types)

# More likely while-loop ... pointer to a file that is being displayed. Then have
# another process that changes the pointer
# After computing all frames of the GIF - create the GIF

# Make output dir
if not os.path.isdir('output'):
    os.mkdir('output')

if not os.path.isdir('output/gifs'):
    os.mkdir('output/gifs')

for fileList in filtered_files:
    for file in fileList:
        # Rotation range
        rot_range = 360 if len(sys.argv) <= 2 else int(sys.argv[2])

        # Ideal image shape (w, h)
        img_shape = None if len(sys.argv) <= 4 else (int(sys.argv[3]), int(sys.argv[4]))

        # Instantiate the class
        it = ImageTransformer(path + file, img_shape)

        # Iterate through rotation range
        f_name, ext = os.path.splitext(file)

        if not os.path.isdir('output/' + f_name):
            os.mkdir('output/' + f_name)

        # NOTE: Here we can change which angle, axis, shift
            # Example of rotating an image along y-axis from 0 to 360 degree 
            # with a 5 pixel shift in +X direction

        with imageio.get_writer('./output/gifs/' + f_name + ".gif", mode = 'I', fps = 5, duration = 0.1) as writer:
            for ang in range(0, rot_range):
                rotated_img = it.rotate_along_axis(phi = ang)
                writer.append_data(rotated_img)

                # if not os.path.isfile('./output/' + f_name + "/" + str(ang) + ".jpg"):
                # cv2.imwrite('output/' + f_name + "/" + str(ang) + ".jpg", rotated_img)

    # Example of rotating an image along yz-axis from 0 to 360 degree
    #       rotated_img = it.rotate_along_axis(phi = ang, gamma = ang)

    # Example of rotating an image along z-axis(Normal 2D) from 0 to 360 degree
    #       rotated_img = it.rotate_along_axis(gamma = ang)