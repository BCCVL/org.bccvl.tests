import os
from base_page import BasePage
from new_sdm_experiment_page import NewSDMExperimentPage
from view_experiment_page import ViewExperimentPage


class ExperimentsPage(BasePage):

    def click_new_sdm_experiment(self):
        self.driver.find_element_by_link_text("new SDM Experiment").click()
        new_sdm_experiment_page = NewSDMExperimentPage(self.driver)
        return new_sdm_experiment_page

    def click_existing_experiment(self, path):
        self.driver.find_element_by_xpath("//a[@href='" + os.environ['URL'] +"/experiments/"+ path + "']").click()
        view_experiment_page = ViewExperimentPage(self.driver)
        return view_experiment_page