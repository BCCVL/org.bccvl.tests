from datasets_tab_page import DatasetsTabPage
from selenium.webdriver.support.ui import Select


class DatasetsUploadSpeciesDatasetPage(DatasetsTabPage):
    def upload_file(self, file):
        self.driver.find_element_by_css_selector("span.btn-file").click()
        self.driver.find_element_by_name("addspecies.widgets.file").send_keys(file)

    def enter_dataset_title(self, title):
        self.driver.find_element_by_name("addspecies.widgets.title").clear()
        self.driver.find_element_by_name("addspecies.widgets.title").send_keys(title)

    def enter_dataset_description(self, description):
        self.driver.find_element_by_name("addspecies.widgets.description").clear()
        self.driver.find_element_by_name("addspecies.widgets.description").send_keys(description)

    def select_dataset_genre(self, genre):
        # Index 0 is dataset genre, Index 1 is sepcies layer
        select = Select(self.driver.find_elements_by_css_selector("div.controls select")[0])
        select.select_by_visible_text(genre)

    def select_species_layer(self, layer):
        # Index 0 is dataset genre, Index 1 is sepcies layer
        select = Select(self.driver.find_elements_by_css_selector("div.controls select")[1])
        select.select_by_visible_text(layer)

    def enter_scientific_name(self, scientific_name):
        # Index 0 is scientific name, 1 is Taxon ID, 2 is Common Name
        self.driver.find_elements_by_css_selector(("div.controls input.input-block-level"))[0].clear()
        self.driver.find_elements_by_css_selector(("div.controls input.input-block-level"))[0].send_keys(scientific_name)

    def enter_taxon_id(self, taxon_id):
        self.driver.find_elements_by_css_selector(("div.controls input.input-block-level"))[1].clear()
        self.driver.find_elements_by_css_selector(("div.controls input.input-block-level"))[1].send_keys(taxon_id)

    def enter_common_name(self, common_name):
        self.driver.find_elements_by_css_selector(("div.controls input.input-block-level"))[2].clear()
        self.driver.find_elements_by_css_selector(("div.controls input.input-block-level"))[2].send_keys(common_name)

    # Can I name this method "sell_your_soul"?
    def agree_to_terms_and_conditions(self):
        self.driver.find_element_by_id("dataset-legal-checkbox").click()

    def submit(self):
        self.driver.find_element_by_name("addspecies.buttons.save").click()

    def cancel(self):
        self.driver.find_element_by_css_selector("#addspecies a.btn.btn-danger.bccvllinks-datasets").click()
