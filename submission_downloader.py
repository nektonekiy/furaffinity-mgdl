from submission_parser import SubmissionParser as SP
from file_system import Folder
import requests
import os

class SubmissionFolder:
    def __init__(self, submission_url: str, folder_path: str=os.getcwd()):
        self.submission_url = submission_url
        self.sp = SP(submission_url)
        self.folder_path_dviders = {
            "posix": "/",
            "nt": "\\"
        }
        self.folder = Folder(folder_path, self.sp.get_pic_title())

    def download_submission_content(self):
        sc_file_url = self.sp.get_content_file_url()
        if sc_file_url == None:
            return 
        filename = sc_file_url.split("/")[-1]
        file_path = f"{self.folder.folder_path}{self.folder_path_dviders[os.name]}{filename}" 
        r = requests.get(sc_file_url)
        with open(file_path, 'wb') as file:
            file.write(r.content)

    def download_description(self):
        filename = "desc.txt"
        file_path = f"{self.folder.folder_path}{self.folder_path_dviders[os.name]}{filename}" 
        desc_file_content = f"{self.sp.get_description()}\n\nDownloaded from: {self.submission_url}"
        try:
            with open(file_path, 'w') as file:
                file.write(desc_file_content)
        except UnicodeEncodeError:
            pass


