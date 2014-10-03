from datasets_tab_page import DatasetsTabPage
from selenium.webdriver.support.ui import Select


class DatasetsUploadSpeciesDatasetPage(DatasetsTabPage):
    def upload_file(self, file):
        self.driver.find_element_by_css_selector("#speciesoccurrence span.btn-file").click()
        self.driver.find_element_by_name("speciesoccurrence.widgets.file").send_keys(file)

    def enter_dataset_title(self, title):
        self.driver.find_element_by_name("speciesoccurrence.widgets.title").clear()
        self.driver.find_element_by_name("speciesoccurrence.widgets.title").send_keys(title)

    def enter_dataset_description(self, description):
        self.driver.find_element_by_name("speciesoccurrence.widgets.description").clear()
        self.driver.find_element_by_name("speciesoccurrence.widgets.description").send_keys(description)

    def enter_scientific_name(self, scientific_name):
        # Index 0 is scientific name, 1 is Taxon ID, 2 is Common Name
        input = self.driver.find_element_by_name("speciesoccurrence.widgets.scientificname")
        input.clear()
        input.send_keys(scientific_name)

    def enter_taxon_id(self, taxon_id):
        input = self.driver.find_element_by_name("speciesoccurrence.widgets.taxonID")
        input.clear()
        input.send_keys(taxon_id)

    def enter_common_name(self, common_name):
        input = self.driver.find_element_by_name("speciesoccurrence.widgets.vernacularName")
        input.clear()
        input.send_keys(common_name)

    # Can I name this method "sell_your_soul"?
    def agree_to_terms_and_conditions(self):
        self.driver.find_element_by_id("dataset-legal-checkbox").click()

    def submit(self):
        self.driver.find_element_by_name("speciesoccurrence.buttons.save").click()

    def cancel(self):
        self.driver.find_element_by_css_selector("#speciesoccurrence a.btn.btn-danger").click()
