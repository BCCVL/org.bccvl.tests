import unittest
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
import tempfile
import os
import time
import sys
import hashlib
from functional_tests.pages.bccvl_homepage import BCCVLHomepage

# Initial test cases to ensure that the BCCVL application is up and running.
class TestBCCVL(unittest.TestCase):

	def setUp(self):
		# acquire URL from env
		try:
			url = os.environ['URL']
		except:
			raise

		# Setup the Firefox Profile and webdriver
		self.driver = webdriver.Firefox()

		# Maximize the window
		self.driver.maximize_window()

		# Go to the bccvl homepage
		self.driver.get(url)

		# wait 10 sec
		self.driver.implicitly_wait(10)

	def test_app_login(self):
		bccvl_homepage = BCCVLHomepage(self.driver)
		self.assertEqual("BCCVL Home", bccvl_homepage.title)
		bccvl_homepage = bccvl_homepage.valid_login('admin', 'admin')
		self.assertEqual("BCCVL Home", bccvl_homepage.title)

	def test_datasets_page(self):
		bccvl_homepage = BCCVLHomepage(self.driver)
		bccvl_homepage = bccvl_homepage.valid_login('admin', 'admin')
		datasets_page = bccvl_homepage.click_datasets()
		self.assertEqual("BCCVL Datasets", datasets_page.title)

	def test_experiments_page(self):
		bccvl_homepage = BCCVLHomepage(self.driver)
		bccvl_homepage = bccvl_homepage.valid_login('admin', 'admin')
		experiments_page = bccvl_homepage.click_experiments()
		self.assertEqual("BCCVL Experiment List", experiments_page.title)

	def test_knowledgebase_page(self):
		bccvl_homepage = BCCVLHomepage(self.driver)
		bccvl_homepage = bccvl_homepage.valid_login('admin', 'admin')
		knowledge_base_page = bccvl_homepage.click_knowledge_base()
		self.assertEqual("BCCVL Knowledge Base", knowledge_base_page.title)


	def tearDown(self):
		self.driver.quit()