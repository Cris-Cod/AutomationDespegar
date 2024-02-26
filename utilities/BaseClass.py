import time

import pytest
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait


@pytest.mark.usefixtures("setup")
class BaseClass:

    def selectByText(self, locator, text):
        dropdown = Select(locator)
        dropdown.select_by_visible_text(text)

    def scroll(self):
        self.driver.execute_script("window.scrollBy(0, 600)")

    def verifyLinkPresence(self, text):
        wait = WebDriverWait(self.driver, 3)
        wait.until(EC.visibility_of_element_located((By.LINK_TEXT, text)))

    def times(self, second):
        return time.sleep(second)

    def element_is_visible(self, locator):
        wait = WebDriverWait(self.driver, 20)
        wait.until(EC._element_if_visible(locator))
