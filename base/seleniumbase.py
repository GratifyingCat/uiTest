from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.ui import WebDriverWait
from typing import List


def by(find_by: str) -> str:
    find_by = find_by.lower()
    locating = {
        'css': By.CSS_SELECTOR,
        'xpath': By.XPATH,
        'class_name': By.CLASS_NAME,
        'id': By.ID,
        'link_text': By.LINK_TEXT,
        'name': By.NAME,
        'partial_link_text': By.PARTIAL_LINK_TEXT,
        'tag_name': By.TAG_NAME
    }
    return locating[find_by]


class SeleniumBase:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 15, 0.3)

    def is_visible(self, find_by: str, locator: str, locator_name: str = None) -> WebElement:
        return self.wait.until(expected_conditions.visibility_of_element_located((by(find_by), locator)), locator_name)

    def are_visible(self, find_by: str, locator: str, locator_name: str = None) -> List[WebElement]:
        return self.wait.until(expected_conditions.visibility_of_all_elements_located((by(find_by), locator)),
                               locator_name)
