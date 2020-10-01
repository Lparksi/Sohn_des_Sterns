import requests


def getDailyImage():
    bashUrl = 'https://cn.bing.com/HPImageArchive.aspx?format=js&idx=0&n=1'
    r = requests.get(bashUrl)
    imageUrl = 'https://cn.bing.com' + r.json()['images'][0]['images']
    return imageUrl
