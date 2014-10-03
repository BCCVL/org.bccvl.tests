from base_page import BasePage
from logged_in_homepage import LoggedInHomepage


class LoginPage(BasePage):

    def valid_login(self, username, password):
        self.driver.find_element_by_css_selector("a.bccvllinks-login").click()
        self.driver.find_element_by_id("login-basic").click()
        self.driver.find_element_by_id("__ac_name").send_keys(username)
        self.driver.find_element_by_id("__ac_password").clear()
        self.driver.find_element_by_id("__ac_password").send_keys(password)
        self.driver.find_element_by_id("legals-checkbox").click()
        self.driver.find_element_by_css_selector("input.btn-success").click()
        logged_in_homepage = LoggedInHomepage(self.driver)
        return logged_in_homepage
