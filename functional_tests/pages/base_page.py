from selenium import webdriver
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait # available since 2.4.0
from selenium.webdriver.support import expected_conditions as EC # available since 2.26.0
from selenium.webdriver.support.ui import WebDriverWait

class BasePage():
    def __init__(self, driver):
        self.driver = driver
        self.title = driver.title

    def check_text_displayed(self, string):
        return string in self.driver.find_element_by_tag_name("body").text

	# This is for AJAX refreshed data - this doesn't refresh the page
    def wait_till_text_displayed(self, string, seconds):
      try:
         print "about to look for element"
         element = WebDriverWait(self.driver, seconds).until(lambda s: self.check_text_exists(string))
      
	  finally:
          print 'found string'

    def check_text_exists(self, text):
        self.driver.refresh()
        element = self.driver.find_element_by_tag_name("body")
        return text in element.text

