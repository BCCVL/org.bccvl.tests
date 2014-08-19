from experiment_test_base import ExperimentTestCase
from pages.homepage import Homepage
from test_utils import (create_sdm,
                        create_projection,
                        generate_timestamp)


# Test cases for SDM experiments - testing all algorithms
class TestBiodiverseExperiment(ExperimentTestCase):

    def test_basic_biodiverse(self):
        homepage = Homepage(self.driver)
        login_page = homepage.click_login()
        homepage = login_page.valid_login(self.username, self.password)
        experiment_page = homepage.click_experiments()

        # First create an SDM experiment to work with:
        new_sdm_page = experiment_page.click_new_sdm_experiment()
        sdm_experiment_name = create_sdm(self, new_sdm_page)

        # Click on Experiments
        experiment_page = homepage.click_experiments()

        # New projection experiment
        new_projection_page = experiment_page.click_new_projection_experiment()
        projection_experiment_name = create_projection(self, sdm_experiment_name, new_projection_page)

        # Click on Experiments
        experiment_page = homepage.click_experiments()

        # New biodiverse experiment
        new_biodiverse_page = experiment_page.click_new_biodiverse_experiment()

        # generate a unique identifier for the projection experiment
        biodiverse_experiment_name = "biodiverse_" + generate_timestamp()
        new_biodiverse_page.enter_experiment_name(biodiverse_experiment_name)
        new_biodiverse_page.enter_experiment_description("This is a biodiverse experiment")

        # select the earlier generated projection experiment
        new_biodiverse_page.select_source_projection_tab()
        new_biodiverse_page.select_projection_experiments(projection_experiment_name)
        new_biodiverse_page.select_species("Phascolarctus cinereus")
        new_biodiverse_page.select_years("2015")
        new_biodiverse_page.select_layers("proj_RCP3PD_gfdl-cm20_2015_Phascolarctus.cinereus.tif")

        # select the configuration tab
        new_biodiverse_page.select_configuration_tab()
        new_biodiverse_page.select_threshold_value("CSI")
        new_biodiverse_page.select_cluster_size("10000")

        # run the experiment
        new_biodiverse_page.select_run()
        experiment_result_page = new_biodiverse_page.select_run_experiment()

        experiment_result_page.wait_for_experiment_to_complete()
        self.assertTrue(experiment_result_page.has_completed_successfully())

        # Check results
        self.assertTrue(experiment_result_page.has_results_header(biodiverse_experiment_name))

        self.assertTrue(experiment_result_page.has_result_file('biodiverse_prefix_REDUNDANCY_SET1.tif'))
        self.assertTrue(experiment_result_page.has_result_file('biodiverse_prefix_REDUNDANCY_ALL.tif'))
        self.assertTrue(experiment_result_page.has_result_file('biodiverse_prefix_ENDW_RICHNESS.tif'))
        self.assertTrue(experiment_result_page.has_result_file('biodiverse_prefix_ENDW_SINGLE.tif'))
        self.assertTrue(experiment_result_page.has_result_file('biodiverse_prefix_ENDW_CWE.tif'))
        self.assertTrue(experiment_result_page.has_result_file('biodiverse_prefix_ENDW_WE.tif'))
        self.assertTrue(experiment_result_page.has_result_file('proj_SRESA1B_cccma-cgcm31_2015_Phascolarctus.cinereus.tif.tif'))
        self.assertTrue(experiment_result_page.has_result_file('biodiverse.plout'))
        self.assertTrue(experiment_result_page.has_result_file('biodiverse_prefix.bds'))
        self.assertTrue(experiment_result_page.has_result_file('pstats.json'))

        #Cleanup
        self.delete_experiment(sdm_experiment_name)
        self.delete_experiment(projection_experiment_name)
        self.delete_experiment(biodiverse_experiment_name)

    def test_biodiverse_2(self):
        homepage = Homepage(self.driver)
        login_page = homepage.click_login()
        homepage = login_page.valid_login(self.username, self.password)
        experiment_page = homepage.click_experiments()

        # First create an SDM experiment to work with:
        new_sdm_page = experiment_page.click_new_sdm_experiment()
        sdm_experiment_name = create_sdm(self, new_sdm_page)

        # Click on Experiments
        experiment_page = homepage.click_experiments()

        # New projection experiment
        new_projection_page = experiment_page.click_new_projection_experiment()
        projection_experiment_name = create_projection(self, sdm_experiment_name, new_projection_page)

        # Click on Experiments
        experiment_page = homepage.click_experiments()

        # New biodiverse experiment
        new_biodiverse_page = experiment_page.click_new_biodiverse_experiment()

        # generate a unique identifier for the projection experiment
        biodiverse_experiment_name = "biodiverse_" + generate_timestamp()
        new_biodiverse_page.enter_experiment_name(biodiverse_experiment_name)
        new_biodiverse_page.enter_experiment_description("This is a biodiverse experiment")

        # select the earlier generated projection experiment
        new_biodiverse_page.select_source_projection_tab()
        new_biodiverse_page.select_projection_experiments(projection_experiment_name)
        new_biodiverse_page.select_species("Phascolarctus cinereus")
        new_biodiverse_page.select_years("2015")
        new_biodiverse_page.select_layers("proj_RCP3PD_gfdl-cm20_2015_Phascolarctus.cinereus.tif")

        # select the configuration tab
        new_biodiverse_page.select_configuration_tab()
        new_biodiverse_page.select_threshold_value("CSI")
        new_biodiverse_page.select_cluster_size("20000")

        # run the experiment
        new_biodiverse_page.select_run()
        experiment_result_page = new_biodiverse_page.select_run_experiment()

        experiment_result_page.wait_for_experiment_to_complete()
        self.assertTrue(experiment_result_page.has_completed_successfully())

        # Check results
        self.assertTrue(experiment_result_page.has_results_header(biodiverse_experiment_name))

        self.assertTrue(experiment_result_page.has_result_file('biodiverse_prefix_REDUNDANCY_SET1.tif'))
        self.assertTrue(experiment_result_page.has_result_file('biodiverse_prefix_REDUNDANCY_ALL.tif'))
        self.assertTrue(experiment_result_page.has_result_file('biodiverse_prefix_ENDW_RICHNESS.tif'))
        self.assertTrue(experiment_result_page.has_result_file('biodiverse_prefix_ENDW_SINGLE.tif'))
        self.assertTrue(experiment_result_page.has_result_file('biodiverse_prefix_ENDW_CWE.tif'))
        self.assertTrue(experiment_result_page.has_result_file('biodiverse_prefix_ENDW_WE.tif'))
        self.assertTrue(experiment_result_page.has_result_file('proj_SRESA1B_cccma-cgcm31_2015_Phascolarctus.cinereus.tif'))
        self.assertTrue(experiment_result_page.has_result_file('biodiverse.plout'))
        self.assertTrue(experiment_result_page.has_result_file('biodiverse_prefix.bds'))
        self.assertTrue(experiment_result_page.has_result_file('pstats.json'))

        #Cleanup
        self.delete_experiment(sdm_experiment_name)
        self.delete_experiment(projection_experiment_name)
        self.delete_experiment(biodiverse_experiment_name)

    def test_biodiverse_3(self):
        homepage = Homepage(self.driver)
        login_page = homepage.click_login()
        homepage = login_page.valid_login(self.username, self.password)
        experiment_page = homepage.click_experiments()

        # First create an SDM experiment to work with:
        new_sdm_page = experiment_page.click_new_sdm_experiment()
        sdm_experiment_name = create_sdm(self, new_sdm_page)

        # Click on Experiments
        experiment_page = homepage.click_experiments()

        # New projection experiment
        new_projection_page = experiment_page.click_new_projection_experiment()
        projection_experiment_name = create_projection(self, sdm_experiment_name, new_projection_page)

        # Click on Experiments
        experiment_page = homepage.click_experiments()

        # New biodiverse experiment
        new_biodiverse_page = experiment_page.click_new_biodiverse_experiment()

        # generate a unique identifier for the projection experiment
        biodiverse_experiment_name = "biodiverse_" + generate_timestamp()
        new_biodiverse_page.enter_experiment_name(biodiverse_experiment_name)
        new_biodiverse_page.enter_experiment_description("This is a biodiverse experiment")

        # select the earlier generated projection experiment
        new_biodiverse_page.select_source_projection_tab()
        new_biodiverse_page.select_projection_experiments(projection_experiment_name)
        new_biodiverse_page.select_species("Phascolarctus cinereus")
        new_biodiverse_page.select_years("2015")
        new_biodiverse_page.select_layers("proj_RCP3PD_gfdl-cm20_2015_Phascolarctus.cinereus.tif")

        # select the configuration tab
        new_biodiverse_page.select_configuration_tab()
        new_biodiverse_page.select_threshold_value("KAPPA")
        new_biodiverse_page.select_cluster_size("20000")

        # run the experiment
        new_biodiverse_page.select_run()
        experiment_result_page = new_biodiverse_page.select_run_experiment()

        experiment_result_page.wait_for_experiment_to_complete()
        self.assertTrue(experiment_result_page.has_completed_successfully())

        # Check results
        self.assertTrue(experiment_result_page.has_results_header(biodiverse_experiment_name))

        self.assertTrue(experiment_result_page.has_result_file('biodiverse_prefix_REDUNDANCY_SET1.tif'))
        self.assertTrue(experiment_result_page.has_result_file('biodiverse_prefix_REDUNDANCY_ALL.tif'))
        self.assertTrue(experiment_result_page.has_result_file('biodiverse_prefix_ENDW_RICHNESS.tif'))
        self.assertTrue(experiment_result_page.has_result_file('biodiverse_prefix_ENDW_SINGLE.tif'))
        self.assertTrue(experiment_result_page.has_result_file('biodiverse_prefix_ENDW_CWE.tif'))
        self.assertTrue(experiment_result_page.has_result_file('biodiverse_prefix_ENDW_WE.tif'))
        self.assertTrue(experiment_result_page.has_result_file('proj_SRESA1B_cccma-cgcm31_2015_Phascolarctus.cinereus.tif'))
        self.assertTrue(experiment_result_page.has_result_file('biodiverse.plout'))
        self.assertTrue(experiment_result_page.has_result_file('biodiverse_prefix.bds'))
        self.assertTrue(experiment_result_page.has_result_file('pstats.json'))

        #Cleanup
        self.delete_experiment(sdm_experiment_name)
        self.delete_experiment(projection_experiment_name)
        self.delete_experiment(biodiverse_experiment_name)
