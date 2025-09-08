# Targeted Folder: Modifiy When Needed
FOLDER_PATH = "C:\\Users\\user\\Downloads"
# Update all of these when needed
# Order: image - video - audio - documents - executables - zips - code

# Destinations
image_dest = f"{FOLDER_PATH}\\images"
video_dest = f"{FOLDER_PATH}\\videos"
audio_dest = f"{FOLDER_PATH}\\audio"
documents_dest = f"{FOLDER_PATH}\\documents"
executables_dest = f"{FOLDER_PATH}\\executables"
zips_dest = f"{FOLDER_PATH}\\zips"
code_dest = f"{FOLDER_PATH}\\code"
# Master Destination List
dest = [image_dest, 
        video_dest, 
        audio_dest, 
        documents_dest, 
        executables_dest, 
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
                       ".csv",]
executable_ext  = [".exe", ".jar", ".msi",]
zip_ext         = [".zip", ".rar",]
code_ext        = [".ipynb", ".py", ".c", ".java", ".js", ".html", ".css", ".cpp", ".lua", ".gd", 
                   ".txt",]
# Master Extension List
ext = [image_ext,
     video_ext,
     audio_ext,
     document_ext,
     executable_ext,
     zip_ext,
     code_ext,]

# Checks if your set destinations and extensions are of equal count, as they should be
DIR_COUNT = len(dest) if len(dest) == len(ext) else 0