from selenium import webdriver
import urllib.request

class animeout():
    def download(self, link, browser):
        # browser = webdriver.Chrome()
        browser.get(link)

        a_elem = browser.find_elements_by_xpath("//a[@href]")

        links = ''
        for a in a_elem:
            title = a.text
            link = a.get_attribute('href')
            # print(title, link)
            if title == 'Download (Public Server)':
                links = link
                break

        print(links)
        browser.get(links)
        download = browser.execute_script("start();")
        # download = download.decode()

        #saving the file to a folder;
        # wget.download(download)

        # browser.close()

        # Saving as csv file
        # data = pd.DataFrame(links)
        # data.to_csv('BlackClover.csv')