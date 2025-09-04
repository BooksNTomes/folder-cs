from os import rename
from os.path import exists, splitext, exists, join
from shutil import move
from sources import *

# Utils
def make_unique(dest, name):
    # SRC: 
    filename, extension = splitext(name)
    counter = 1
    while exists(f"{dest}/{name}"):
        name = f"{filename}({str(counter)}){extension}"
        counter += 1

    return name

def move_file(dest, entry, name):
    # SRC: 
    if exists(f"{dest}/{name}"):
        unique_name = make_unique(dest, name)
        oldName = join(dest, name)
        newName = join(dest, unique_name)
        rename(oldName, newName)
    move(entry, dest)

def check_files(extensions, dest_dir, entry, name):
    # REFERENCE: 
    for extension in extensions:
        if name.endswith(extension) or name.endswith(extension.upper()):
            move_file(dest_dir, entry, name)
            print(f"Moved file {name} to {dest_dir}")