import os
import os.path
import fnmatch
from PIL import Image as PImage
from glob import glob
from os import listdir

def loadFiles(path):
    # return list of file extensions in the working directory
    fileList = listdir(path)
    fileTypes = []

    for file in fileList:
        name, extension = os.path.splitext(file)
        if (extension != '') and (("*" + extension) not in fileTypes):
            fileTypes.append("*" + extension)
            print(fileTypes)

    return fileTypes

def filterFiles(path, fileTypes):
    # return list of filtered lists with respect to filetype
    filteredFiles = []

    for fileType in fileTypes:
        files = fnmatch.filter(os.listdir(path), fileType)
        filteredFiles.append(files)
        print(filteredFiles)

    return filteredFiles