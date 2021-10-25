from math import pi
import cv2
import os

""" Utility Functions """

def load_image(img_path, shape=None):
    #imread method loads an image from specified file
    #example: path = r'C:\Users\Rajnish\Desktop\geeksforgeeks.png'
    img = cv2.imread(img_path, 1)
    if shape is not None:
        img = cv2.resize(img, shape)
    
    return img

def save_image(img_path, directory, img):
    os.chdir(directory)
    cv2.imwrite(img_path, img)

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