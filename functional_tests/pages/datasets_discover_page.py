from datasets_tab_page import DatasetsTabPage
from datasets_list_page import DatasetsListPage


class DatasetsDiscoverPage(DatasetsTabPage):

    def enter_find_species(self,name):
        self.driver.find_element_by_css_selector("div#searchOccurrence input").clear()
        self.driver.find_element_by_css_selector("div#searchOccurrence input").send_keys(name)

    def click_species(self):
        # Select the first match in the list
        self.driver.find_element_by_css_selector("div#searchOccurrence li").click()

    def click_download_species(self):
        # Click download
        self.driver.find_element_by_css_selector("i.icon-download-alt").click()
        new_datasets_list_page = DatasetsListPage(self.driver)
        return new_datasets_list_page
