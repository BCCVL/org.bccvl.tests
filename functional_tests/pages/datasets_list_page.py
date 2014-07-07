from datasets_tab_page import DatasetsTabPage

class DatasetsListPage(DatasetsTabPage):

    def click_preview_dataset(self):
        pass

    # This method, given a name, returns a list of
    # DatasetObjects which name contains the parameter 'name'
    def get_dataset_list(self):
        dataset_list = []
        names = self.driver.find_elements_by_css_selector("table.bccvl-datasetstable tbody tr h1")
        for name in names:
            dataset_list.append(name.text.lower())


        return dataset_list





