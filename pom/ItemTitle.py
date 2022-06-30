from selenium.webdriver.remote.webelement import WebElement

from base.seleniumbase import SeleniumBase
from typing import List


class ItemTitle(SeleniumBase):
    def __init__(self, driver, titles_path):
        super(ItemTitle, self).__init__(driver)
        self.__titles_path = titles_path
        self.TITLES_TEXT = 'Sauce Labs Backpack,Sauce Labs Bike Light,Sauce Labs Bolt T-Shirt,Sauce Labs Fleece ' \
                           'Jacket,Sauce Labs Onesie,Test.allTheThings() T-Shirt (Red)'

    def get_title_items(self, titles_path) -> List[WebElement]:
        return self.are_visible('CSS', titles_path)

    def get_titles_text(self):
        titles = self.get_title_items(self.__titles_path)
        titles_text = [title.text for title in titles]
        return ','.join(titles_text)

