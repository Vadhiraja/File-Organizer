# imports:
import os
import shutil
import sys

#Check for duplicate folders and Create new folders
def create_folders(directories, Downloads):
    """
    This function creates the folders in <Downloads> where the files
    will be moved to.
    """
    for key in directories:
        if key not in os.listdir(Downloads):
            os.mkdir(os.path.join(Downloads, key))
    if "OTHER" not in os.listdir(Downloads):
        os.mkdir(os.path.join(Downloads, "OTHER"))



def organize_folders(directories, Downloads):
    """This function organizes the files in the specified folder into folders
    """
    for file in os.listdir(Downloads):
        if os.path.isfile(os.path.join(Downloads, file)):
            src_path = os.path.join(Downloads, file)
            for key in directories:
                extension = directories[key]
                if file.endswith(extension):
                    dest_path = os.path.join(Downloads, key, file)
                    shutil.move(src_path, dest_path)
                    break

#If the folder contains files other than the specified extensions
def organize_remaining_files(Downloads):
    
    for file in os.listdir(Downloads):
        if os.path.isfile(os.path.join(Downloads, file)):
            src_path = os.path.join(Downloads, file)
            dest_path = os.path.join(Downloads, "OTHER", file)
            shutil.move(src_path, dest_path)


def organize_remaining_folders(directories, Downloads):
    
    list_dir = os.listdir(Downloads)
    organized_folders = []
    for folder in directories:
        organized_folders.append(folder)
    organized_folders = tuple(organized_folders)
    for folder in list_dir:
        if folder not in organized_folders:
            src_path = os.path.join(Downloads, folder)
            dest_path = os.path.join(Downloads, "FOLDERS", folder)
            try:
                shutil.move(src_path, dest_path)
            except shutil.Error:
                shutil.move(src_path, dest_path + " - copy")
                print("That folder already exists in the destination folder."
                      "\nThe folder is renamed to '{}'".format(folder + " - copy"))


if __name__ == '__main__':
    Downloads = "C:/Users/91911/Downloads"
    directories = {
        "HTML": (".html5", ".html", ".htm", ".xhtml"),
        "Images": (".jpeg", ".jpg", ".tiff", ".gif", ".bmp", ".png", ".bpg",
                   "svg",
                   ".heif", ".psd"),
        "Videos": (".avi", ".flv", ".wmv", ".mov", ".mp4", ".webm", ".vob",
                   ".mng",
                   ".qt", ".mpg", ".mpeg", ".3gp", ".mkv"),
        "Documents": (".oxps", ".epub", ".pages", ".docx", ".doc", ".fdf",
                      ".ods",
                      ".odt", ".pwi", ".xsn", ".xps", ".dotx", ".docm", ".dox",
                      ".rvg", ".rtf", ".rtfd", ".wpd", ".xls", ".xlsx", ".ppt",
                      "pptx"),
        "Archives": (".a", ".ar", ".cpio", ".iso", ".tar", ".gz", ".rz", ".7z",
                     ".dmg", ".rar", ".xar", ".zip"),
        "Audio": (".aac", ".aa", ".aac", ".dvf", ".m4a", ".m4b", ".m4p",
                  ".mp3",
                  ".msv", "ogg", "oga", ".raw", ".vox", ".wav", ".wma"),
        "PlainText": (".txt", ".in", ".out"),
        "PDF": ".pdf",
        "Python": ".py",
        "EXE": ".exe",
        "Others": "",
        "FOLDERS": ""
    }
    try:
        create_folders(directories, Downloads)
        organize_folders(directories, Downloads)
        organize_remaining_files(Downloads)
        organize_remaining_folders(directories, Downloads)
    except shutil.Error:
        print("There was an error trying to move an item to its destination folder")

