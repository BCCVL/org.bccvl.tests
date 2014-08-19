from selenium.webdriver.support.ui import WebDriverWait


class BasePage():

    def __init__(self, driver):
        self.driver = driver
        self.title = driver.title

    def is_jquery_active(self):
        return self.driver.execute_script('return jQuery.active') != 0

    def switch_tab(self, link_text):
        self.driver.find_element_by_link_text(link_text).click()
        # wait for ajax calls to finish
        WebDriverWait(self.driver, 10).until(lambda s: not self.is_jquery_active())
