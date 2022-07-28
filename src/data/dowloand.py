import gdown
import zipfile
import os

def main(url, output):
    
    gdown.download(url, os.path.join(output,"visum.zip"), quiet=False)
    with zipfile.ZipFile(os.path.join(output,"visum.zip"),'r') as zip_ref:
       zip_ref.extractall(output)
    os.remove(os.path.join(output,"visum.zip"))

if __name__ == "__main__":
    url = "https://drive.google.com/u/0/uc?id=1gOIA55wF16J92VjcYkFkf4FbjAv2OciR&export=download"
    output = "./data/interim/"
    main(url, output)
