import time
from selenium.webdriver.support.select import Select
from selenium.common.exceptions import NoSuchElementException
from bccvl_testcase import BCCVLTestCase


# This is the base class of all classes that test experiments.
# Used so we can keep track of experiments & delete them afterwards.
class ExperimentTestCase(BCCVLTestCase):

    def delete_all_experiments(self):
        self.driver.get(self.url+'/experiments/manage_main')
        self.driver.find_element_by_name('selectButton').click()
        self.driver.find_element_by_name('manage_delObjects:method').click()

    def delete_experiment(self, experiment_name):
        self.driver.get(self.url+'/experiments/manage_main')
        end_time = time.time() + 60
        while time.time() <= end_time:
            if self._check_exists_by_xpath("//option[@value='" + experiment_name + "']"):
                break
            self.driver.refresh()
        select = Select(self.driver.find_element_by_xpath("//select[@name='ids:list']"))
        select.select_by_value(experiment_name)
        self.driver.find_element_by_name("manage_delObjects:method").click()

    # Note: This method will block if the element was not immediately visible.
    # The amount of time that this will block depends on the call to self.driver.implicitly_wait in this class'
    # setUp(self)
    def _check_exists_by_xpath(self, xpath):
        try:
            self.driver.find_element_by_xpath(xpath)
        except NoSuchElementException:
            return False
        return True
