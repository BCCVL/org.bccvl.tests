from __future__ import absolute_import
from .datasets_tab_page import DatasetsTabPage
from .sharing_page import SharingPage
from selenium.webdriver.support.ui import WebDriverWait
from .base_page import retry_if_stale


class DatasetsListPage(DatasetsTabPage):

    # NOTE: there is some danger here, as some datasets may not have visualise buttons,
    # essentially throwing out the index.
    def click_preview_dataset(self, name):
        names = self.driver.find_elements_by_css_selector("div.datasets-list-entry p.lead")
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
        names = self.driver.find_elements_by_css_selector("td.bccvl-table-label p:first-child")

        # Figure out where it is in the list
        index = 0
        for checkName in names:
            if name.lower() in checkName.text.lower():
                break
            index = index + 1

        # Get the share button at that index
        # get the index-th list entry
        entry = self.driver.find_elements_by_css_selector('div.datasets-list-entry')[index]
        # open the preview pane
        entry.find_element_by_css_selector('a.dropdown-button').click()
        # click sharing button
        entry.find_element_by_css_selector("a.sharing-btn").click()

        return SharingPage(self.driver)

    # This method, given a name, returns a list of
    # DatasetObjects which name contains the parameter 'name'
    def get_dataset_list(self):
        dataset_list = []
        data = self.driver.find_elements_by_css_selector("div.datasets-list-entry p.lead")

        for name in data:
            dataset_list.append(name.text.lower())
        return dataset_list

    # given an css-selector, sees if the dataset at a particular index, contains that element
    # used to find spinners and controls
    def _check_dataset_element_exists(self, element_name, index):
        row = self.driver.find_elements_by_css_selector("div.datasets-list-entry div.dataset-list-dropdown")[index]
        # TODO: we may get a stale reference exception here if the list entry updates
        #       before the next line. (esp. when we wait until the import spinner
        #       disappears. At the moment this is handled in the check_spinner method.)
        results = row.find_elements_by_css_selector(element_name)
        if len(results) == 0:
            return False
        else:
            return True

    # Check if spinner is there for a particular dataset_list item
    @retry_if_stale
    def check_spinner(self, index):
        return self._check_dataset_element_exists("i.bccvl-small-spinner", index)

    def wait_while_spinner(self, index, timeout=300):
        '''
        Wait up to 5 minues for spinner to disappear.
        '''
        WebDriverWait(self.driver, timeout).until(lambda s: not self.check_spinner(index))


    # Check for controls (i.e. visualise, share etc buttons) next to a particular dataset list item
    def check_controls_exist(self, index):
        # using not because we look for the failure element, if it's there, we want to return false
        return not self._check_dataset_element_exists("td.bccvl-table-controls i.dataset-import-failed", index)

    def check_visualised_something(self):
        # Currently not implemented. iframes cannot be straight-forwardly looked in
        # with selenium
        assert False is True
        pass

    def click_homepage(self):
        self.driver.find_element_by_css_selector('a.bccvllinks-home').click()
        from .logged_in_homepage import LoggedInHomepage
        return LoggedInHomepage(self.driver)
