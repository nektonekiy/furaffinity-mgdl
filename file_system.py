import os
import demoji

class Folder:
    def __init__(self, folder_location: str, folder_name: str):
        def filter_forbidden_symbols(name: str):
            print("Filtering forbidden symbols")
            filtred_name = demoji.replace_with_desc(name, sep="")
            forbidden_symbols = ["<",">",":","/","\\","\"","|","?","*"]
            for forbidden_symbol in forbidden_symbols:
                filtred_name = filtred_name.replace(forbidden_symbol,"[FORBIDDEN SYMBOL]")
            return filtred_name
        self.folder_name = filter_forbidden_symbols(folder_name)
        folder_path_dviders = {
            "posix": "/",
            "nt": "\\"
        }
        print("Creating folder")
        try:
            self.folder_path = f"{folder_location}{folder_path_dviders[os.name]}{self.folder_name}"
            os.mkdir(self.folder_path)
        except FileExistsError:
            folder_name_number = 1
            is_created = False
            while not is_created:
                try:
                    self.folder_path = f"{folder_location}{folder_path_dviders[os.name]}{self.folder_name} ({folder_name_number})"
                    os.mkdir(self.folder_path)
                    is_created = True
                except:
                    folder_name_number+=1
