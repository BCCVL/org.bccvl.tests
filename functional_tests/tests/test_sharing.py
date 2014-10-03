from experiment_test_base import ExperimentTestCase
from pages.homepage import Homepage
from test_utils import generate_timestamp


# These tests test sharing experiments and datasets between users
# It only uses built-in authentication since tests cannot use AAF to log in
# ***********************************************************************
# These tests assume a built-in authentication test user has been created
# with:
# Username: testuser
# Password: Pass.123
# ***********************************************************************

class TestSharing(ExperimentTestCase):

    # Create an experiment, and share it.
    def test_sharing_experiment(self):
        homepage = Homepage(self.driver)
        login_page = homepage.click_login()
        homepage = login_page.valid_login(self.username, self.password)
        experiment_page = homepage.click_experiments()
        new_sdm_page = experiment_page.click_new_sdm_experiment()
        experiment_name = "sharing_test_" + generate_timestamp()
        new_sdm_page.enter_experiment_name(experiment_name)
        new_sdm_page.enter_experiment_description('Artificial Neural Network with Koala occurrences')
        new_sdm_page.select_configuration()
        new_sdm_page.select_sdm_algorithm('Artificial Neural Network')
        new_sdm_page.select_occurrences()
        new_sdm_page.select_occurrences_dataset('Koala - Mini occurrence dataset for Redland City')
        new_sdm_page.select_absences()
        new_sdm_page.select_absences_dataset('Koala - Mini absence dataset for Redland City')
        new_sdm_page.select_environment()
        new_sdm_page.select_current_climate_layers('Current climate layers for Redland City, 30" (~1km)')
        new_sdm_page.select_environmental_datasets('Current climate layers for Redland City, 30" (~1km)',
                                                   'B14 - Precipitation of Driest Month')
        new_sdm_page.select_run()
        experiment_view = new_sdm_page.select_review_start_experiment()

        # Wait until completion
        experiment_view.wait_for_experiment_to_complete()
        self.assertTrue(experiment_view.has_completed_successfully())


        # Navigate back to experiment list
        experiment_page = experiment_view.click_experiments()

        # Check it's in the list
        experiments = experiment_page.get_experiment_list()
        self.assertTrue(experiment_name.lower() in experiments[0], "Could not find SDM experment")

        # Share it
        sharing_page = experiment_page.click_share_experiment(experiment_name)
        sharing_page.check_can_view("Logged-in users")
        sharing_page.agree_to_terms_and_conditions()
        sharing_page.select_share_save()

        # Log out
        logged_out_homepage = homepage.click_logout()
        login_page = logged_out_homepage.click_login()
        login_page.valid_login("testuser", "Pass.123")
        experiment_page = homepage.click_experiments()

        experiments = experiment_page.get_experiment_list()
        self.assertTrue(experiment_name in experiments[0])

        # Log out so we can delete it
        logged_out_homepage = homepage.click_logout("test user")
        login_page = logged_out_homepage.click_login()
        login_page.valid_login(self.username, self.password)

        # Cleanup
        self.delete_experiment(experiment_name)

    # import a dataset from ALA share it.
    def test_sharing_dataset(self):
        homepage = Homepage(self.driver)
        login_page = homepage.click_login()
        homepage = login_page.valid_login(self.username, self.password)

        datasets_page = homepage.click_datasets()

        datasets_discover_page = datasets_page.select_dataset_discover()
        datasets_discover_page.enter_find_species("pig")
        datasets_discover_page.click_species()

        # We get redirected back to datasets list page here
        datasets_page = datasets_discover_page.click_download_species()

        # Try generate the list of names
        name_list = datasets_page.get_dataset_list()

        # The first one should be pig
        # Make sure we can find pig in the first one'
        self.assertNotEqual(name_list[0].find("pig"), -1, "Could not find pig dataset")

        # Wait until the first one doesn't have a spinner anymore
        datasets_page.wait_while_spinner(0)

        # Refresh the page
        datasets_page.driver.refresh()

        # See if the first one still has controls
        self.assertFalse(datasets_page.check_spinner(0), "Spinner still found when it shouldn't have been!")
        self.assertTrue(datasets_page.check_controls_exist(0), "Dataset controls not found for this dataset entry")

        # click on share.
        sharing_page = datasets_page.click_share_dataset("pig")
        sharing_page.check_can_view("Logged-in users")
        sharing_page.agree_to_terms_and_conditions()
        datasets_page = sharing_page.select_share_save()
        logged_in_homepage = datasets_page.click_homepage()

        # Log out
        logged_out_homepage = logged_in_homepage.click_logout("admin")
        login_page = logged_out_homepage.click_login()
        homepage = login_page.valid_login("testuser", "Pass.123")
        datasets_page = homepage.click_datasets()

        datasets = datasets_page.get_dataset_list()
        self.assertTrue("pig" in datasets[0].lower())

        # ************************************#
        # At this point, we log out of testuser, back into admin
        # to add a different ALA set to make sure the test
        # passed not because of a coincidence
        # ************************************#
        logged_out_homepage = homepage.click_logout("test user")
        login_page = logged_out_homepage.click_login()
        homepage = login_page.valid_login(self.username, self.password)
        datasets_page = homepage.click_datasets()
        datasets_discover_page = datasets_page.select_dataset_discover()
        datasets_discover_page.enter_find_species("platypus")
        datasets_discover_page.click_species()

        # We get redirected back to datasets list page here
        datasets_page = datasets_discover_page.click_download_species()

        # Try generate the list of names
        name_list = datasets_page.get_dataset_list()

        # The first one should be pig
        # Make sure we can find pig in the first one'
        self.assertNotEqual(name_list[0].find("platypus"), -1, "Could not find platypus dataset")

        # Wait until the first one doesn't have a spinner anymore
        datasets_page.wait_while_spinner(0)

        # Refresh the page
        datasets_page.driver.refresh()

        # See if the first one still has controls
        self.assertFalse(datasets_page.check_spinner(0), "Spinner still found when it shouldn't have been!")
        self.assertTrue(datasets_page.check_controls_exist(0), "Dataset controls not found for this dataset entry")

        # click on share.
        sharing_page = datasets_page.click_share_dataset("platypus")
        sharing_page.check_can_view("Logged-in users")
        sharing_page.agree_to_terms_and_conditions()
        sharing_page.select_share_save()

        # Log out
        logged_out_homepage = homepage.click_logout()
        login_page = logged_out_homepage.click_login()
        homepage = login_page.valid_login("testuser", "Pass.123")
        datasets_page = homepage.click_datasets()

        datasets = datasets_page.get_dataset_list()
        self.assertTrue("platypus" in datasets[0].lower())

    # import a dataset from ALA share it.
    # check you can see it from other accounts
    # unshare it
    # check you can no longer see it.
    def test_unsharing_dataset(self):
        homepage = Homepage(self.driver)
        login_page = homepage.click_login()
        homepage = login_page.valid_login(self.username, self.password)

        datasets_page = homepage.click_datasets()

        datasets_discover_page = datasets_page.select_dataset_discover()
        datasets_discover_page.enter_find_species("pig")
        datasets_discover_page.click_species()

        # We get redirected back to datasets list page here
        datasets_page = datasets_discover_page.click_download_species()

        # Try generate the list of names
        name_list = datasets_page.get_dataset_list()

        # The first one should be pig
        # Make sure we can find pig in the first one'
        self.assertNotEqual(name_list[0].find("pig"), -1, "Could not find pig dataset")

        # Wait until the first one doesn't have a spinner anymore
        datasets_page.wait_while_spinner(0)

        # Refresh the page
        datasets_page.driver.refresh()

        # See if the first one still has controls
        self.assertFalse(datasets_page.check_spinner(0), "Spinner still found when it shouldn't have been!")
        self.assertTrue(datasets_page.check_controls_exist(0), "Dataset controls not found for this dataset entry")

        # click on share.
        sharing_page = datasets_page.click_share_dataset("pig")
        sharing_page.check_can_view("Logged-in users")
        sharing_page.agree_to_terms_and_conditions()
        sharing_page.select_share_save()

        # Do this again with a different dataset, so that when we unshare one, we know
        # which one should be at the top.
        datasets_discover_page = datasets_page.select_dataset_discover()
        datasets_discover_page.enter_find_species("rat")
        datasets_discover_page.click_species()

        # We get redirected back to datasets list page here
        datasets_page = datasets_discover_page.click_download_species()

        # Try generate the list of names
        name_list = datasets_page.get_dataset_list()

        # The first one should be pig
        # Make sure we can find pig in the first one'
        self.assertNotEqual(name_list[0].find("rat"), -1, "Could not find rat dataset")

        # Wait until the first one doesn't have a spinner anymore
        datasets_page.wait_while_spinner(0)

        # Refresh the page
        datasets_page.driver.refresh()

        # See if the first one still has controls
        self.assertFalse(datasets_page.check_spinner(0), "Spinner still found when it shouldn't have been!")
        self.assertTrue(datasets_page.check_controls_exist(0), "Dataset controls not found for this dataset entry")

        # click on share.
        sharing_page = datasets_page.click_share_dataset("rat")
        sharing_page.check_can_view("Logged-in users")
        sharing_page.agree_to_terms_and_conditions()
        datasets_list = sharing_page.select_share_save()
        logged_in_homepage = datasets_list.click_homepage()

        # Log out
        logged_out_homepage = logged_in_homepage.click_logout()
        login_page = logged_out_homepage.click_login()
        homepage = login_page.valid_login("testuser", "Pass.123")
        datasets_page = homepage.click_datasets()

        datasets = datasets_page.get_dataset_list()
        self.assertNotEqual("rat" in datasets[0].lower(), -1, "Wrong dataset in dataset list")

        # ************************************#
        # At this point, we log back into admin to unshare pig
        # ************************************#
        logged_out_homepage = homepage.click_logout("test user")
        login_page = logged_out_homepage.click_login()
        homepage = login_page.valid_login(self.username, self.password)
        datasets_page = homepage.click_datasets()

        # Toggle rat. (i.e. unshare)
        sharing_page = datasets_page.click_share_dataset("rat")
        sharing_page.check_can_view("Logged-in users")
        sharing_page.agree_to_terms_and_conditions()
        datasets_list = sharing_page.select_share_save()
        logged_in_homepage = datasets_list.click_homepage()

        logged_out_homepage = logged_in_homepage.click_logout()
        login_page = logged_out_homepage.click_login()
        homepage = login_page.valid_login("testuser", "Pass.123")
        datasets_page = homepage.click_datasets()
        datasets = datasets_page.get_dataset_list()

        self.assertNotEqual("pig" in datasets[0].lower(), -1, "Wrong dataset in the dataset list")
