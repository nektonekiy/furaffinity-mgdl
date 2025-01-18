from post_parser import PostParser as PP
from file_system import Folder
import requests
import os

class PostFolder:
    def __init__(self, post_url: str, folder_path: str=os.getcwd()):
        self.post_url = post_url
        self.pp = PP(post_url)
        self.folder_path_dviders = {
            "posix": "/",
            "nt": "\\"
        }
        self.folder = Folder(folder_path, self.pp.get_pic_title())

    def download_picture(self):
        print("Downloading picture")
        pic_file_url = self.pp.get_pic_file_url()
        filename = pic_file_url.split("/")[-1]
        file_path = f"{self.folder.folder_path}{self.folder_path_dviders[os.name]}{filename}" 
        r = requests.get(pic_file_url)
        with open(file_path, 'wb') as file:
            file.write(r.content)

    def download_description(self):
        print("Downloading description")
        filename = "desc.txt"
        file_path = f"{self.folder.folder_path}{self.folder_path_dviders[os.name]}{filename}" 
        desc_file_content = f"{self.pp.get_pic_description()}\n\nDownloaded from: {self.post_url}"
        with open(file_path, 'w') as file:
            file.write(desc_file_content)
