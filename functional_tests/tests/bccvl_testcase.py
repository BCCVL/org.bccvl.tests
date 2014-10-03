import unittest
import os
from pyvirtualdisplay import Display
from selenium import webdriver


# Base Test Cases used to test BCCVL
class BCCVLTestCase(unittest.TestCase):

    def setUp(self):
        # acquire URL, username and password from environment variables, or use default values for dev env.
        self.username = os.getenv('BCCVL_TEST_USERNAME', 'admin')
        self.password = os.getenv('BCCVL_TEST_PASSWORD', 'admin')
        self.url = os.getenv('BCCVL_TEST_URL', 'https://192.168.100.200/')

        # The amount of time selenium will potentially wait in searching for elements. This is blocking.
        implicit_wait = int(os.getenv('BCCVL_TEST_IMPLICIT_WAIT', '15'))

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
        #self.driver.maximize_window()
        self.driver.set_window_size(1200, 800)

        # Go to the bccvl homepage
        self.driver.get(self.url)

    def tearDown(self):
        if self.display:
            self.display.stop()
        self.driver.quit()
