import os
from base_page import BasePage
from experiment_sdm_page import SDMExperimentPage
from experiment_projection_page import ProjectionExperimentPage
from experiment_biodiverse_page import BiodiverseExperimentPage
from experiment_results_page import ExperimentResultsPage
from sharing_page import SharingPage

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

    def click_new_biodiverse_experiment(self):
        self.driver.find_element_by_link_text("new Biodiverse Experiment").click()
        new_biodiverse_experiment = BiodiverseExperimentPage(self.driver)
        return new_biodiverse_experiment

    def click_share_experiment(self, experiment_name):
        buttons = self.driver.find_elements_by_css_selector("table.bccvl-experimenttable tbody tr td.bccvl-table-controls a.sharing-btn")

        # Returns a list of TRs.
        # they are in duples like:
        # - title
        # - type
        # There is no easy way to differentiate them
        tds = self.driver.find_elements_by_css_selector("table.bccvl-experimenttable tbody tr td.bccvl-table-label")

        # Extract all the titles. (i.e. every 2nd one)
        names = []
        index = 0
        for td in tds:
            index = index % 2
            if index == 0:
                # put them into names
                # get the h1 which is the actual text of the name
                names.append(td.find_element_by_css_selector("h1"))
            index = index + 1

        # there should be a share button for every experiment
        assert len(buttons) == len(names)

        # Now go through the list of name webelements to find the index of the one
        # that has the same name as what we're looking for
        # and click on it that element.
        index = 0
        for name in names:
            if experiment_name in name.text:
                buttons[index].click()
                return SharingPage(self.driver)
            else:
                index = index + 1

        # Shouldn't reach this point unless nothing was clicked
        assert False is True
        return

    # After selecting share you can search for users
    def enter_user_search(self, name):
        self.driver.find_element_by_id('sharing-user-group-search').clear()
        self.driver.find_element_by_id('sharing-user-group-search').send_keys(name)


    # Returns a list of all the names of the experiments.
    def get_experiment_list(self):
        experiments = []

        # Every 2nd one is the experiment type - discard
        elements = self.driver.find_elements_by_css_selector('table.bccvl-experimenttable tbody tr h1')
        discard = False
        for element in elements:
            if discard is True:
                discard = False
                continue
            else:
                discard = True
                experiments.append(element.text.lower())

        return experiments




