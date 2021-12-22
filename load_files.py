import os
import fnmatch
from os import listdir

def loadFiles(path):
    # Return a list of lists of files in the working directory
    fileList = listdir(path)
    fileTypes = []
    filteredFiles = []

    # Create a list of extensions in working directory
    for file in fileList:
        name, extension = os.path.splitext(file)
        if (extension != '') and (("*" + extension) not in fileTypes):
            fileTypes.append("*" + extension)

    # Create a list of files according to extensions
    for fileType in fileTypes:
        files = fnmatch.filter(os.listdir(path), fileType)
        filteredFiles.append(files)

    return filteredFiles