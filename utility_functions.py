from math import pi
import skimage.io as skio

""" Utility Functions """

def load_image(img_path, shape=None):
    #imread method loads an image from specified file
    #example: path = r'C:\Users\Rajnish\Desktop\geeksforgeeks.png'
    img = skio.imread(img_path)
    if shape is not None:
        img = skio.resize(img, shape)
        
    return img

def get_rad(theta, phi, gamma):
    return (deg_to_rad(theta),
            deg_to_rad(phi),
            deg_to_rad(gamma))

def get_deg(rtheta, rphi, rgamma):
    return (rad_to_deg(rtheta),
            rad_to_deg(rphi),
            rad_to_deg(rgamma))

def deg_to_rad(deg):
    return deg * pi / 180.0

def rad_to_deg(rad):
    return rad * 180.0 / pi