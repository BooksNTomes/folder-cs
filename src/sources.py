from dotenv import load_dotenv
from os import getenv
from os.path import join

load_dotenv()

FOLDER_PATH = getenv('FOLDER_PATH') 
# Update all of these when needed
# Order: image - video - audio - documents - executables - zips - code

# Destinations
image_dest = join(FOLDER_PATH, "images") # type: ignore
video_dest = join(FOLDER_PATH, "videos") # type: ignore
audio_dest = join(FOLDER_PATH, "audio") # type: ignore
documents_dest = join(FOLDER_PATH, "documents") # type: ignore
executables_dest = join(FOLDER_PATH, "executables") # type: ignore
installers_dest = join(FOLDER_PATH, "installers") # type: ignore
zips_dest = join(FOLDER_PATH, "zips") # type: ignore
code_dest = join(FOLDER_PATH, "code") # type: ignore
# Master Destination List
dest = [image_dest, 
        video_dest, 
        audio_dest, 
        documents_dest, 
        executables_dest, 
        installers_dest,
        zips_dest, 
        code_dest,]

# Extensions
image_ext       = [".jpg", ".jpeg", ".jpe", ".jif", ".jfif", ".jfi", ".png", 
                    ".gif", ".webp", ".tiff", ".tif", ".psd", ".raw", ".arw", ".cr2", ".nrw",
                    ".k25", ".bmp", ".dib", ".heif", ".heic", ".kra", ".ase", ".ind", ".indd", ".indt", ".jp2", 
                    ".j2k", ".jpf", ".jpf", ".jpx", ".jpm", ".mj2", ".svg", ".svgz", ".ai", ".eps", ".ico",]
video_ext       = [".webm", ".mpg", ".mp2", ".mpeg", ".mpe", ".mpv", ".ogg", ".mkv",
                    ".mp4", ".mp4v", ".m4v", ".avi", ".wmv", ".mov", ".qt", ".flv", ".swf", ".avchd",]
audio_ext       = [".m4a", ".flac", "mp3", ".wav", ".wma", ".aac",]
document_ext    = [".doc", ".docx", ".odt", ".ods",
                       ".pdf", ".xls", ".xlsx", ".ppt", ".pptx", 
                       ".csv", ".json"]
executable_ext  = [".exe", ".jar", ".AppImage"]
installers_ext  = [".msi", ".deb", ".tar.gz"]
zip_ext         = [".zip", ".rar",]
code_ext        = [".ipynb", ".py", ".c", ".java", ".js", ".html", ".css", ".cpp", ".lua", ".gd", 
                   ".txt",]
# Master Extension List
ext = [image_ext,
     video_ext,
     audio_ext,
     document_ext,
     executable_ext,
     installers_ext,
     zip_ext,
     code_ext,]

# Checks if your set destinations and extensions are of equal count, as they should be
DIR_COUNT = len(dest) if len(dest) == len(ext) else 0
