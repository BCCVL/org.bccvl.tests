from bccvl_testcase import BCCVLTestCase
from pages.homepage import Homepage
from test_utils import generate_timestamp
import os


class TestDatasetUpload(BCCVLTestCase):

    def test_upload_species_dataset(self):
        homepage = Homepage(self.driver)
        login_page = homepage.click_login()
        homepage = login_page.valid_login(self.username, self.password)
        datasets_page = homepage.click_datasets()
        upload_page = datasets_page.select_dataset_upload()
        upload_page.upload_file(os.getcwd() + "test.csv")
        upload_page.enter_dataset_title("species_dataset" + generate_timestamp())
        upload_page.enter_dataset_description("bleh")
        upload_page.select_dataset_genre("Abundance")
        upload_page.select_species_layer("Presence")
        upload_page.enter_scientific_name("bleh")
        upload_page.enter_taxon_id("bluh")
        upload_page.enter_common_name("bloop")
        upload_page.agree_to_terms_and_conditions()
        upload_page.submit()

    def test_upload_environmental_layer(self):
        homepage = Homepage(self.driver)
        login_page = homepage.click_login()
        homepage = login_page.valid_login(self.username, self.password)
        datasets_page = homepage.click_datasets()
        upload_page = datasets_page.select_dataset_upload()
        upload_page = upload_page.select_dataset_type("Environmental Layer")
        upload_page.upload_file(os.getcwd() + "test.csv")
        upload_page.enter_dataset_title("environmental_layer" + generate_timestamp())
        upload_page.enter_dataset_description("blurp")
        upload_page.select_dataset_genre("Environmental")
        upload_page.select_type("continuous")
        upload_page.select_resolution("30\" (~1km)")
        upload_page.enter_start_date(1, 1, 2000, "wow")
        upload_page.enter_end_date(2, 2, 2001, "weo")
        upload_page.select_emission_scenario("RCP6")
        upload_page.select_global_climate_model("Coupled Global Climate Model (CGCM3)")
        upload_page.agree_to_terms_and_conditions()
        upload_page.submit()

    def test_upload_species_trait(self):
        homepage = Homepage(self.driver)
        login_page = homepage.click_login()
        homepage = login_page.valid_login(self.username, self.password)
        datasets_page = homepage.click_datasets()
        upload_page = datasets_page.select_dataset_upload()
        upload_page = upload_page.select_dataset_type("Species Trait")
        upload_page.upload_file(os.getcwd() + "test.csv")
        dataset_title = "species_trait_test_" + generate_timestamp()
        upload_page.enter_dataset_title(dataset_title)
        upload_page.enter_dataset_description("Description")

        upload_page.agree_to_terms_and_conditions()
        datasets_page = upload_page.submit()

        # Retry while datasets page hasn't loaded.
        datasets = datasets_page.get_dataset_list()
        while (len(datasets) == 0):
            datasets = datasets_page.get_dataset_list()

        self.assertTrue(dataset_title in datasets)
