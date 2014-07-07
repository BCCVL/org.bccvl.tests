from selenium.webdriver.support.ui import WebDriverWait
from base_page import BasePage


class ExperimentResultsPage(BasePage):

    results_table_id = 'bccvl-experimentresults-table'
    experiment_status_completed = 'COMPLETED'
    experiment_status_failed = 'FAILED'

    def has_results_header(self, header):
        table_header = self._get_result_table_header()
        return header in table_header.text

    def has_result_file(self, filename):
        out_files = self._get_output_file_names()
        return len(filter(lambda f: f.text == filename, out_files)) == 1

    def get_num_output_files(self):
        return len(self._get_output_file_names())

    def has_completed_successfully(self):
        return self.experiment_status_completed == self._get_experiment_status()

    def has_completed_with_failure(self):
        return self.experiment_status_failed == self._get_experiment_status()

    def wait_for_experiment_to_complete(self, seconds):
        WebDriverWait(self.driver, seconds).until(lambda s: self._is_experiment_complete())

    def _get_output_file_names(self):
        return self.driver.find_elements_by_xpath("//table[@id='" + self.results_table_id + "']/tbody/tr/td/h1")

    def _get_result_table_header(self):
        return self.driver.find_element_by_xpath("//table[@id='" + self.results_table_id + "']/tbody/tr[@class='info']/td")

    def _get_experiment_status(self):
        return self.driver.find_element_by_css_selector("div.bccvl-expstatus").get_attribute("data-status")

    def _is_experiment_complete(self):
        experiment_status = self._get_experiment_status()
        return experiment_status in [self.experiment_status_completed, self.experiment_status_failed]
