from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import StaleElementReferenceException


def retry_if_stale(wrapped_func):
    """
    Decorator to catch StaleElementReferenceException and retry given func.
    """
    def catch_stale_and_retry(*args, **kw):
        retry = 3
        while retry:
            try:
                return wrapped_func(*args, **kw)
            except StaleElementReferenceException, e:
                if retry:
                    retry -= 1
                    continue
                raise e
    return catch_stale_and_retry


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
