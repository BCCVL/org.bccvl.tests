from homepage import Homepage
from experiment_list_page import ExperimentListPage
from datasets_page import DatasetsPage


class LoggedInHomepage(Homepage):

    def click_experiments(self):
        self.driver.find_element_by_link_text("Experiments").click()
        experiment_homepage = ExperimentListPage(self.driver)
        return experiment_homepage

    def click_datasets(self):
        self.driver.find_element_by_link_text("Datasets").click()
        datasets_page = DatasetsPage(self.driver)
        return datasets_page

    def click_logout(self):
        from homepage import Homepage
        self.driver.find_element_by_link_text("admin").click()
        self.driver.find_element_by_link_text("Log out").click()
        return Homepage(self.driver)
