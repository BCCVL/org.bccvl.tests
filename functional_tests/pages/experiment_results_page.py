from selenium.webdriver.support.ui import WebDriverWait
from datasets_list_page import DatasetsListPage
from base_page import BasePage


class ExperimentResultsPage(BasePage):

    # The maximum amount of time to wait for experiments to complete. 15mins
    # Once this time has elapsed, the tests will fail.
    experiment_complete_timeout = 60 * 15

    results_table_id = 'bccvl-experimentresults-table'
    experiment_status_completed = 'COMPLETED'
    experiment_status_failed = 'FAILED'

    def has_results_header(self, header):
        table_header = self._get_result_table_header()
        return header in table_header.text

    def has_result_file(self, filename, algorithm=None):
        out_files = self._get_output_file_names(algorithm)
        return len(filter(lambda f: f.text == filename, out_files)) == 1

    def get_num_output_files(self):
        return len(self._get_output_file_names())

    def has_completed_successfully(self):
        return self.experiment_status_completed == self._get_experiment_status()

    def click_datasets(self):
        self.driver.find_element_by_css_selector('a.bccvllinks-datasets').click()
        new_dataset_list_page = DatasetsListPage(self.driver)
        return new_dataset_list_page

    def click_experiments(self):
        self.driver.find_element_by_css_selector('a.bccvllinks-experiments').click()
        from experiment_list_page import ExperimentListPage
        new_dataset_list_page = ExperimentListPage(self.driver)
        return new_dataset_list_page

    def has_completed_with_failure(self):
        return self.experiment_status_failed == self._get_experiment_status()

    def wait_for_experiment_to_complete(self):
        WebDriverWait(self.driver, self.experiment_complete_timeout).until(lambda s: self._is_experiment_complete())

    def _get_output_file_names(self, algorithm=None):

        if algorithm == None: # return all
            return self.driver.find_elements_by_css_selector("table#" + self.results_table_id + " p")
        else: # only return the ones relevant to the algorithm
            items = self.driver.find_elements_by_css_selector("table#" + self.results_table_id + " tbody tr td:first-child")

            # make a list
            results = []
            # keep track of current label
            current_label = None
            for item in items:
                # if it's a label, try match it
                if item.text.find(" - ") != -1: # We found a label
                    if current_label is not None: # Maybe we've already actually finished
                        break
                    if item.text.find(" - " + algorithm) != -1:
                        if current_label is not None:
                            break
                        else:
                            # Remember the algorithm we're working on
                            current_label = algorithm

                # if it's a file,
                else:
                    # see if we're in the right category
                    if current_label is None: # we haven't found our label yet
                        continue;
                    else:
                        # Append the filename onto the list
                        results.append(item.find_element_by_css_selector("p"))

            return results

    def _get_result_table_header(self):
        return self.driver.find_element_by_xpath("//table[@id='" + self.results_table_id + "']/tbody/tr[@class='info']/td")

    def _get_experiment_status(self):
        return self.driver.find_element_by_css_selector("div.bccvl-expstatus").get_attribute("data-status")

    def _is_experiment_complete(self):
        experiment_status = self._get_experiment_status()
        return experiment_status in [self.experiment_status_completed, self.experiment_status_failed]
