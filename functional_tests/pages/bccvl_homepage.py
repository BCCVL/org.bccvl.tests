from base_page import BasePage
from experiments_page import ExperimentsPage
from datasets_page import DatasetsPage
from knowledge_base_page import KnowledgeBasePage

class BCCVLHomepage(BasePage):

    def click_experiments(self):
        self.driver.find_element_by_link_text("Experiments").click()
        experiment_homepage = ExperimentsPage(self.driver)
        return experiment_homepage

    def click_datasets(self):
        self.driver.find_element_by_link_text("Datasets").click()
        datasets_page = DatasetsPage(self.driver)
        return datasets_page

    def click_knowledge_base(self):
        self.driver.find_element_by_link_text("Knowledge Base").click()
        knowledge_base_page = KnowledgeBasePage(self.driver)
        return knowledge_base_page

    def valid_login(self, username, password):
        self.driver.find_element_by_id("personaltools-login").click()
        self.driver.implicitly_wait(5)
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
        return self