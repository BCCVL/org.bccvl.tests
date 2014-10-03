from base_page import BasePage
from selenium.webdriver.support.select import Select


# DatasetsTabPage represents everything above and including
# the three navigation tabs common to dataset list, dataset discover
# and dataset upload
class DatasetsTabPage(BasePage):

    def select_dataset_list(self):
        self.driver.find_element_by_css_selector("li.tab-datasetslisting a").click()
        from datasets_list_page import DatasetsListPage
        new_dataset_list_page = DatasetsListPage(self.driver)
        return new_dataset_list_page

    def select_dataset_discover(self):
        self.driver.find_element_by_css_selector("li.tab-datasetsimport a").click()
        from datasets_discover_page import DatasetsDiscoverPage
        new_dataset_discover_page = DatasetsDiscoverPage(self.driver)
        return new_dataset_discover_page

    def select_dataset_upload(self):
        self.driver.find_element_by_css_selector("li.tab-datasetsupload a").click()
        from datasets_upload_species_dataset_page import DatasetsUploadSpeciesDatasetPage
        new_dataset_upload_page = DatasetsUploadSpeciesDatasetPage(self.driver)
        return new_dataset_upload_page

    def select_dataset_type(self, type):
        select = Select(self.driver.find_element_by_id("upload-dataset-type"))

        if type == "Species Dataset":
            select.select_by_value("species")
            from datasets_upload_species_dataset_page import DatasetsUploadSpeciesDatasetPage
            new_dataset_upload_page = DatasetsUploadSpeciesDatasetPage(self.driver)
        elif type == "Environmental Layer":
            select.select_by_value("environmental-layer")
            from datasets_upload_environmental_layer_page import DatasetsUploadEnvironmentalLayerPage
            new_dataset_upload_page = DatasetsUploadEnvironmentalLayerPage(self.driver)
        else:
            select.select_by_value("species-trait")
            from datasets_upload_species_trait_page import DatasetsUploadSpeciesTraitPage
            new_dataset_upload_page = DatasetsUploadSpeciesTraitPage(self.driver)
        return new_dataset_upload_page
