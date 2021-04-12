# Code to organize files in a directory into subdirectories
import os
from pathlib import Path

SUBDIRECTORIES = {
    "OrganizeMe-DOCUMENTS": ['.pdf', '.rtf', '.txt'],
    "OrganizeMe-AUDIO": ['.m4a', '.m4b', '.mp3'],
    "OrganizeMe-VIDEOS": ['.mov', '.avi', '.mp4'],
    "OrganizeMe-IMAGES": ['.jpg', '.jpeg', '.png']
}


# Check which subdirectory the file extension should go to
def pickDirectory(value):
    for category, suffixes in SUBDIRECTORIES.items():
        for suffix in suffixes:
            if suffix == value:
                return category
    # Return 'MISC' if the filetype does not exist in the dictionary
    return 'MISC'


def organizeDirectory():
    for item in os.scandir():
        # Check if the item is a directory
        if item.is_dir():
            continue
        filePath = Path(item)
        filetype = filePath.suffix.lower()
        # Skip the python script
        if filetype == '.py':
            continue
        directory = pickDirectory(filetype)
        directoryPath = Path(directory)
        if not directoryPath.is_dir():
            directoryPath.mkdir()
        filePath.rename(directoryPath.joinpath(filePath))


if __name__ == '__main__':
    organizeDirectory()
