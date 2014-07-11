from datasets_tab_page import DatasetsTabPage
from selenium.webdriver.support.ui import Select

class DatasetsUploadEnvironmentalLayerPage(DatasetsTabPage):

    def upload_file(self, file):
        self.driver.find_element_by_css_selector("#addlayer .btn.btn-file").click()
        self.driver.find_element_by_name("addlayer.widgets.file").clear()
        self.driver.find_element_by_name("addlayer.widgets.file").send_keys(file)

    def enter_dataset_title(self,title):
        self.driver.find_element_by_name("addlayer.widgets.title").clear()
        self.driver.find_element_by_name("addlayer.widgets.title").send_keys(title)

    def enter_dataset_description(self,description):
        self.driver.find_element_by_name("addlayer.widgets.description").clear()
        self.driver.find_element_by_name("addlayer.widgets.description").send_keys(description)

    def select_dataset_genre(self,genre):
        select = Select(self.driver.find_element_by_id("addlayer.widgets.datagenre:list"))
        select.select_by_visible_text(genre)

    def select_type(self,type):
        select = Select(self.driver.find_element_by_id("addlayer.widgets.datatype:list"))
        select.select_by_visible_text(type)

    def select_resolution(self,resolution):
        select = Select(self.driver.find_element_by_id("addlayer.widgets.resolution:list"))
        select.select_by_visible_text(resolution)

    def enter_other_resolution(self,resolution):
        self.driver.find_element_by_name("addlayer.widgets.resolutiono").clear()
        self.driver.find_element_by_css_selector("addlayer.widgets.resolutiono").send_keys(resolution)

    def enter_start_date(self,day,month,year,description):
        self.driver.find_element_by_name("addlayer.widgets.temporal.start-day").clear()
        self.driver.find_element_by_css_selector("addlayer.widgets.temporal.start-day").send_keys(day)
        self.driver.find_element_by_name("addlayer.widgets.temporal.start-month").clear()
        self.driver.find_element_by_css_selector("addlayer.widgets.temporal.start-month").send_keys(month)
        self.driver.find_element_by_name("addlayer.widgets.temporal.start-year").clear()
        self.driver.find_element_by_css_selector("addlayer.widgets.temporal.start-year").send_keys(year)
        self.driver.find_element_by_name("addlayer.widgets.temporal.starttext").clear()
        self.driver.find_element_by_css_selector("addlayer.widgets.temporal.starttext").send_keys(description)

    def enter_end_date(self,day,month,year,description):
        self.driver.find_element_by_name("addlayer.widgets.temporal.end-day").clear()
        self.driver.find_element_by_css_selector("addlayer.widgets.temporal.end-day").send_keys(day)
        self.driver.find_element_by_name("addlayer.widgets.temporal.end-month").clear()
        self.driver.find_element_by_css_selector("addlayer.widgets.temporal.end-month").send_keys(month)
        self.driver.find_element_by_name("addlayer.widgets.temporal.end-year").clear()
        self.driver.find_element_by_css_selector("addlayer.widgets.temporal.end-year").send_keys(year)
        self.driver.find_element_by_name("addlayer.widgets.temporal.endtext").clear()
        self.driver.find_element_by_css_selector("addlayer.widgets.temporal.endtext").send_keys(description)

    def select_emission_scenario(self,emission_scenario):
        select = Select(self.driver.find_element_by_id("addlayer.widgets.emissionscenario:list"))
        select.select_by_visible_text(emission_scenario)

    def select_global_climate_model(self,global_climate_model):
        select = Select(self.driver.find_element_by_id("addlayer.widgets.gcm:list"))
        select.select_by_visible_text(global_climate_model)

    # Can I name this method "sell_your_soul"?
    def agree_to_terms_and_conditions(self):
        self.driver.find_element_by_id("dataset-legal-checkbox").click()

    def submit(self):
        self.driver.find_element_by_name("addlayer.buttons.save").click()

    def cancel(self):
        self.driver.find_element_by_css_selector("#addlayer a.btn.btn-danger.bccvllinks-datasets").click()
