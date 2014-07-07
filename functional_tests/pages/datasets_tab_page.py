from base_page import BasePage


# DatasetsTabPage represents everything above and including
# the three navigation tabs common to dataset list, dataset discover
# and dataset upload
class DatasetsTabPage(BasePage):

    def select_dataset_list(self):
        self.driver.find_element_by_css_selector("li#tab-datasetslisting a").click()
        from datasets_list_page import DatasetsListPage
        new_dataset_list_page = DatasetsListPage(self.driver)
        return new_dataset_list_page

    def select_dataset_discover(self):
        self.driver.find_element_by_css_selector("li#tab-datasetsimport a").click()
        from datasets_discover_page import DatasetsDiscoverPage
        new_dataset_discover_page = DatasetsDiscoverPage(self.driver)
        return new_dataset_discover_page

    def select_dataset_upload(self):
        self.driver.find_element_by_css_selector("li#tab-datasetsupload a").click()
        from datasets_upload_page import DatasetsUploadPage
        new_dataset_upload_page = DatasetsUploadPage(self.driver)
        return new_dataset_upload_page

