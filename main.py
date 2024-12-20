from artist_gallery_parser import GalleryParser as GP
from post_parser import PostParser as PP
from progress.bar import IncrementalBar
import requests
import os

def main():
    artist_url = input("Enter artist's gallery url: ").strip().split("/")
    if artist_url[-1] == "":
        artist_url.pop()
    artist_url = "/".join(artist_url)
    print(artist_url)
    artist_username = artist_url.split("/")[-1]
    os.mkdir(artist_username)
    gp = GP(artist_url)

    pics_urls = gp.get_pics_urls()

    bar = IncrementalBar("Downloading", max=len(pics_urls))

    for pic_url in pics_urls:
        pp = PP(pic_url)
        if os.name == "posix":
            folder_path = artist_username + "/" + pp.get_pic_title()
        elif os.name == "nt":
            folder_path = artist_username + "\\" + pp.get_pic_title()
        os.mkdir(folder_path)
       
        pic_url = pp.get_pic_file_url()
        filename = "pic" + pic_url.split("/")[-1]           
        if os.name == "posix":
            file_path = folder_path + "/" + filename
        elif os.name == "nt":
            file_path = folder_path + "\\" + filename
        r = requests.get(pic_url)
        with open(file_path, 'wb') as file:
            file.write(r.content)

        filename = "description.txt"
        if os.name == "posix":
            file_path = folder_path + "/" + filename
        elif os.name == "nt":
            file_path = folder_path + "\\" + filename 
        with open(file_path, 'w') as file:
            file.write(pp.get_pic_description())
        bar.next()

if __name__ == "__main__":
    main()

