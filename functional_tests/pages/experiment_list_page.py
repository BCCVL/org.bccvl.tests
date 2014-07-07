import os
from base_page import BasePage
from experiment_sdm_page import SDMExperimentPage
from experiment_projection_page import ProjectionExperimentPage
from experiment_results_page import ExperimentResultsPage


class ExperimentListPage(BasePage):

    def click_new_sdm_experiment(self):
        self.driver.find_element_by_link_text("new SDM Experiment").click()
        new_sdm_experiment_page = SDMExperimentPage(self.driver)
        return new_sdm_experiment_page

    def click_existing_experiment(self, path):
        self.driver.find_element_by_xpath("//a[@href='" + os.environ['URL'] + "/experiments/" + path + "']").click()
        view_experiment_page = ExperimentResultsPage(self.driver)
        return view_experiment_page

    def click_new_projection_experiment(self):
        self.driver.find_element_by_link_text("new Projection Experiment").click()
        new_projection_experiment = ProjectionExperimentPage(self.driver)
        return new_projection_experiment