from artist_gallery_parser import GalleryParser as GP
from file_system import Folder 
from progress.bar import IncrementalBar
from submission_downloader import SubmissionFolder as SF
import sys
import os

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
    root_folder = Folder(os.getcwd(), artist_username)
    
    print("Fetching posts links...")
    gp = GP(artist_url, "gallery")
    posts_urls = gp.get_pics_urls()

    bar = IncrementalBar("Downloading pictures and descriptions...", max=len(posts_urls))
    for post_url in posts_urls:
        sf = SF(post_url, root_folder.folder_path)
        sf.download_picture()
        sf.download_description()
        bar.next()

if __name__ == "__main__":
    main()

