import os
from base_page import BasePage
from logged_in_homepage import LoggedInHomepage


class LoginPage(BasePage):

    def valid_login(self, username, password):
        self.driver.find_element_by_id("drop1").click()
        self.driver.implicitly_wait(5)
        self.driver.find_element_by_id("login-basic").click()
        self.driver.implicitly_wait(5)
        self.driver.find_element_by_id("__ac_name").clear()
        self.driver.find_element_by_id("__ac_name").send_keys(username)
        self.driver.implicitly_wait(5)
        self.driver.find_element_by_id("__ac_password").clear()
        self.driver.find_element_by_id("__ac_password").send_keys(password)
        self.driver.find_element_by_id("legals-checkbox").click()
        self.driver.find_element_by_name("submit").click()
        self.driver.implicitly_wait(100)
        logged_in_homepage = LoggedInHomepage(self.driver)
        return logged_in_homepage