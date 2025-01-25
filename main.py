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
    
    print("Fetching submissions links...")
    gp = GP(artist_url, "gallery")
    submissions_urls = gp.get_submissions_urls()

    bar = IncrementalBar("Downloading pictures and descriptions...", max=len(submissions_urls))
    for submission_url in submissions_urls:
        sf = SF(submission_url, root_folder.folder_path)
        sf.download_submission_content()
        sf.download_description()
        bar.next()

if __name__ == "__main__":
    main()

