from artist_gallery_parser import GalleryParser as GP
from post_parser import PostParser as PP
from progress.bar import IncrementalBar
import requests
import os
import sys
import demoji

def main():
    try:
        artist_url = sys.argv[1].strip().split("/")
    except IndexError:
        print("Oops... Enter artist's gallery url")
        sys.exit()
    if artist_url[-1] == "":
        artist_url.pop()
    artist_url = "/".join(artist_url)
    artist_username = artist_url.split("/")[-1]
    os.mkdir(artist_username)

    print("Fetching posts links...")
    gp = GP(artist_url)
    pics_urls = gp.get_pics_urls()

    bar = IncrementalBar("Downloading pictures and descriptions...", max=len(pics_urls))

    for pic_url in pics_urls:
        pp = PP(pic_url)
        folder_path_dviders = {
                "posix": "/",
                "nt": "\\"
            }
        def create_post_folder():
            folder_name = demoji.replace_with_desc(pp.get_pic_title(), sep="")
            try:
                folder_path = f"{artist_username}{folder_path_dviders[os.name]}{folder_name}"
                os.mkdir(folder_path)
            except FileExistsError:
                folder_name_number = 1
                is_created = False
                while not is_created:
                    try:
                        folder_path = f"{artist_username}{folder_path_dviders[os.name]}{pp.get_pic_title()} ({folder_name_number})"
                        os.mkdir(folder_path)
                        is_created = True
                    except:
                        folder_name_number+=1
            return folder_path

        folder_path = create_post_folder()

        pic_url = pp.get_pic_file_url()
        filename = "pic" + pic_url.split("/")[-1]           
        file_path = f"{folder_path}{folder_path_dviders[os.name]}{filename}"
        r = requests.get(pic_url)
        with open(file_path, 'wb') as file:
            file.write(r.content)

        filename = "description.txt"
        file_path = f"{folder_path}{folder_path_dviders[os.name]}{filename}" 
        desc_file_content = f"{pp.get_pic_description()}\n\nDownloaded from: {pic_url}"
        with open(file_path, 'w') as file:
            file.write(desc_file_content)
        bar.next()

if __name__ == "__main__":
    main()

