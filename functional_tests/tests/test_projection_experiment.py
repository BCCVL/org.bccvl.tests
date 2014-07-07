from experiment_test_base import ExperimentTestCase
from pages.homepage import Homepage
from test_utils import generate_timestamp


# Test cases for SDM experiments - testing all algorithms
class TestProjectionExperiment(ExperimentTestCase):

    def test_basic_projection(self):
        homepage = Homepage(self.driver)
        login_page = homepage.click_login()
        homepage = login_page.valid_login(self.username, self.password)
        experiment_page = homepage.click_experiments()

        # First create an SDM experiment to work with:
        # Copied from SDM experiment test
        new_sdm_page = experiment_page.click_new_sdm_experiment()

        sdm_experiment_name = "ann_" + generate_timestamp()

        new_sdm_page.enter_experiment_name(sdm_experiment_name)
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
        new_sdm_page.select_environmental_datasets('Current climate layers for Redland City, 30" (~1km)',
                                                   'B15 - Precipitation Seasonality (Coefficient of Variation)')
        new_sdm_page.select_run()
        experiment_view = new_sdm_page.select_review_start_experiment()

        # Wait until completion
        experiment_view.wait_for_experiment_to_complete(500)
        self.assertTrue(experiment_view.has_completed_successfully())

        # Click on Experiments
        experiment_page = homepage.click_experiments()
        # New projection experiment
        new_projection_page = experiment_page.click_new_projection_experiment()

        # generate a unique identifier for the projection experiment
        projection_experiment_name = "projection" + generate_timestamp()
        new_projection_page.enter_experiment_name(projection_experiment_name)
        new_projection_page.enter_experiment_description("This is a projection experiment")

        # Choose the SDM experiment as the source
        new_projection_page.select_source_model_tab()
        new_projection_page.select_source_model(sdm_experiment_name)

        # Just check the first tickbox for each column
        new_projection_page.select_projection()
        new_projection_page.select_year("2015")
        new_projection_page.select_emission_scenario("RCP3PD")
        new_projection_page.select_climate_models("CM2.0 - AOGCM")

        # run the experiment
        new_projection_page.select_run()
        experiment_result_page = new_projection_page.select_run_experiment()

        # Wait until completion
        experiment_result_page.wait_for_experiment_to_complete(500)
        self.assertTrue(experiment_result_page.has_completed_successfully())

        # Check results
        self.assertTrue(experiment_result_page.has_results_header(projection_experiment_name))
        self.assertEqual(5, experiment_result_page.get_num_output_files())
        self.assertTrue(experiment_result_page.has_result_file('proj_RCP3PD_gfdl-cm20_2015_ClampingMask.tif'))
        self.assertTrue(experiment_result_page.has_result_file('proj_RCP3PD_gfdl-cm20_2015_Phascolarctus.cinereus.tif'))
        self.assertTrue(experiment_result_page.has_result_file('projection.Rout'))
        self.assertTrue(experiment_result_page.has_result_file('Phascolarctus.cinereus.RCP3PD_gfdl-cm20_2015.projection.out'))
        self.assertTrue(experiment_result_page.has_result_file('pstats.json'))

        # Cleanup
        self.delete_experiment(sdm_experiment_name)
        self.delete_experiment(projection_experiment_name)