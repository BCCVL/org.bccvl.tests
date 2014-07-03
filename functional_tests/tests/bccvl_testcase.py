import unittest
import os
import time
from pyvirtualdisplay import Display
from selenium import webdriver
from selenium.webdriver.support.select import Select
from selenium.common.exceptions import NoSuchElementException


# Base Test Cases used to test BCCVL
class BCCVLTestCase(unittest.TestCase):

    def setUp(self):
        # acquire URL, username and password from environment variables, or use default values for dev env.
        self.username = os.getenv('BCCVL_TEST_USERNAME', 'admin')
        self.password = os.getenv('BCCVL_TEST_PASSWORD', 'admin')
        self.url = os.getenv('BCCVL_TEST_URL', 'https://192.168.100.200/')

        # The amount of time selenium will potentially wait in searching for elements. This is blocking.
        implicit_wait = int(os.getenv('BCCVL_TEST_IMPLICIT_WAIT', '5'))

        # Run tests in a virtual display (xvfb)
        virtual_display = os.getenv('BCCVL_TEST_VIRTUAL_DISPLAY', 'false') == 'true'

        # Setup the virtual display
        if virtual_display:
            self.display = Display(visible=0, size=(1920, 1080))
            self.display.start()
        else:
            self.display = None

        # Setup the Firefox Profile and webdriver
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(implicit_wait)
        # Maximize the window
        self.driver.maximize_window()
        # Go to the bccvl homepage
        self.driver.get(self.url)
        self.experiments = []

    def tearDown(self):
        # if experiments were created during this test then delete them
        for experiment in self.experiments:
            self.delete_experiment(experiment)
        if self.display:
            self.display.stop()
        self.driver.quit()

    def delete_dataset(self, title):
        self.driver.get(self.url+'/datasets/manage_main')
        # TODO: write this method when doing datasets page tests

    def delete_experiment(self, title):
        self.driver.get(self.url+'/experiments/manage_main')
        end_time = time.time() + 60
        while time.time() <= end_time:
            if self._check_exists_by_xpath("//option[@value='" + title + "']"):
                break
            self.driver.refresh()
        select = Select(self.driver.find_element_by_xpath("//select[@name='ids:list']"))
        select.select_by_value(title)
        self.driver.find_element_by_name("manage_delObjects:method").click()

    # Delete all experiments in the BCCVL
    def delete_all_experiments(self):
        self.driver.get(self.url+'/experiments/manage_main')
        self.driver.find_element_by_name('selectButton').click()
        self.driver.find_element_by_name('manage_delObjects:method').click()

    def generate_timestamp(self):
        return str(int(time.time()))

    # Note: This method will block if the element was not immediately visible.
    # The amount of time that this will block depends on the call to self.driver.implicitly_wait in this class'
    # setUp(self)
    def _check_exists_by_xpath(self, xpath):
        try:
            self.driver.find_element_by_xpath(xpath)
        except NoSuchElementException:
            return False
        return True