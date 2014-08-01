from base_page import BasePage


class SharingPage(BasePage):

    # On the share page you can tick "can view" for certain people
    # Currently this only works for ADMIN ACCOUNTS
    # i.e. accounts that have all 5 options in share.
    def check_can_view(self, name):
        options = self.driver.find_elements_by_css_selector("tbody#user-group-sharing-settings td")
        # options contains:
        # - name
        # - can add tickbox
        # - can edit tickbox
        # - can review tickbox
        # - can view tickbox
        assert len(options) % 5 == 0

        index = 0
        while index < len(options) / 5:
            # Names are index 0, 5, 10 etc. hence 5*index
            if name.lower() in options[(5*index)].text.lower():
                # We've found it.
                # +4 to reach the view tickbox.
                options[(5 * index) + 4].find_element_by_css_selector("input").click()
                break

            # Not found.
            index = index + 1

    def select_share_save(self):
        self.driver.find_element_by_id('sharing-save-button').click()
        from datasets_list_page import DatasetsListPage
        return DatasetsListPage(self.driver)

    def select_share_cancel(self):
        self.driver.find_element_by_css_selector('input.btn-danger').click()

    def agree_to_terms_and_conditions(self):
        self.driver.find_element_by_id("legal-checkbox").click()
