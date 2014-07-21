from homepage import Homepage
from experiment_list_page import ExperimentListPage
from datasets_list_page import DatasetsListPage


class LoggedInHomepage(Homepage):

    def click_experiments(self):
        self.driver.find_element_by_link_text("Experiments").click()
        experiment_homepage = ExperimentListPage(self.driver)
        return experiment_homepage

    def click_datasets(self):
        self.driver.find_element_by_link_text("Datasets").click()
        datasets_page = DatasetsListPage(self.driver)
        return datasets_page

    def click_logout(self, username="admin"):
        from homepage import Homepage
        self.driver.find_element_by_link_text(username).click()
        self.driver.find_element_by_link_text("Log out").click()
        return Homepage(self.driver)
