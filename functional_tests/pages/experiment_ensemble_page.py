from base_page import BasePage
from experiment_results_page import ExperimentResultsPage
from selenium.webdriver.support.select import Select


class EnsembleExperimentPage(BasePage):

    def enter_experiment_name(self, name):
        self.driver.find_element_by_name('form.widgets.IDublinCore.title').send_keys(name)

    def enter_experiment_description(self, description):
        self.driver.find_element_by_name('form.widgets.IDublinCore.description').send_keys(description)

    def click_source_data(self):
        self.driver.find_element_by_link_text('Source Data').click()

    def select_dataset_type(self, type):
        select = Select(self.driver.find_element_by_css_selector('select.bccvl-inputdatasettype'))
        select.select_by_value(type)

    def select_source_experiment(self, experiment_id):
        elements = self.driver.find_elements_by_css_selector('table.bccvl-sourceexperimenttable tbody tr')

        for element in elements:
            name = element.find_elements_by_css_selector('p')
            if len(name) == 0:
                continue
            else:
                if name[0].text == experiment_id:
                    element.find_element_by_css_selector('input').click()
                    return

        # Should never get here if you actually found what you were looking for
        assert True is False

    # NOTE: this method may throw exceptions relating to clicking on elements that are not visible.
    def select_available_file(self, filename):
        all_files = self.driver.find_elements_by_css_selector('table.bccvl-inputfiletable tr p')
        for file in all_files:
            if file.text == filename:
                # found it
                file.find_element_by_xpath("..").find_element_by_xpath("..").find_element_by_xpath("..").find_element_by_css_selector('td.bccvl-table-choose input').click()
                return

        # should not reach this point less it couldn't find your file.
        assert False is True

    def click_run(self):
        self.driver.find_element_by_link_text('Run').click()

    def click_start_experiment(self):
        self.driver.find_element_by_css_selector('button.bccvllinks-experiment-start').click()
        return ExperimentResultsPage(self.driver)
