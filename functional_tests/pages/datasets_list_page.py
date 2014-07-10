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

    # given an css-selector, sees if the dataset at a particular index, contains that element
    # used to find spinners and controls
    def _check_dataset_element_exists(self,element_name,index):
        tables = self.driver.find_elements_by_css_selector("table.bccvl-datasetstable tbody tr")
        currentIndex = 0
        for table in tables:
            if currentIndex == index:
                objects = self.driver.find_elements_by_css_selector(element_name)
                if len(objects) != 0:
                    return True
                else:
                    return False
            else:
                index += 1


    # Check if spinner is there for a particular dataset_list item
    def check_spinner(self,index):
        return self._check_dataset_element_exists("i.bccvl-small-spinner", index)

    # Check for controls (i.e. visualise, share etc buttons) next to a particular dataset list item
    def check_controls_exist(self,index):
        # using not because we look for the failure element, if it's there, we want to return false
        return not self._check_dataset_element_exists("td.bccvl-table-controls i.dataset-import-failed", index)
