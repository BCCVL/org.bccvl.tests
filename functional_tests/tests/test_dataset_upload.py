from bccvl_testcase import BCCVLTestCase
from pages.homepage import Homepage
import os

class TestDatasetUpload(BCCVLTestCase):
    # def test_upload_species_dataset(self):
    #     # Comment out until we get better test file
    #     # homepage = Homepage(self.driver)
    #     # login_page = homepage.click_login()
    #     # homepage = login_page.valid_login(self.username, self.password)
    #     # datasets_page = homepage.click_datasets()
    #     # upload_page = datasets_page.select_dataset_upload()
    #     # upload_page.upload_file(os.getcwd() + "test.csv")
    #     # upload_page.enter_dataset_title()
    #     # upload_page.enter_dataset_description()
    #     # upload_page.select_dataset_genre()
    #     # upload_page.select_species_layer()
    #     # upload_page.enter_scientific_name()
    #     # upload_page.enter_taxon_id()
    #     # upload_page.enter_common_name()
    #     # upload_page.agree_to_terms_and_conditions()
    #     # upload_page.submit()
    #     pass
    #
    # def test_upload_environmental_layer(self):
    #     pass

    def test_upload_species_trait(self):
        homepage = Homepage(self.driver)
        login_page = homepage.click_login()
        homepage = login_page.valid_login(self.username, self.password)
        datasets_page = homepage.click_datasets()
        upload_page = datasets_page.select_dataset_upload()
        upload_page = upload_page.select_dataset_type("Species Trait")
        upload_page.upload_file(os.getcwd() + "test.csv")
        dataset_title = "Species Trait Test"
        upload_page.enter_dataset_title(dataset_title)
        upload_page.enter_dataset_description("Description")
        # upload_page.agree_to_terms_and_conditions() <--- This is currently not working
        # upload_page.submit()
        # datasets = datasets_page.get_dataset_list()
        # self.assertTrue(dataset_title in datasets)
        pass