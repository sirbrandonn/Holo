import os
from collections import defaultdict


def load_files(path):
    """
    Return a list of lists of files in the working directory
    :param str path: Path to the target directory
    :return list(list) Files in the Directory Partitioned by filetype
    """
    file_list = os.listdir(path)

    file_map = defaultdict(list)

    # Create a list of filetypes in the provided path and partition them by filetype
    for file in file_list:
        name, extension = os.path.splitext(file)
        file_map["*" + extension].append(file)

    return list(file_map.values())
