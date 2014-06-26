from base_page import BasePage
from experiments_page import ExperimentsPage
from datasets_page import DatasetsPage
from knowledge_base_page import KnowledgeBasePage


class LoggedInHomepage(BasePage):

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

	def click_logout(self):
		from homepage import Homepage
		self.driver.find_element_by_link_text("admin").click()
		self.driver.find_element_by_link_text("Log out").click()
		return Homepage(self.driver)