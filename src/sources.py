# Targeted Folder: Modifiy When Needed
FOLDER_PATH = "C:\\Users\\user\\Downloads"


# Directories to create and use within Targeted Folder
dest_dir_music = f"{FOLDER_PATH}\\music"
dest_dir_video = f"{FOLDER_PATH}\\videos"
dest_dir_image = f"{FOLDER_PATH}\\images"
dest_dir_documents = f"{FOLDER_PATH}\\documents"
dest_dir_executables = f"{FOLDER_PATH}\\executables"
dest_dir_zips = f"{FOLDER_PATH}\\zips"
dest_dir_code = f"{FOLDER_PATH}\\code"
dest = [dest_dir_music, 
        dest_dir_video, 
        dest_dir_image, 
        dest_dir_documents, 
        dest_dir_executables, 
        dest_dir_zips, 
        dest_dir_code,]


# Supported Files: Modify when needed
image_extensions = [".jpg", ".jpeg", ".jpe", ".jif", ".jfif", ".jfi", ".png", 
                    ".gif", ".webp", ".tiff", ".tif", ".psd", ".raw", ".arw", ".cr2", ".nrw",
                    ".k25", ".bmp", ".dib", ".heif", ".heic", ".kra", ".ase", ".ind", ".indd", ".indt", ".jp2", 
                    ".j2k", ".jpf", ".jpf", ".jpx", ".jpm", ".mj2", ".svg", ".svgz", ".ai", ".eps", ".ico",]

video_extensions = [".webm", ".mpg", ".mp2", ".mpeg", ".mpe", ".mpv", ".ogg", ".mkv",
                    ".mp4", ".mp4v", ".m4v", ".avi", ".wmv", ".mov", ".qt", ".flv", ".swf", ".avchd",]

audio_extensions = [".m4a", ".flac", "mp3", ".wav", ".wma", ".aac",]

document_extensions = [".doc", ".docx", ".odt", ".ods",
                       ".pdf", ".xls", ".xlsx", ".ppt", ".pptx", 
                       ".csv",]

executable_extensions = [".exe", ".jar", ".msi",]

zip_extensions = [".zip", ".rar",]

code_extensions = [".ipynb", ".py", ".c", ".java", ".js", ".html", ".css", ".cpp", ".lua", ".gd", 
                   ".txt",]