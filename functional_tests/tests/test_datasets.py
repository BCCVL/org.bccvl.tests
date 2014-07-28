from bccvl_testcase import BCCVLTestCase
from pages.homepage import Homepage
import time


class TestDatasets(BCCVLTestCase):

    def test_import_ALA(self):
        homepage = Homepage(self.driver)
        login_page = homepage.click_login()
        homepage = login_page.valid_login(self.username, self.password)
        datasets_page = homepage.click_datasets()

        # Get the number of datasets
        name_list = datasets_page.get_dataset_list()
        number_of_datasets = len(name_list)

        # import koala
        datasets_discover_page = datasets_page.select_dataset_discover()
        datasets_discover_page.enter_find_species("koala")
        datasets_discover_page.click_species()

        # We get redirected back to datasets list page here
        datasets_page = datasets_discover_page.click_download_species()

        # Try generate the list of names
        name_list = datasets_page.get_dataset_list()

        # The first one should be koala
        # Make sure we can find koala in the first one'
        self.assertNotEqual(name_list[0].find("koala"), -1, "Could not find koala dataset")

        # Check we have one more dataset than before.
        if number_of_datasets == 100: # The page only shows 100, so check it's 100 still
            self.assertEqual(len(name_list), 100, "Mismatch number of datasets")
        else:
            self.assertEqual(len(name_list), number_of_datasets + 1, "Mismatch number of datasets")

        # Wait until the first one doesn't have a spinner anymore
        end_time = time.time() + (5 * 60)
        while time.time() <= end_time:
            if not datasets_page.check_spinner(0):
                break
            time.sleep(5)
        if datasets_page.check_spinner(0):
            self.fail("Time out wating for ALA import")

        # Refresh the page
        datasets_page.driver.refresh()

        # See if the first one still has controls
        self.assertFalse(datasets_page.check_spinner(0), "Spinner still found when it shouldn't have been!")
        self.assertTrue(datasets_page.check_controls_exist(0), "Dataset controls not found for this dataset entry")

    # TODO: Wait until visualiser stops using iframes or implement a workaround for
    # looking inside the iframe.
    # def test_visualise_dataset(self):
    #     homepage = Homepage(self.driver)
    #     login_page = homepage.click_login()
    #     homepage = login_page.valid_login(self.username, self.password)
    #     datasets_page = homepage.click_datasets()
    #
    #     # Get the number of datasets
    #     name_list = datasets_page.get_dataset_list()
    #     number_of_datasets = len(name_list)
    #
    #     # import koala
    #     datasets_discover_page = datasets_page.select_dataset_discover()
    #     datasets_discover_page.enter_find_species("koala")
    #     datasets_discover_page.click_species()
    #
    #     # We get redirected back to datasets list page here
    #     datasets_page = datasets_discover_page.click_download_species()
    #
    #     # Try generate the list of names
    #     name_list = datasets_page.get_dataset_list()
    #
    #     # The first one should be koala
    #     # Make sure we can find koala in the first one'
    #     self.assertNotEqual(name_list[0].find("koala"), -1, "Could not find koala dataset")
    #
    #     # Wait until the first one doesn't have a spinner anymore
    #     end_time = time.time() + (5 * 60)
    #     while time.time() <= end_time:
    #         if not datasets_page.check_spinner(0):
    #             break
    #         time.sleep(5)
    #     if datasets_page.check_spinner(0):
    #         self.fail("Time out wating for ALA import")
    #
    #     # Refresh the page
    #     datasets_page.driver.refresh()
    #
    #     datasets_page.click_preview_dataset("Strongylium koala")
    #     end_time = time.time() + 10
    #     while time.time() < end_time:
    #         visualised = datasets_page.check_visualised_something()
    #         if visualised is True:
    #             break
    #
    #     self.assertTrue(visualised)
    #

