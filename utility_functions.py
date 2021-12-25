from math import pi
import skimage.io as skio
import skimage.transform as sktr


# Utility Functions

def load_image(img_path, shape=None):
    """ Loads an image given a path and an optional desired shape
    :param str img_path: The path to the image being loaded
    :param list shape: The desired shape for the image
    :return Desired Image
    """
    # imread method loads an image from specified file
    # example: path = r'C:\Users\Rajnish\Desktop\geeksforgeeks.png'
    img = skio.imread(img_path)
    if shape is not None:
        img = sktr.resize(img, shape)

    return img


def get_rad(theta, phi, gamma):
    """ Transforms spherical coordinates to radians
    :param float theta: Angle of rotation in Degrees
    :param float phi: Angle of rotation in Degrees
    :param float gamma: Angle of rotation in Degrees
    :return Spherical Coordinates in radians
    """
    return (deg_to_rad(theta),
            deg_to_rad(phi),
            deg_to_rad(gamma))


def get_deg(rtheta, rphi, rgamma):
    """ Transforms spherical coordinates to Degrees
    :param float rtheta: Angle of rotation in Radians
    :param float rphi: Angle of rotation in Radians
    :param float rgamma: Angle of rotation in Radians
    :return Spherical Coordinates in degrees
    """
    return (rad_to_deg(rtheta),
            rad_to_deg(rphi),
            rad_to_deg(rgamma))


def deg_to_rad(deg):
    """ Converts Degrees to Radians
    :param float deg: The angle to be converted
    :return The input angle in radians
    """
    return deg * pi / 180.0


def rad_to_deg(rad):
    """ Converts Radians to Degrees
    :param float rad: The angle to be converted
    :return The input angle in degrees
    """
    return rad * 180.0 / pi
