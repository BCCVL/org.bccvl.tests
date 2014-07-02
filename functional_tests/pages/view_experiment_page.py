import hashlib
import os
from base_page import BasePage
from selenium import webdriver

class ViewExperimentPage(BasePage):
    def test(self):
        pass

    def select_results(self):
        self.driver.find_element_by_link_text("Results").click()

    def select_details(self):
        self.driver.find_element_by_link_text("Details").click()

    def downalod_experiment_results(self, file_name):
        self.driver.find_element_by_xpath("//a[@data-friendlyname='a_experimentoutput_" + file_name + "']").click()

    def has_result_file(self, filename):
        return self.check_text_displayed(filename)




