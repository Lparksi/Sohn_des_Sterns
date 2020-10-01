import requests


def getDailyImage():
    bashUrl = 'https://cn.bing.com/HPImageArchive.aspx?format=js&idx=0&n=1'
    r = requests.get(bashUrl)
    imageUrl = 'https://cn.bing.com' + r.json()['images'][0]['url']
    return imageUrl


def getBingImage():
    return "https://uploadbeta.com/api/pictures/random/?key=BingEverydayWallpaperPicture"
