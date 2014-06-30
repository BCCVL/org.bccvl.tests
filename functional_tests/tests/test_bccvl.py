from bccvl_testcase import BCCVLTestCase
from functional_tests.pages.homepage import Homepage

# Initial test cases to ensure that the BCCVL application is up and running.
class TestBCCVL(BCCVLTestCase):

	def test_app_login(self):
		homepage = Homepage(self.driver)
		self.assertEqual("BCCVL Home", homepage.title)
		login_page = homepage.click_login()
		homepage = login_page.valid_login('admin', 'admin')
		self.assertEqual("BCCVL Home", homepage.title)

	def test_app_logout(self):
		homepage = Homepage(self.driver)
		login_page = homepage.click_login()
		homepage = login_page.valid_login('admin', 'admin')
		logged_out_homepage = homepage.click_logout()
		self.assertEqual("BCCVL Home", logged_out_homepage.title)		

	def test_datasets_page(self):
		homepage = Homepage(self.driver)
		login_page = homepage.click_login()
		homepage = login_page.valid_login('admin', 'admin')
		datasets_page = homepage.click_datasets()
		self.assertEqual("BCCVL Datasets", datasets_page.title)

	def test_experiments_page(self):
		homepage = Homepage(self.driver)
		login_page = homepage.click_login()
		homepage = login_page.valid_login('admin', 'admin')
		experiments_page = homepage.click_experiments()
		self.assertEqual("BCCVL Experiment List", experiments_page.title)

	def test_knowledgebase_page(self):
		homepage = Homepage(self.driver)
		login_page = homepage.click_login()
		homepage = login_page.valid_login('admin', 'admin')
		knowledge_base_page = homepage.click_knowledge_base()
		self.assertEqual("BCCVL Knowledge Base", knowledge_base_page.title)