import unittest
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.select import Select
from selenium.common.exceptions import NoSuchElementException    
import tempfile
import os
import time
import sys
import hashlib

# Initial test cases to ensure that the BCCVL application is up and running.
class BCCVLTestCase(unittest.TestCase):

	def setUp(self):
		# acquire URL from env
		try:
			self.url = os.environ['URL']
		except:
			raise

		# Setup the Firefox Profile and webdriver
		self.driver = webdriver.Firefox()

		# Maximize the window
		self.driver.maximize_window()

		# Go to the bccvl homepage
		self.driver.get(self.url)

		# wait 10 sec
		self.driver.implicitly_wait(10)

		# any experiments that get creates are put into this list so 
		# that it can be deleted in tearDown
		self.experiments = []

	def check_exists_by_xpath(self, xpath):
		self.driver.refresh()
		try:
			self.driver.find_element_by_xpath(xpath)
		except NoSuchElementException:
			return False
		return True

	def deleteDataset(self, title):
		self.driver.get(self.url+'/datasets/manage_main')
		# TODO: write this method when doing datasets page tests

	def deleteExperiment(self, title):
		self.driver.get(self.url+'/experiments/manage_main')
		self.driver.refresh()
		try:
			element = WebDriverWait(self.driver, 30).until(lambda s: self.check_exists_by_xpath("//option[@value='" + title + "']"))
		finally:         	
			select = Select(self.driver.find_element_by_xpath("//select[@name='ids:list']"))
			select.select_by_value(title)
			self.driver.find_element_by_name("manage_delObjects:method").click()
			self.driver.get(self.url+'/experiments')

	def tearDown(self):
		# if experiments were created during this test then delete them
		if len(self.experiments) > 0:
			for experiment in self.experiments:
				self.deleteExperiment(experiment)
				self.experiments.remove(experiment)

		self.driver.quit()
		time.sleep(5)