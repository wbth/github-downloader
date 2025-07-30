# github-downloader

This script automatically downloads all PDF files from a folder in a GitHub repository. 
First, the script accesses the folder's contents using the GitHub API. After obtaining the list of files, it filters only those of type document and then downloads them one by one using the direct link provided by GitHub (download_url). The downloaded files are saved to a local folder, which will be created automatically if it doesn't already exist.
This way, users can access all PDF files from the folder without having to manually download them one by one.
