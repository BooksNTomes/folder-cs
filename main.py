from os import scandir, mkdir
from os.path import exists
from src.sources import *
from src.utils import *

# Main Execution
if __name__ == "__main__":
    for dir in dest:
        if (not exists(dir)):
            mkdir(dir)
            print(f"Created dir: {dir}")

    with scandir(FOLDER_PATH) as entries:

        for entry in entries:
            name = entry.name
            for i in range(DIR_COUNT):
                check_files(ext[i], dest[i], entry, name)
            
    input("Enter to Exit")