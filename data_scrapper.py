import requests
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import urllib.request
from PIL import Image

def download(fileName, urlStr):
    with open(fileName, 'wb') as f:
        x = requests.get(urlStr, headers={'User-Agent': 'My User Agent 1.0'}).content
        f.write(x)

if __name__ == '__main__':

    DRIVER_PATH = "C:\\Users\\lenovo\\Desktop\\fastai\\chromedriver",
    wd = webdriver.Chrome(executable_path=DRIVER_PATH)

    queryStr = 'cat'

    urlstr = "https://www.google.com.sg/search?q={}&source=lnms&tbm=isch&sa=X&ei=0eZEVbj3IJG5uATalICQAQ&ved=0CAcQ_AUoAQ&biw=939&bih=591".format(queryStr)
    wd.get(urlstr)

    element = wd.find_elements_by_tag_name('img')
    prev = -1
    while (len(element) != prev):
        prev = len(element)
        time.sleep(5)
        wd.execute_script("window.scrollTo(0, 60000)")
        time.sleep(5)
        element = wd.find_elements_by_tag_name('img')

    c = 1
    for item in element:
        src = item.get_attribute('src')
        if (src is not None):
            try:
                download("image_{}.jpg".format(c), src)
                print("Downloaded image_{}.jpg".format(c))
                c = c + 1
            except:
                print("Unable to download")

    wd.close()
    
