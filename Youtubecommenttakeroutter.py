from selenium import webdriver
from time import sleep
from selenium.webdriver.common.keys import Keys


class GetComments:
    def __new__(cls, url, number, prefix):
        driver = webdriver.Chrome()
        driver.get(url)
        html = driver.find_element_by_tag_name('html')
        sleep(3)

        while len(driver.find_elements_by_xpath('//*[@id="content-text"]')) < number:
            html.send_keys(Keys.PAGE_DOWN)
            print(len(driver.find_elements_by_xpath('//*[@id="content-text"]')))
            sleep(.1)

        comments = [elem.text for elem in driver.find_elements_by_xpath('//*[@id="content-text"]')]

        return ' '.join([str(elem) for elem in [f"\n{prefix}" + x for x in comments]])


print(GetComments("https://www.youtube.com/watch?v=DU2AFIOnw_c", 300, "Comment:"))
