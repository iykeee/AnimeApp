import sys
sys.path.insert(0, '/home/iykee/ik/lib/python3.9/site-packages')
import re
import time
import urllib.request

from bs4 import BeautifulSoup
from selenium import webdriver

from webcrawl.download import animeout
from selenium.webdriver.chrome.options import Options

options = Options()

options.add_argument('--no-sandbox')
options.add_argument('--headless')
options.add_argument('--disable-dev-shm-usage')

browser = webdriver.Chrome('/home/iykee/.config/google-chrome/chromedriver',options=options)

urlpage = 'https://www.animeout.xyz/shingeki-no-kyojin-the-final-season-1080p-300mb720p-150mbepisode-1/'

try:
        for y in range(60):
                try:
                        browser.get(urlpage)
                        break
                except:
                        if (y % 10 == 0):
                                print(f"Error in loading {urlpage}, kindly ensure your network is stable")
                                print("Page Timeout!")
                                if (y == 50):
                                        sys.exit()

        aTags = browser.find_elements_by_xpath("//a[@href]")
        # print(aTags)

        links = []
        wanted = []
        for a in aTags:
            title = a.text
            link = a.get_attribute('href')
            links.append({"Title" : title, "Links" : link})
            wanted.append(link)

        choice = []
        for link in wanted:
            if re.search('^http://nimbus.animeout.com/series/00RAPIDBOT.*mkv', link) or re.search('^http://nimbus.animeout.com/series/00RAPIDBOT.*mkv', link):
                choice.append(link)

        choice.reverse()

        url = choice[0]

        animeout.download("Boruto", url, browser)

except KeyboardInterrupt:
        pass
