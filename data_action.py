import pandas as pd
import os
import requests

def get_data(url):
    #df = pd.DataFrame()
    url = url
    csv_name = url[url.rfind("/")+1:]
    check = ""
    if os.path.exists(csv_name):
        #print("File exists locally, skipping download.")
        check = "File exists locally, skipping download."
    else:
        try:
            req = requests.get(url)
            assert req.status_code == 200 # if the download failed, this line will generate an error
            with open(csv_name, 'wb') as f:
                f.write(req.content)
            #df = pd.read_csv(csv_name)
            #print("Download performed successfully.")
            check = "Download performed successfully." 
        except AssertionError: 
            #print("URL does not point to a file that exists.")
            check = "URL does not point to a file that exists."
    return check

def delete_data(url):
    url = url
    csv_name = url[url.rfind("/")+1:]
    check = ""
    try:
        os.remove(csv_name)
        #print("File successfully removed locally.")
        check = "File successfully removed locally."
    except FileNotFoundError:
        #print("File from URL not found locally.")
        check = "File from URL not found locally."
    return check