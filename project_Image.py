from PIL import Image as PImage
from glob import glob
from os import listdir


path = "/Users/brandon/Desktop/Holobox/Project_Holo/TestFiles/"

def loadFiles(path):
    # return array of files

    fileList = listdir(path)
    loadedFiles = []
    for file in fileList:
        currentFile = PImage.open(path + file)
        loadedFiles.append(currentFile)

    return loadedFiles

fileArray = loadFiles(path)

for currentFile in fileArray:
    currentFile.show()



#types = ["*.gif", "*.png", "*.jpg", "*.mp4", "*.mp3", "*.mov"]

# fileTypeArray = []

#for type in types:
#    thisFileType = glob.glob(type)
#    fileTypeArray += thisFileType
# "/Users/brandon/Downloads/test.jpg"
#    tempImage = Image.open(type)
#    tempImage.show()

# print(fileTypeArray)





