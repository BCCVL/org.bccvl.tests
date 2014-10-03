from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC


class BasePage():

    def __init__(self, driver):
        self.driver = driver
        self.title = driver.title

    def is_jquery_active(self):
        return self.driver.execute_script('return jQuery.active') != 0

    def wait_for_jquery(self):
        WebDriverWait(self.driver, 10).until(lambda s: not self.is_jquery_active())

    def wait_for_visible(self, id):
        WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.ID, id)))

    def switch_tab(self, link_text):
        self.driver.find_element_by_link_text(link_text).click()
        # wait for ajax calls to finish
        self.wait_for_jquery()
