from experiment_test_base import ExperimentTestCase
from pages.homepage import Homepage
from test_utils import generate_timestamp


# Test cases for SDM experiments - testing all algorithms
class TestSDMExperiment(ExperimentTestCase):

    def test_ann_1km(self):
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
        new_sdm_page.select_environmental_datasets('Current climate layers for Redland City, 30" (~1km)',
                                                   'B15 - Precipitation Seasonality (Coefficient of Variation)')
        new_sdm_page.select_run()
        experiment_view = new_sdm_page.select_review_start_experiment()

        # Wait until completion
        experiment_view.wait_for_experiment_to_complete(500)
        self.assertTrue(experiment_view.has_completed_successfully())

        # Check results
        self.assertTrue(experiment_view.has_results_header(experiment_name))
        self.assertEqual(9, experiment_view.get_num_output_files())
        self.assertTrue(experiment_view.has_result_file('mean_response_curves.png'))
        self.assertTrue(experiment_view.has_result_file('mean_response_curves.png'))
        self.assertTrue(experiment_view.has_result_file('pROC.png'))
        self.assertTrue(experiment_view.has_result_file('ann.Rout'))
        self.assertTrue(experiment_view.has_result_file('combined.modelEvaluation.csv'))
        self.assertTrue(experiment_view.has_result_file('biomod2.modelEvaluation.csv'))
        self.assertTrue(experiment_view.has_result_file('model.object.RData.zip'))
        self.assertTrue(experiment_view.has_result_file('pstats.json'))
        self.assertTrue(experiment_view.has_result_file('proj_current_ClampingMask.tif'))

        # Cleanup
        self.delete_experiment(experiment_name)

    def test_ann_5km(self):
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
        new_sdm_page.select_current_climate_layers('Current climate layers for Australia, 2.5arcmin (~5km)')
        new_sdm_page.select_environmental_datasets('Current climate layers for Australia, 2.5arcmin (~5km)',
                                                   'B14 - Precipitation of Driest Month')
        new_sdm_page.select_environmental_datasets('Current climate layers for Australia, 2.5arcmin (~5km)',
                                                   'B15 - Precipitation Seasonality (Coefficient of Variation)')
        new_sdm_page.select_run()
        experiment_view = new_sdm_page.select_review_start_experiment()

        # Wait until completion
        experiment_view.wait_for_experiment_to_complete(500)
        self.assertTrue(experiment_view.has_completed_successfully())

        # Check results
        self.assertTrue(experiment_view.has_results_header(experiment_name))
        self.assertEqual(9, experiment_view.get_num_output_files())
        self.assertTrue(experiment_view.has_result_file('mean_response_curves.png'))
        self.assertTrue(experiment_view.has_result_file('mean_response_curves.png'))
        self.assertTrue(experiment_view.has_result_file('pROC.png'))
        self.assertTrue(experiment_view.has_result_file('ann.Rout'))
        self.assertTrue(experiment_view.has_result_file('combined.modelEvaluation.csv'))
        self.assertTrue(experiment_view.has_result_file('biomod2.modelEvaluation.csv'))
        self.assertTrue(experiment_view.has_result_file('model.object.RData.zip'))
        self.assertTrue(experiment_view.has_result_file('pstats.json'))
        self.assertTrue(experiment_view.has_result_file('proj_current_ClampingMask.tif'))

        # Cleanup
        self.delete_experiment(experiment_name)

    def test_bioclim_1km(self):
        homepage = Homepage(self.driver)
        login_page = homepage.click_login()
        homepage = login_page.valid_login(self.username, self.password)
        experiment_page = homepage.click_experiments()
        new_sdm_page = experiment_page.click_new_sdm_experiment()

        experiment_name = "bioclim_" + generate_timestamp()

        new_sdm_page.enter_experiment_name(experiment_name)
        new_sdm_page.enter_experiment_description('Bioclim with Koala occurrences')
        new_sdm_page.select_configuration()
        new_sdm_page.select_sdm_algorithm('Bioclim')
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

        self.assertTrue(experiment_view.has_results_header(experiment_name))
        self.assertEqual(13, experiment_view.get_num_output_files())
        self.assertTrue(experiment_view.has_result_file('dismo.eval.object.RData'))
        self.assertTrue(experiment_view.has_result_file('AUC.png'))
        self.assertTrue(experiment_view.has_result_file('results.html'))
        self.assertTrue(experiment_view.has_result_file('combined.modelEvaluation.csv'))
        self.assertTrue(experiment_view.has_result_file('maxent_like_VariableImportance.csv'))
        self.assertTrue(experiment_view.has_result_file('biomod2_like_VariableImportance.csv'))
        self.assertTrue(experiment_view.has_result_file('Phascolarctus.cinereus.model.object.RData'))
        self.assertTrue(experiment_view.has_result_file('bioclim.Rout'))
        self.assertTrue(experiment_view.has_result_file('bioclim_15_response.png'))
        self.assertTrue(experiment_view.has_result_file('bioclim_14_response.png'))
        self.assertTrue(experiment_view.has_result_file('results.html.zip'))
        self.assertTrue(experiment_view.has_result_file('pstats.json'))
        self.assertTrue(experiment_view.has_result_file('proj_current_Phascolarctus.cinereus.tif'))

        # Cleanup
        self.delete_experiment(experiment_name)

    def test_bioclim_5km(self):
        homepage = Homepage(self.driver)
        login_page = homepage.click_login()
        homepage = login_page.valid_login(self.username, self.password)
        experiment_page = homepage.click_experiments()
        new_sdm_page = experiment_page.click_new_sdm_experiment()

        experiment_name = "bioclim_" + generate_timestamp()

        new_sdm_page.enter_experiment_name(experiment_name)
        new_sdm_page.enter_experiment_description('Bioclim with Koala occurrences')
        new_sdm_page.select_configuration()
        new_sdm_page.select_sdm_algorithm('Bioclim')
        new_sdm_page.select_occurrences()
        new_sdm_page.select_occurrences_dataset('Koala - Mini occurrence dataset for Redland City')
        new_sdm_page.select_absences()
        new_sdm_page.select_absences_dataset('Koala - Mini absence dataset for Redland City')
        new_sdm_page.select_environment()
        new_sdm_page.select_current_climate_layers('Current climate layers for Australia, 2.5arcmin (~5km)')
        new_sdm_page.select_environmental_datasets('Current climate layers for Australia, 2.5arcmin (~5km)',
                                                   'B14 - Precipitation of Driest Month')
        new_sdm_page.select_environmental_datasets('Current climate layers for Australia, 2.5arcmin (~5km)',
                                                   'B15 - Precipitation Seasonality (Coefficient of Variation)')
        new_sdm_page.select_run()
        experiment_view = new_sdm_page.select_review_start_experiment()

        # Wait until completion
        experiment_view.wait_for_experiment_to_complete(500)
        self.assertTrue(experiment_view.has_completed_successfully())

        self.assertTrue(experiment_view.has_results_header(experiment_name))
        self.assertEqual(13, experiment_view.get_num_output_files())
        self.assertTrue(experiment_view.has_result_file('dismo.eval.object.RData'))
        self.assertTrue(experiment_view.has_result_file('AUC.png'))
        self.assertTrue(experiment_view.has_result_file('results.html'))
        self.assertTrue(experiment_view.has_result_file('combined.modelEvaluation.csv'))
        self.assertTrue(experiment_view.has_result_file('maxent_like_VariableImportance.csv'))
        self.assertTrue(experiment_view.has_result_file('biomod2_like_VariableImportance.csv'))
        self.assertTrue(experiment_view.has_result_file('Phascolarctus.cinereus.model.object.RData'))
        self.assertTrue(experiment_view.has_result_file('bioclim.Rout'))
        self.assertTrue(experiment_view.has_result_file('bioclim_15_response.png'))
        self.assertTrue(experiment_view.has_result_file('bioclim_14_response.png'))
        self.assertTrue(experiment_view.has_result_file('results.html.zip'))
        self.assertTrue(experiment_view.has_result_file('pstats.json'))
        self.assertTrue(experiment_view.has_result_file('proj_current_Phascolarctus.cinereus.tif'))

        # Cleanup
        self.delete_experiment(experiment_name)

    def test_brt_1km(self):
        homepage = Homepage(self.driver)
        login_page = homepage.click_login()
        homepage = login_page.valid_login(self.username, self.password)
        experiment_page = homepage.click_experiments()
        new_sdm_page = experiment_page.click_new_sdm_experiment()

        experiment_name = "brt_" + generate_timestamp()

        new_sdm_page.enter_experiment_name(experiment_name)
        new_sdm_page.enter_experiment_description('Boosted Regression Experiment with Koala occurrences')
        new_sdm_page.select_configuration()
        new_sdm_page.select_sdm_algorithm('Boosted Regression Tree')
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

        # Check results
        self.assertTrue(experiment_view.has_results_header(experiment_name))
        self.assertEqual(13, experiment_view.get_num_output_files())
        self.assertTrue(experiment_view.has_result_file('dismo.eval.object.RData'))
        self.assertTrue(experiment_view.has_result_file('AUC.png'))
        self.assertTrue(experiment_view.has_result_file('results.html'))
        self.assertTrue(experiment_view.has_result_file('combined.modelEvaluation.csv'))
        self.assertTrue(experiment_view.has_result_file('maxent_like_VariableImportance.csv'))
        self.assertTrue(experiment_view.has_result_file('biomod2_like_VariableImportance.csv'))
        self.assertTrue(experiment_view.has_result_file('Phascolarctus.cinereus.model.object.RData'))
        self.assertTrue(experiment_view.has_result_file('brt.Rout'))
        self.assertTrue(experiment_view.has_result_file('bioclim_15_response.png'))
        self.assertTrue(experiment_view.has_result_file('bioclim_14_response.png'))
        self.assertTrue(experiment_view.has_result_file('results.html.zip'))
        self.assertTrue(experiment_view.has_result_file('pstats.json'))
        self.assertTrue(experiment_view.has_result_file('proj_current_Phascolarctus.cinereus.tif'))

        # Cleanup
        self.delete_experiment(experiment_name)

    def test_brt_5km(self):
        homepage = Homepage(self.driver)
        login_page = homepage.click_login()
        homepage = login_page.valid_login(self.username, self.password)
        experiment_page = homepage.click_experiments()
        new_sdm_page = experiment_page.click_new_sdm_experiment()

        experiment_name = "brt_" + generate_timestamp()

        new_sdm_page.enter_experiment_name(experiment_name)
        new_sdm_page.enter_experiment_description('Boosted Regression Experiment with Koala occurrences')
        new_sdm_page.select_configuration()
        new_sdm_page.select_sdm_algorithm('Boosted Regression Tree')
        new_sdm_page.select_occurrences()
        new_sdm_page.select_occurrences_dataset('Koala - Mini occurrence dataset for Redland City')
        new_sdm_page.select_absences()
        new_sdm_page.select_absences_dataset('Koala - Mini absence dataset for Redland City')
        new_sdm_page.select_environment()
        new_sdm_page.select_current_climate_layers('Current climate layers for Australia, 2.5arcmin (~5km)')
        new_sdm_page.select_environmental_datasets('Current climate layers for Australia, 2.5arcmin (~5km)',
                                                   'B14 - Precipitation of Driest Month')
        new_sdm_page.select_environmental_datasets('Current climate layers for Australia, 2.5arcmin (~5km)',
                                                   'B15 - Precipitation Seasonality (Coefficient of Variation)')
        new_sdm_page.select_run()
        experiment_view = new_sdm_page.select_review_start_experiment()

        # Wait until completion
        experiment_view.wait_for_experiment_to_complete(500)
        self.assertTrue(experiment_view.has_completed_successfully())

        # Check results
        self.assertTrue(experiment_view.has_results_header(experiment_name))
        self.assertEqual(13, experiment_view.get_num_output_files())
        self.assertTrue(experiment_view.has_result_file('dismo.eval.object.RData'))
        self.assertTrue(experiment_view.has_result_file('AUC.png'))
        self.assertTrue(experiment_view.has_result_file('results.html'))
        self.assertTrue(experiment_view.has_result_file('combined.modelEvaluation.csv'))
        self.assertTrue(experiment_view.has_result_file('maxent_like_VariableImportance.csv'))
        self.assertTrue(experiment_view.has_result_file('biomod2_like_VariableImportance.csv'))
        self.assertTrue(experiment_view.has_result_file('Phascolarctus.cinereus.model.object.RData'))
        self.assertTrue(experiment_view.has_result_file('brt.Rout'))
        self.assertTrue(experiment_view.has_result_file('bioclim_15_response.png'))
        self.assertTrue(experiment_view.has_result_file('bioclim_14_response.png'))
        self.assertTrue(experiment_view.has_result_file('results.html.zip'))
        self.assertTrue(experiment_view.has_result_file('pstats.json'))
        self.assertTrue(experiment_view.has_result_file('proj_current_Phascolarctus.cinereus.tif'))

        # Cleanup
        self.delete_experiment(experiment_name)

    def test_circles_1km(self):
        homepage = Homepage(self.driver)
        login_page = homepage.click_login()
        homepage = login_page.valid_login(self.username, self.password)
        experiment_page = homepage.click_experiments()
        new_sdm_page = experiment_page.click_new_sdm_experiment()

        experiment_name = "circles_" + generate_timestamp()

        new_sdm_page.enter_experiment_name(experiment_name)
        new_sdm_page.enter_experiment_description('Circles Experiment with Koala occurrences')
        new_sdm_page.select_configuration()
        new_sdm_page.select_sdm_algorithm('Circles')
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

        self.assertTrue(experiment_view.has_results_header(experiment_name))
        self.assertEqual(15, experiment_view.get_num_output_files())
        self.assertTrue(experiment_view.has_result_file('dismo.eval.object.RData'))
        self.assertTrue(experiment_view.has_result_file('AUC.png'))
        self.assertTrue(experiment_view.has_result_file('results.html'))
        self.assertTrue(experiment_view.has_result_file('combined.modelEvaluation.csv'))
        self.assertTrue(experiment_view.has_result_file('maxent_like_VariableImportance.csv'))
        self.assertTrue(experiment_view.has_result_file('biomod2_like_VariableImportance.csv'))
        self.assertTrue(experiment_view.has_result_file('Phascolarctus.cinereus.model.object.RData'))
        self.assertTrue(experiment_view.has_result_file('circles.Rout'))
        self.assertTrue(experiment_view.has_result_file('lon_response.png'))
        self.assertTrue(experiment_view.has_result_file('bioclim_15_response.png'))
        self.assertTrue(experiment_view.has_result_file('lat_response.png'))
        self.assertTrue(experiment_view.has_result_file('bioclim_14_response.png'))
        self.assertTrue(experiment_view.has_result_file('results.html.zip'))
        self.assertTrue(experiment_view.has_result_file('proj_current_Phascolarctus.cinereus.tif'))
        self.assertTrue(experiment_view.has_result_file('pstats.json'))

        # Cleanup
        self.delete_experiment(experiment_name)

    def test_circles_5km(self):
        homepage = Homepage(self.driver)
        login_page = homepage.click_login()
        homepage = login_page.valid_login(self.username, self.password)
        experiment_page = homepage.click_experiments()
        new_sdm_page = experiment_page.click_new_sdm_experiment()

        experiment_name = "circles_" + generate_timestamp()

        new_sdm_page.enter_experiment_name(experiment_name)
        new_sdm_page.enter_experiment_description('Circles Experiment with Koala occurrences')
        new_sdm_page.select_configuration()
        new_sdm_page.select_sdm_algorithm('Circles')
        new_sdm_page.select_occurrences()
        new_sdm_page.select_occurrences_dataset('Koala - Mini occurrence dataset for Redland City')
        new_sdm_page.select_absences()
        new_sdm_page.select_absences_dataset('Koala - Mini absence dataset for Redland City')
        new_sdm_page.select_environment()
        new_sdm_page.select_current_climate_layers('Current climate layers for Australia, 2.5arcmin (~5km)')
        new_sdm_page.select_environmental_datasets('Current climate layers for Australia, 2.5arcmin (~5km)',
                                                   'B14 - Precipitation of Driest Month')
        new_sdm_page.select_environmental_datasets('Current climate layers for Australia, 2.5arcmin (~5km)',
                                                   'B15 - Precipitation Seasonality (Coefficient of Variation)')
        new_sdm_page.select_run()
        experiment_view = new_sdm_page.select_review_start_experiment()

        # Wait until completion
        experiment_view.wait_for_experiment_to_complete(500)
        self.assertTrue(experiment_view.has_completed_successfully())

        self.assertTrue(experiment_view.has_results_header(experiment_name))
        self.assertEqual(15, experiment_view.get_num_output_files())
        self.assertTrue(experiment_view.has_result_file('dismo.eval.object.RData'))
        self.assertTrue(experiment_view.has_result_file('AUC.png'))
        self.assertTrue(experiment_view.has_result_file('results.html'))
        self.assertTrue(experiment_view.has_result_file('combined.modelEvaluation.csv'))
        self.assertTrue(experiment_view.has_result_file('maxent_like_VariableImportance.csv'))
        self.assertTrue(experiment_view.has_result_file('biomod2_like_VariableImportance.csv'))
        self.assertTrue(experiment_view.has_result_file('Phascolarctus.cinereus.model.object.RData'))
        self.assertTrue(experiment_view.has_result_file('circles.Rout'))
        self.assertTrue(experiment_view.has_result_file('lon_response.png'))
        self.assertTrue(experiment_view.has_result_file('bioclim_15_response.png'))
        self.assertTrue(experiment_view.has_result_file('lat_response.png'))
        self.assertTrue(experiment_view.has_result_file('bioclim_14_response.png'))
        self.assertTrue(experiment_view.has_result_file('results.html.zip'))
        self.assertTrue(experiment_view.has_result_file('proj_current_Phascolarctus.cinereus.tif'))
        self.assertTrue(experiment_view.has_result_file('pstats.json'))

        # Cleanup
        self.delete_experiment(experiment_name)

    def test_classification_tree_1km(self):
        homepage = Homepage(self.driver)
        login_page = homepage.click_login()
        homepage = login_page.valid_login(self.username, self.password)
        experiment_page = homepage.click_experiments()
        new_sdm_page = experiment_page.click_new_sdm_experiment()

        experiment_name = "ct_" + generate_timestamp()

        new_sdm_page.enter_experiment_name(experiment_name)
        new_sdm_page.enter_experiment_description('Classification Tree Experiment with Koala occurrences')
        new_sdm_page.select_configuration()
        new_sdm_page.select_sdm_algorithm('Classification Tree')
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

        self.assertTrue(experiment_view.has_results_header(experiment_name))
        self.assertEqual(9, experiment_view.get_num_output_files())
        self.assertTrue(experiment_view.has_result_file('mean_response_curves.png'))
        self.assertTrue(experiment_view.has_result_file('pROC.png'))
        self.assertTrue(experiment_view.has_result_file('cta.Rout'))
        self.assertTrue(experiment_view.has_result_file('combined.modelEvaluation.csv'))
        self.assertTrue(experiment_view.has_result_file('biomod2.modelEvaluation.csv'))
        self.assertTrue(experiment_view.has_result_file('model.object.RData.zip'))
        self.assertTrue(experiment_view.has_result_file('proj_current_Phascolarctus.cinereus.tif'))
        self.assertTrue(experiment_view.has_result_file('proj_current_ClampingMask.tif'))
        self.assertTrue(experiment_view.has_result_file('pstats.json'))

        # Cleanup
        self.delete_experiment(experiment_name)

    def test_classification_tree_5km(self):
        homepage = Homepage(self.driver)
        login_page = homepage.click_login()
        homepage = login_page.valid_login(self.username, self.password)
        experiment_page = homepage.click_experiments()
        new_sdm_page = experiment_page.click_new_sdm_experiment()

        experiment_name = "ct_" + generate_timestamp()

        new_sdm_page.enter_experiment_name(experiment_name)
        new_sdm_page.enter_experiment_description('Classification Tree Experiment with Koala occurrences')
        new_sdm_page.select_configuration()
        new_sdm_page.select_sdm_algorithm('Classification Tree')
        new_sdm_page.select_occurrences()
        new_sdm_page.select_occurrences_dataset('Koala - Mini occurrence dataset for Redland City')
        new_sdm_page.select_absences()
        new_sdm_page.select_absences_dataset('Koala - Mini absence dataset for Redland City')
        new_sdm_page.select_environment()
        new_sdm_page.select_current_climate_layers('Current climate layers for Australia, 2.5arcmin (~5km)')
        new_sdm_page.select_environmental_datasets('Current climate layers for Australia, 2.5arcmin (~5km)',
                                                   'B14 - Precipitation of Driest Month')
        new_sdm_page.select_environmental_datasets('Current climate layers for Australia, 2.5arcmin (~5km)',
                                                   'B15 - Precipitation Seasonality (Coefficient of Variation)')
        new_sdm_page.select_run()
        experiment_view = new_sdm_page.select_review_start_experiment()

        # Wait until completion
        experiment_view.wait_for_experiment_to_complete(500)
        self.assertTrue(experiment_view.has_completed_successfully())

        self.assertTrue(experiment_view.has_results_header(experiment_name))
        self.assertEqual(9, experiment_view.get_num_output_files())
        self.assertTrue(experiment_view.has_result_file('mean_response_curves.png'))
        self.assertTrue(experiment_view.has_result_file('pROC.png'))
        self.assertTrue(experiment_view.has_result_file('cta.Rout'))
        self.assertTrue(experiment_view.has_result_file('combined.modelEvaluation.csv'))
        self.assertTrue(experiment_view.has_result_file('biomod2.modelEvaluation.csv'))
        self.assertTrue(experiment_view.has_result_file('model.object.RData.zip'))
        self.assertTrue(experiment_view.has_result_file('proj_current_Phascolarctus.cinereus.tif'))
        self.assertTrue(experiment_view.has_result_file('proj_current_ClampingMask.tif'))
        self.assertTrue(experiment_view.has_result_file('pstats.json'))

        # Cleanup
        self.delete_experiment(experiment_name)

    def test_convex_hull_1km(self):
        homepage = Homepage(self.driver)
        login_page = homepage.click_login()
        homepage = login_page.valid_login(self.username, self.password)
        experiment_page = homepage.click_experiments()
        new_sdm_page = experiment_page.click_new_sdm_experiment()

        experiment_name = "convhull_" + generate_timestamp()

        new_sdm_page.enter_experiment_name(experiment_name)
        new_sdm_page.enter_experiment_description('Convex Hull Experiment with Koala occurrences')
        new_sdm_page.select_configuration()
        new_sdm_page.select_sdm_algorithm('Convex Hull')
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

        self.assertTrue(experiment_view.has_results_header(experiment_name))
        self.assertEqual(15, experiment_view.get_num_output_files())
        self.assertTrue(experiment_view.has_result_file('dismo.eval.object.RData'))
        self.assertTrue(experiment_view.has_result_file('AUC.png'))
        self.assertTrue(experiment_view.has_result_file('results.html'))
        self.assertTrue(experiment_view.has_result_file('combined.modelEvaluation.csv'))
        self.assertTrue(experiment_view.has_result_file('maxent_like_VariableImportance.csv'))
        self.assertTrue(experiment_view.has_result_file('biomod2_like_VariableImportance.csv'))
        self.assertTrue(experiment_view.has_result_file('Phascolarctus.cinereus.model.object.RData'))
        self.assertTrue(experiment_view.has_result_file('convhull.Rout'))
        self.assertTrue(experiment_view.has_result_file('lon_response.png'))
        self.assertTrue(experiment_view.has_result_file('bioclim_15_response.png'))
        self.assertTrue(experiment_view.has_result_file('lat_response.png'))
        self.assertTrue(experiment_view.has_result_file('bioclim_14_response.png'))
        self.assertTrue(experiment_view.has_result_file('results.html.zip'))
        self.assertTrue(experiment_view.has_result_file('pstats.json'))
        self.assertTrue(experiment_view.has_result_file('proj_current_Phascolarctus.cinereus.tif'))

        # Cleanup
        self.delete_experiment(experiment_name)

    def test_convex_hull_5km(self):
        homepage = Homepage(self.driver)
        login_page = homepage.click_login()
        homepage = login_page.valid_login(self.username, self.password)
        experiment_page = homepage.click_experiments()
        new_sdm_page = experiment_page.click_new_sdm_experiment()

        experiment_name = "convhull_" + generate_timestamp()

        new_sdm_page.enter_experiment_name(experiment_name)
        new_sdm_page.enter_experiment_description('Convex Hull Experiment with Koala occurrences')
        new_sdm_page.select_configuration()
        new_sdm_page.select_sdm_algorithm('Convex Hull')
        new_sdm_page.select_occurrences()
        new_sdm_page.select_occurrences_dataset('Koala - Mini occurrence dataset for Redland City')
        new_sdm_page.select_absences()
        new_sdm_page.select_absences_dataset('Koala - Mini absence dataset for Redland City')
        new_sdm_page.select_environment()
        new_sdm_page.select_current_climate_layers('Current climate layers for Australia, 2.5arcmin (~5km)')
        new_sdm_page.select_environmental_datasets('Current climate layers for Australia, 2.5arcmin (~5km)',
                                                   'B14 - Precipitation of Driest Month')
        new_sdm_page.select_environmental_datasets('Current climate layers for Australia, 2.5arcmin (~5km)',
                                                   'B15 - Precipitation Seasonality (Coefficient of Variation)')
        new_sdm_page.select_run()
        experiment_view = new_sdm_page.select_review_start_experiment()

        # Wait until completion
        experiment_view.wait_for_experiment_to_complete(500)
        self.assertTrue(experiment_view.has_completed_successfully())

        self.assertTrue(experiment_view.has_results_header(experiment_name))
        self.assertEqual(15, experiment_view.get_num_output_files())
        self.assertTrue(experiment_view.has_result_file('dismo.eval.object.RData'))
        self.assertTrue(experiment_view.has_result_file('AUC.png'))
        self.assertTrue(experiment_view.has_result_file('results.html'))
        self.assertTrue(experiment_view.has_result_file('combined.modelEvaluation.csv'))
        self.assertTrue(experiment_view.has_result_file('maxent_like_VariableImportance.csv'))
        self.assertTrue(experiment_view.has_result_file('biomod2_like_VariableImportance.csv'))
        self.assertTrue(experiment_view.has_result_file('Phascolarctus.cinereus.model.object.RData'))
        self.assertTrue(experiment_view.has_result_file('convhull.Rout'))
        self.assertTrue(experiment_view.has_result_file('lon_response.png'))
        self.assertTrue(experiment_view.has_result_file('bioclim_15_response.png'))
        self.assertTrue(experiment_view.has_result_file('lat_response.png'))
        self.assertTrue(experiment_view.has_result_file('bioclim_14_response.png'))
        self.assertTrue(experiment_view.has_result_file('results.html.zip'))
        self.assertTrue(experiment_view.has_result_file('pstats.json'))
        self.assertTrue(experiment_view.has_result_file('proj_current_Phascolarctus.cinereus.tif'))

        # Cleanup
        self.delete_experiment(experiment_name)

    def test_domain_1km(self):
        homepage = Homepage(self.driver)
        login_page = homepage.click_login()
        homepage = login_page.valid_login(self.username, self.password)
        experiment_page = homepage.click_experiments()
        new_sdm_page = experiment_page.click_new_sdm_experiment()

        experiment_name = "domain_" + generate_timestamp()

        new_sdm_page.enter_experiment_name(experiment_name)
        new_sdm_page.enter_experiment_description('Domain experiments with Koala occurrences')
        new_sdm_page.select_configuration()
        new_sdm_page.select_sdm_algorithm('Domain')
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

        self.assertTrue(experiment_view.has_results_header(experiment_name))
        self.assertEqual(13, experiment_view.get_num_output_files())
        self.assertTrue(experiment_view.has_result_file('dismo.eval.object.RData'))
        self.assertTrue(experiment_view.has_result_file('AUC.png'))
        self.assertTrue(experiment_view.has_result_file('results.html'))
        self.assertTrue(experiment_view.has_result_file('combined.modelEvaluation.csv'))
        self.assertTrue(experiment_view.has_result_file('maxent_like_VariableImportance.csv'))
        self.assertTrue(experiment_view.has_result_file('biomod2_like_VariableImportance.csv'))
        self.assertTrue(experiment_view.has_result_file('Phascolarctus.cinereus.model.object.RData'))
        self.assertTrue(experiment_view.has_result_file('domain.Rout'))
        self.assertTrue(experiment_view.has_result_file('bioclim_15_response.png'))
        self.assertTrue(experiment_view.has_result_file('bioclim_14_response.png'))
        self.assertTrue(experiment_view.has_result_file('results.html.zip'))
        self.assertTrue(experiment_view.has_result_file('proj_current_Phascolarctus.cinereus.tif'))
        self.assertTrue(experiment_view.has_result_file('pstats.json'))

        # Cleanup
        self.delete_experiment(experiment_name)

    def test_domain_5km(self):
        homepage = Homepage(self.driver)
        login_page = homepage.click_login()
        homepage = login_page.valid_login(self.username, self.password)
        experiment_page = homepage.click_experiments()
        new_sdm_page = experiment_page.click_new_sdm_experiment()

        experiment_name = "domain_" + generate_timestamp()

        new_sdm_page.enter_experiment_name(experiment_name)
        new_sdm_page.enter_experiment_description('Domain experiments with Koala occurrences')
        new_sdm_page.select_configuration()
        new_sdm_page.select_sdm_algorithm('Domain')
        new_sdm_page.select_occurrences()
        new_sdm_page.select_occurrences_dataset('Koala - Mini occurrence dataset for Redland City')
        new_sdm_page.select_absences()
        new_sdm_page.select_absences_dataset('Koala - Mini absence dataset for Redland City')
        new_sdm_page.select_environment()
        new_sdm_page.select_current_climate_layers('Current climate layers for Australia, 2.5arcmin (~5km)')
        new_sdm_page.select_environmental_datasets('Current climate layers for Australia, 2.5arcmin (~5km)',
                                                   'B14 - Precipitation of Driest Month')
        new_sdm_page.select_environmental_datasets('Current climate layers for Australia, 2.5arcmin (~5km)',
                                                   'B15 - Precipitation Seasonality (Coefficient of Variation)')
        new_sdm_page.select_run()
        experiment_view = new_sdm_page.select_review_start_experiment()

        # Wait until completion
        experiment_view.wait_for_experiment_to_complete(500)
        self.assertTrue(experiment_view.has_completed_successfully())

        self.assertTrue(experiment_view.has_results_header(experiment_name))
        self.assertEqual(13, experiment_view.get_num_output_files())
        self.assertTrue(experiment_view.has_result_file('dismo.eval.object.RData'))
        self.assertTrue(experiment_view.has_result_file('AUC.png'))
        self.assertTrue(experiment_view.has_result_file('results.html'))
        self.assertTrue(experiment_view.has_result_file('combined.modelEvaluation.csv'))
        self.assertTrue(experiment_view.has_result_file('maxent_like_VariableImportance.csv'))
        self.assertTrue(experiment_view.has_result_file('biomod2_like_VariableImportance.csv'))
        self.assertTrue(experiment_view.has_result_file('Phascolarctus.cinereus.model.object.RData'))
        self.assertTrue(experiment_view.has_result_file('domain.Rout'))
        self.assertTrue(experiment_view.has_result_file('bioclim_15_response.png'))
        self.assertTrue(experiment_view.has_result_file('bioclim_14_response.png'))
        self.assertTrue(experiment_view.has_result_file('results.html.zip'))
        self.assertTrue(experiment_view.has_result_file('proj_current_Phascolarctus.cinereus.tif'))
        self.assertTrue(experiment_view.has_result_file('pstats.json'))

        # Cleanup
        self.delete_experiment(experiment_name)

    def test_fda_1km(self):
        homepage = Homepage(self.driver)
        login_page = homepage.click_login()
        homepage = login_page.valid_login(self.username, self.password)
        experiment_page = homepage.click_experiments()
        new_sdm_page = experiment_page.click_new_sdm_experiment()

        experiment_name = "fda_" + generate_timestamp()

        new_sdm_page.enter_experiment_name(experiment_name)
        new_sdm_page.enter_experiment_description('Flexible Descriminant Analysis with Koala occurrences')
        new_sdm_page.select_configuration()
        new_sdm_page.select_sdm_algorithm('Flexible Discriminant Analysis')
        new_sdm_page.select_occurrences()
        new_sdm_page.select_occurrences_dataset('Koala - Mini occurrence dataset for Redland City')
        new_sdm_page.select_absences()
        new_sdm_page.select_absences_dataset('Koala - Mini absence dataset for Redland City')
        new_sdm_page.select_environment()
        # Note: FDA Only works with 5km climate layer datasets
        new_sdm_page.select_current_climate_layers('Current climate layers for Redland City, 30" (~1km)')
        new_sdm_page.select_environmental_datasets('Current climate layers for Redland City, 30" (~1km)',
                                                   'B14 - Precipitation of Driest Month')
        new_sdm_page.select_environmental_datasets('Current climate layers for Redland City, 30" (~1km)',
                                                   'B15 - Precipitation Seasonality (Coefficient of Variation)')
        new_sdm_page.select_run()
        experiment_view = new_sdm_page.select_review_start_experiment()

        # Wait until completion
        experiment_view.wait_for_experiment_to_complete(500)

        # FDA fails with 1km climate layer
        self.assertTrue(experiment_view.has_completed_with_failure())

        # Cleanup
        self.delete_experiment(experiment_name)

    def test_fda_5km(self):
        homepage = Homepage(self.driver)
        login_page = homepage.click_login()
        homepage = login_page.valid_login(self.username, self.password)
        experiment_page = homepage.click_experiments()
        new_sdm_page = experiment_page.click_new_sdm_experiment()

        experiment_name = "fda_" + generate_timestamp()

        new_sdm_page.enter_experiment_name(experiment_name)
        new_sdm_page.enter_experiment_description('Flexible Descriminant Analysis with Koala occurrences')
        new_sdm_page.select_configuration()
        new_sdm_page.select_sdm_algorithm('Flexible Discriminant Analysis')
        new_sdm_page.select_occurrences()
        new_sdm_page.select_occurrences_dataset('Koala - Mini occurrence dataset for Redland City')
        new_sdm_page.select_absences()
        new_sdm_page.select_absences_dataset('Koala - Mini absence dataset for Redland City')
        new_sdm_page.select_environment()
        # Note: FDA Only works with 5km climate layer datasets
        new_sdm_page.select_current_climate_layers('Current climate layers for Australia, 2.5arcmin (~5km)')
        new_sdm_page.select_environmental_datasets('Current climate layers for Australia, 2.5arcmin (~5km)',
                                                   'B14 - Precipitation of Driest Month')
        new_sdm_page.select_environmental_datasets('Current climate layers for Australia, 2.5arcmin (~5km)',
                                                   'B15 - Precipitation Seasonality (Coefficient of Variation)')
        new_sdm_page.select_run()
        experiment_view = new_sdm_page.select_review_start_experiment()

        # Wait until completion
        experiment_view.wait_for_experiment_to_complete(500)
        self.assertTrue(experiment_view.has_completed_successfully())

        self.assertTrue(experiment_view.has_results_header(experiment_name))
        self.assertEqual(9, experiment_view.get_num_output_files())
        self.assertTrue(experiment_view.has_result_file('mean_response_curves.png'))
        self.assertTrue(experiment_view.has_result_file('pROC.png'))
        self.assertTrue(experiment_view.has_result_file('biomod2.modelEvaluation.csv'))
        self.assertTrue(experiment_view.has_result_file('combined.modelEvaluation.csv'))
        self.assertTrue(experiment_view.has_result_file('fda.Rout'))
        self.assertTrue(experiment_view.has_result_file('model.object.RData.zip'))
        self.assertTrue(experiment_view.has_result_file('proj_current_Phascolarctus.cinereus.tif'))
        self.assertTrue(experiment_view.has_result_file('proj_current_ClampingMask.tif'))
        self.assertTrue(experiment_view.has_result_file('pstats.json'))

        # Cleanup
        self.delete_experiment(experiment_name)

    def test_gam_1km(self):
        homepage = Homepage(self.driver)
        login_page = homepage.click_login()
        homepage = login_page.valid_login(self.username, self.password)
        experiment_page = homepage.click_experiments()
        new_sdm_page = experiment_page.click_new_sdm_experiment()

        experiment_name = "gam_" + generate_timestamp()

        new_sdm_page.enter_experiment_name(experiment_name)
        new_sdm_page.enter_experiment_description('Generalized Additive Model with Koala occurrences')
        new_sdm_page.select_configuration()
        new_sdm_page.select_sdm_algorithm('Generalized Additive Model')
        new_sdm_page.select_occurrences()
        new_sdm_page.select_occurrences_dataset('Koala - Mini occurrence dataset for Redland City')
        new_sdm_page.select_absences()
        new_sdm_page.select_absences_dataset('Koala - Mini absence dataset for Redland City')
        new_sdm_page.select_environment()
        # Note: FDA Only works with 5km climate layer datasets
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

        self.assertTrue(experiment_view.has_results_header(experiment_name))
        self.assertEqual(9, experiment_view.get_num_output_files())

        self.assertTrue(experiment_view.has_result_file('mean_response_curves.png'))
        self.assertTrue(experiment_view.has_result_file('pROC.png'))
        self.assertTrue(experiment_view.has_result_file('gam.Rout'))
        self.assertTrue(experiment_view.has_result_file('biomod2.modelEvaluation.csv'))
        self.assertTrue(experiment_view.has_result_file('combined.modelEvaluation.csv'))
        self.assertTrue(experiment_view.has_result_file('model.object.RData.zip'))
        self.assertTrue(experiment_view.has_result_file('proj_current_Phascolarctus.cinereus.tif'))
        self.assertTrue(experiment_view.has_result_file('proj_current_ClampingMask.tif'))
        self.assertTrue(experiment_view.has_result_file('pstats.json'))

        # Cleanup
        self.delete_experiment(experiment_name)

    def test_gam_5km(self):
        homepage = Homepage(self.driver)
        login_page = homepage.click_login()
        homepage = login_page.valid_login(self.username, self.password)
        experiment_page = homepage.click_experiments()
        new_sdm_page = experiment_page.click_new_sdm_experiment()

        experiment_name = "gam_" + generate_timestamp()

        new_sdm_page.enter_experiment_name(experiment_name)
        new_sdm_page.enter_experiment_description('Generalized Additive Model with Koala occurrences')
        new_sdm_page.select_configuration()
        new_sdm_page.select_sdm_algorithm('Generalized Additive Model')
        new_sdm_page.select_occurrences()
        new_sdm_page.select_occurrences_dataset('Koala - Mini occurrence dataset for Redland City')
        new_sdm_page.select_absences()
        new_sdm_page.select_absences_dataset('Koala - Mini absence dataset for Redland City')
        new_sdm_page.select_environment()
        # Note: FDA Only works with 5km climate layer datasets
        new_sdm_page.select_current_climate_layers('Current climate layers for Australia, 2.5arcmin (~5km)')
        new_sdm_page.select_environmental_datasets('Current climate layers for Australia, 2.5arcmin (~5km)',
                                                   'B14 - Precipitation of Driest Month')
        new_sdm_page.select_environmental_datasets('Current climate layers for Australia, 2.5arcmin (~5km)',
                                                   'B15 - Precipitation Seasonality (Coefficient of Variation)')
        new_sdm_page.select_run()
        experiment_view = new_sdm_page.select_review_start_experiment()

        # Wait until completion
        experiment_view.wait_for_experiment_to_complete(500)
        self.assertTrue(experiment_view.has_completed_successfully())

        self.assertTrue(experiment_view.has_results_header(experiment_name))
        self.assertEqual(9, experiment_view.get_num_output_files())

        self.assertTrue(experiment_view.has_result_file('mean_response_curves.png'))
        self.assertTrue(experiment_view.has_result_file('pROC.png'))
        self.assertTrue(experiment_view.has_result_file('gam.Rout'))
        self.assertTrue(experiment_view.has_result_file('biomod2.modelEvaluation.csv'))
        self.assertTrue(experiment_view.has_result_file('combined.modelEvaluation.csv'))
        self.assertTrue(experiment_view.has_result_file('model.object.RData.zip'))
        self.assertTrue(experiment_view.has_result_file('proj_current_Phascolarctus.cinereus.tif'))
        self.assertTrue(experiment_view.has_result_file('proj_current_ClampingMask.tif'))
        self.assertTrue(experiment_view.has_result_file('pstats.json'))

        # Cleanup
        self.delete_experiment(experiment_name)
