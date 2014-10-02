from base_page import BasePage
from knowledge_base_page import KnowledgeBasePage
import time


class Homepage(BasePage):

    def click_knowledge_base(self):
        self.driver.find_element_by_link_text("Knowledge Base").click()
        knowledge_base_page = KnowledgeBasePage(self.driver)
        return knowledge_base_page

    def click_login(self):
        from login_page import LoginPage
        self.driver.find_element_by_css_selector("a.bccvllinks-login").click()
        time.sleep(1)
        login_page = LoginPage(self.driver)
        return login_page
