import pandas as pd 
import urllib.request


URL_PATH = '' # csv file where image URL contain
FILE_PATH = '' #create local folder path to download URL images

def url_jpg(URL_PATH, FILE_PATH):
    URLS = pd.read_csv(URL_PATH)
    name = URLS['Images']
    for n in name: 
        check = n.split('/')[-1]
    url = []
    for i in enumerate(URLS.values):
        links = i[1][0] #rows and columns
        url.append(links)

    for j in range(len(url)):
        name = check.split('/')[-1][:-4]
        fileName = ('{}.jpg'.format(name))
        imagePath = ('{}{}'.format(FILE_PATH, fileName))
        urllib.request.urlretrieve(url[j], imagePath)
        print('{} saved.'.format(fileName))
url_jpg(URL_PATH, FILE_PATH)
