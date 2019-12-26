from selenium import webdriver
from time import sleep
from selenium.webdriver.common.keys import Keys


class GetComments:
    def __new__(cls, url, number, prefix):
        driver = webdriver.Chrome()
        driver.get(url)
        comments = []
        html = driver.find_element_by_tag_name('html')
        sleep(3)

        while len(comments) < number:
            comments = [elem.text for elem in driver.find_elements_by_xpath('//*[@id="content-text"]')]
            sleep(.5)
            html.send_keys(Keys.PAGE_DOWN)

        return ' '.join([str(elem) for elem in [f"\n{prefix}" + x for x in comments]])
