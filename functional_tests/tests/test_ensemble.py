from experiment_test_base import ExperimentTestCase
from pages.homepage import Homepage
from test_utils import generate_timestamp
import os
from test_utils import *

class TestEnsemble(ExperimentTestCase):

    def test_ensemble_SDM(self):
        homepage = Homepage(self.driver)
        login_page = homepage.click_login()
        homepage = login_page.valid_login(self.username, self.password)
        experiment_page = homepage.click_experiments()
        new_sdm_page = experiment_page.click_new_sdm_experiment()

        experiment_name = "ann_" + generate_timestamp()

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

        experiments_page = experiment_view.click_experiments()
        new_ensemble_page = experiments_page.click_new_ensemble_experiment()
        new_ensemble_page.enter_experiment_name("Ensemble_" + generate_timestamp())
        new_ensemble_page.enter_experiment_description("A description goes here.")
        new_ensemble_page.click_source_data()
        new_ensemble_page.select_dataset_type("sdm")
        # Choose the SDM from before
        new_ensemble_page.select_source_experiment(experiment_name)
        # Choose a file from that SDM experiment:
        new_ensemble_page.select_available_file("proj_current_Phascolarctus.cinereus.tif")
        new_ensemble_page.click_run()
        experiment_results = new_ensemble_page.click_start_experiment()

        experiment_results.wait_for_experiment_to_complete()
        self.assertTrue(experiment_results.has_completed_successfully())

    # under construction
    # def test_ensemble_projection(self):
    #     homepage = Homepage(self.driver)
    #     login_page = homepage.click_login()
    #     homepage = login_page.valid_login(self.username, self.password)
    #     experiment_page = homepage.click_experiments()
    #
    #     # First create an SDM experiment to work with:
    #     # Copied from SDM experiment test
    #     new_sdm_page = experiment_page.click_new_sdm_experiment()
    #
    #     sdm_experiment_name = "ann_" + generate_timestamp()
    #
    #     new_sdm_page.enter_experiment_name(sdm_experiment_name)
    #     new_sdm_page.enter_experiment_description('Artificial Neural Network with Koala occurrences')
    #     new_sdm_page.select_configuration()
    #     new_sdm_page.select_sdm_algorithm('Artificial Neural Network')
    #     new_sdm_page.select_occurrences()
    #     new_sdm_page.select_occurrences_dataset('Koala - Mini occurrence dataset for Redland City')
    #     new_sdm_page.select_absences()
    #     new_sdm_page.select_absences_dataset('Koala - Mini absence dataset for Redland City')
    #     new_sdm_page.select_environment()
    #     new_sdm_page.select_current_climate_layers('Current climate layers for Redland City, 30" (~1km)')
    #     new_sdm_page.select_environmental_datasets('Current climate layers for Redland City, 30" (~1km)',
    #                                                'B14 - Precipitation of Driest Month')
    #     new_sdm_page.select_environmental_datasets('Current climate layers for Redland City, 30" (~1km)',
    #                                                'B15 - Precipitation Seasonality (Coefficient of Variation)')
    #     new_sdm_page.select_run()
    #     experiment_view = new_sdm_page.select_review_start_experiment()
    #
    #     # Wait until completion
    #     experiment_view.wait_for_experiment_to_complete()
    #     self.assertTrue(experiment_view.has_completed_successfully())
    #
    #     # Click on Experiments
    #     experiment_page = homepage.click_experiments()
    #     # New projection experiment
    #     new_projection_page = experiment_page.click_new_projection_experiment()
    #
    #     # generate a unique identifier for the projection experiment
    #     projection_experiment_name = "projection" + generate_timestamp()
    #     new_projection_page.enter_experiment_name(projection_experiment_name)
    #     new_projection_page.enter_experiment_description("This is a projection experiment")
    #
    #     # Choose the SDM experiment as the source
    #     new_projection_page.select_source_model_tab()
    #     new_projection_page.select_source_model(sdm_experiment_name)
    #
    #     # Just check the first tickbox for each column
    #     new_projection_page.select_projection()
    #     new_projection_page.select_year("2015")
    #     new_projection_page.select_emission_scenario("RCP3PD")
    #     new_projection_page.select_climate_models("CM2.0 - AOGCM")
    #
    #     # run the experiment
    #     new_projection_page.select_run()
    #     experiment_result_page = new_projection_page.select_run_experiment()
    #
    #     # Wait until completion
    #     experiment_result_page.wait_for_experiment_to_complete()
    #     self.assertTrue(experiment_result_page.has_completed_successfully())
    #
    #     # TODO: Ensemble
    #
    # def test_ensemble_biodiversity(self):
    #     homepage = Homepage(self.driver)
    #     login_page = homepage.click_login()
    #     homepage = login_page.valid_login(self.username, self.password)
    #     experiment_page = homepage.click_experiments()
    #
    #     # First create an SDM experiment to work with:
    #     new_sdm_page = experiment_page.click_new_sdm_experiment()
    #     sdm_experiment_name = create_sdm(self, new_sdm_page)
    #
    #     # Click on Experiments
    #     experiment_page = homepage.click_experiments()
    #
    #     # New projection experiment
    #     new_projection_page = experiment_page.click_new_projection_experiment()
    #     projection_experiment_name = create_projection(self, sdm_experiment_name, new_projection_page)
    #
    #     # Click on Experiments
    #     experiment_page = homepage.click_experiments()
    #
    #     # New biodiverse experiment
    #     new_biodiverse_page = experiment_page.click_new_biodiverse_experiment()
    #
    #     # generate a unique identifier for the projection experiment
    #     biodiverse_experiment_name = "biodiverse_" + generate_timestamp()
    #     new_biodiverse_page.enter_experiment_name(biodiverse_experiment_name)
    #     new_biodiverse_page.enter_experiment_description("This is a biodiverse experiment")
    #
    #     # select the earlier generated projection experiment
    #     new_biodiverse_page.select_source_projection_tab()
    #     new_biodiverse_page.select_projection_experiments(projection_experiment_name)
    #     new_biodiverse_page.select_species("Phascolarctus cinereus")
    #     new_biodiverse_page.select_years("2015")
    #     new_biodiverse_page.select_layers("proj_RCP3PD_gfdl-cm20_2015_Phascolarctus.cinereus.tif")
    #
    #     # select the configuration tab
    #     new_biodiverse_page.select_configuration_tab()
    #     new_biodiverse_page.select_threshold_value("CSI")
    #     new_biodiverse_page.select_cluster_size("10000")
    #
    #     # run the experiment
    #     new_biodiverse_page.select_run()
    #     experiment_result_page = new_biodiverse_page.select_run_experiment()
    #
    #     experiment_result_page.wait_for_experiment_to_complete()
    #     self.assertTrue(experiment_result_page.has_completed_successfully())
    #
    #     # TODO: Ensemble
    #
    # def test_ensemble_SDM_and_projection(self):
    #     homepage = Homepage(self.driver)
    #     login_page = homepage.click_login()
    #     homepage = login_page.valid_login(self.username, self.password)
    #     experiment_page = homepage.click_experiments()
    #
    #     # First create an SDM experiment to work with:
    #     # Copied from SDM experiment test
    #     new_sdm_page = experiment_page.click_new_sdm_experiment()
    #
    #     sdm_experiment_name = "ann_" + generate_timestamp()
    #
    #     new_sdm_page.enter_experiment_name(sdm_experiment_name)
    #     new_sdm_page.enter_experiment_description('Artificial Neural Network with Koala occurrences')
    #     new_sdm_page.select_configuration()
    #     new_sdm_page.select_sdm_algorithm('Artificial Neural Network')
    #     new_sdm_page.select_occurrences()
    #     new_sdm_page.select_occurrences_dataset('Koala - Mini occurrence dataset for Redland City')
    #     new_sdm_page.select_absences()
    #     new_sdm_page.select_absences_dataset('Koala - Mini absence dataset for Redland City')
    #     new_sdm_page.select_environment()
    #     new_sdm_page.select_current_climate_layers('Current climate layers for Redland City, 30" (~1km)')
    #     new_sdm_page.select_environmental_datasets('Current climate layers for Redland City, 30" (~1km)',
    #                                                'B14 - Precipitation of Driest Month')
    #     new_sdm_page.select_environmental_datasets('Current climate layers for Redland City, 30" (~1km)',
    #                                                'B15 - Precipitation Seasonality (Coefficient of Variation)')
    #     new_sdm_page.select_run()
    #     experiment_view = new_sdm_page.select_review_start_experiment()
    #
    #     # Wait until completion
    #     experiment_view.wait_for_experiment_to_complete()
    #     self.assertTrue(experiment_view.has_completed_successfully())
    #
    #     # Click on Experiments
    #     experiment_page = homepage.click_experiments()
    #     # New projection experiment
    #     new_projection_page = experiment_page.click_new_projection_experiment()
    #
    #     # generate a unique identifier for the projection experiment
    #     projection_experiment_name = "projection" + generate_timestamp()
    #     new_projection_page.enter_experiment_name(projection_experiment_name)
    #     new_projection_page.enter_experiment_description("This is a projection experiment")
    #
    #     # Choose the SDM experiment as the source
    #     new_projection_page.select_source_model_tab()
    #     new_projection_page.select_source_model(sdm_experiment_name)
    #
    #     # Just check the first tickbox for each column
    #     new_projection_page.select_projection()
    #     new_projection_page.select_year("2015")
    #     new_projection_page.select_emission_scenario("RCP3PD")
    #     new_projection_page.select_climate_models("CM2.0 - AOGCM")
    #
    #     # run the experiment
    #     new_projection_page.select_run()
    #     experiment_result_page = new_projection_page.select_run_experiment()
    #
    #     # Wait until completion
    #     experiment_result_page.wait_for_experiment_to_complete()
    #     self.assertTrue(experiment_result_page.has_completed_successfully())
    #
    #     # TODO: Ensemble
    #
    # def test_ensemble_projection_and_biodiversity(self):
    #     pass
    #
    #
    # def test_ensemble_projection_SDM_and_biodiversity(self):
    #     pass