from datasets_tab_page import DatasetsTabPage
from sharing_page import SharingPage
from homepage import Homepage

class DatasetsListPage(DatasetsTabPage):

    # NOTE: there is some danger here, as some datasets may not have visualise buttons,
    # essentially throwing out the index.
    def click_preview_dataset(self, name):
        names = self.driver.find_elements_by_css_selector("table.bccvl-datasetstable tr td p")
        names.reverse()
        # Figure out where it is in the list
        index = 0
        for checkName in names:
            if name.lower() in checkName.text.lower():
                break
            index = index + 1

        # There are two <P> tags per dataset, so just divide by 2 and floor to get the correct dataset
        # index.
        index = index / 2

        # get all visualise buttons
        controls = self.driver.find_elements_by_css_selector("i.icon-eye-open")

        # Get the index-th one.
        controls[index].click()

    def click_share_dataset(self, name):
        # TODO: This needs to be rewritten for the new UI
        assert True is False
        names = self.driver.find_elements_by_css_selector("table.bccvl-datasetstable tr td h1")

        # Figure out where it is in the list
        index = 0
        for checkName in names:
            if name.lower() in checkName.text.lower():
                break
            index = index + 1

        # Get the share button at that index
        controls = self.driver.find_elements_by_css_selector("table.bccvl-datasetstable tr td.bccvl-table-controls")

        # Get the index-th one.
        controls[index].find_element_by_css_selector("a.sharing-btn").click()

        return SharingPage(self.driver)

    # This method, given a name, returns a list of
    # DatasetObjects which name contains the parameter 'name'
    def get_dataset_list(self):
        dataset_list = []
        data = self.driver.find_elements_by_css_selector("table.bccvl-datasetstable tbody tr p")
        # take the first of each pair.
        names = []
        keep = True
        for data_entry in data:
            if keep is True:
                names.append(data_entry)
                keep = False
            else:
                keep = True

        for name in names:
            dataset_list.append(name.text.lower())
        return dataset_list

    # given an css-selector, sees if the dataset at a particular index, contains that element
    # used to find spinners and controls
    def _check_dataset_element_exists(self, element_name, index):
        row = self.driver.find_elements_by_css_selector("td.bccvl-table-controls")[index]
        results = row.find_elements_by_css_selector(element_name)
        if len(results) == 0:
            return False
        else:
            return True

    # Check if spinner is there for a particular dataset_list item
    def check_spinner(self, index):
        return self._check_dataset_element_exists("i.bccvl-small-spinner", index)

    # Check for controls (i.e. visualise, share etc buttons) next to a particular dataset list item
    def check_controls_exist(self, index):
        # using not because we look for the failure element, if it's there, we want to return false
        return not self._check_dataset_element_exists("td.bccvl-table-controls i.dataset-import-failed", index)

    def check_visualised_something(self):
        # Currently not implemented. iframes cannot be straight-forwardly looked in
        # with selenium
        pass
