from datasets_tab_page import DatasetsTabPage
from datasets_list_page import DatasetsListPage


class DatasetsUploadSpeciesTraitPage(DatasetsTabPage):
    def upload_file(self, file):
        self.driver.find_element_by_css_selector("#addtraits .btn.btn-file").click()
        self.driver.find_element_by_name("addtraits.widgets.file").send_keys(file)


    def enter_dataset_title(self, title):
        self.driver.find_element_by_name("addtraits.widgets.title").clear()
        self.driver.find_element_by_name("addtraits.widgets.title").send_keys(title)

    def enter_dataset_description(self, description):
        self.driver.find_element_by_name("addtraits.widgets.description").clear()
        self.driver.find_element_by_name("addtraits.widgets.description").send_keys(description)

    # Can I name this method "sell_your_soul"?
    def agree_to_terms_and_conditions(self):
        self.driver.find_element_by_id("traits-legal-checkbox").click()

    def submit(self):
        self.driver.find_element_by_id("addtraits-buttons-save").click()
        new_datasets_list_page = DatasetsListPage(self.driver)
        return new_datasets_list_page

    def cancel(self):
        self.driver.find_element_by_css_selector("#addtraits .btn.btn-danger.bccvllinks-datasets").click()
