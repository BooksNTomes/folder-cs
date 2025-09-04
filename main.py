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
            check_files(audio_extensions, dest_dir_music, entry, name)
            check_files(video_extensions, dest_dir_video, entry, name)
            check_files(image_extensions, dest_dir_image, entry, name)
            check_files(document_extensions, dest_dir_documents, entry, name)
            check_files(executable_extensions, dest_dir_executables, entry, name)
            check_files(zip_extensions, dest_dir_zips, entry, name)
            check_files(code_extensions, dest_dir_code, entry, name)

    input("Enter to Exit")