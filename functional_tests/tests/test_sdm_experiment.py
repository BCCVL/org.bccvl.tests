from bccvl_testcase import BCCVLTestCase
from pages.homepage import Homepage


# Test cases for SDM experiments - testing all algorithms
class TestSDMExperiment(BCCVLTestCase):

    def test_ann(self):
        homepage = Homepage(self.driver)
        login_page = homepage.click_login()
        homepage = login_page.valid_login(self.username, self.password)
        experiment_page = homepage.click_experiments()
        new_sdm_page = experiment_page.click_new_sdm_experiment()

        title = "ann_"+self.generate_timestamp()
        self.experiments.append(title)

        new_sdm_page.enter_experiment_name(title)
        new_sdm_page.enter_experiment_description('Artificial Nueral Network with Koala occurrences')
        new_sdm_page.select_configuration()
        new_sdm_page.select_sdm_algorithm('Artificial Neural Network')
        new_sdm_page.select_occurrences()
        new_sdm_page.select_occurrences_dataset('Koala - Mini occurrence dataset for Redland City')
        new_sdm_page.select_absences()
        new_sdm_page.select_absences_dataset('Koala - Mini absence dataset for Redland City')
        new_sdm_page.select_environment()
        new_sdm_page.select_current_climate_layers('Current climate layers for Redland City, 30" (~1km)')
        new_sdm_page.select_environmental_datasets('Current climate layers for Redland City, 30" (~1km)', 'B14 - Precipitation of Driest Month')
        new_sdm_page.select_environmental_datasets('Current climate layers for Redland City, 30" (~1km)', 'B15 - Precipitation Seasonality (Coefficient of Variation)')
        new_sdm_page.select_run()
        experiment_view = new_sdm_page.select_review_start_experiment()

        # Wait until completion
        experiment_view.wait_for_experiment_to_complete(500)
        self.assertTrue(experiment_view.has_completed_successfully())

        # Check results
        self.assertTrue(experiment_view.has_results_header(title))
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

    def test_bioclim(self):
        homepage = Homepage(self.driver)
        login_page = homepage.click_login()
        homepage = login_page.valid_login(self.username, self.password)
        experiment_page = homepage.click_experiments()
        new_sdm_page = experiment_page.click_new_sdm_experiment()

        title = "bioclim_"+self.generate_timestamp()
        self.experiments.append(title)

        new_sdm_page.enter_experiment_name(title)
        new_sdm_page.enter_experiment_description('Bioclim with Koala occurrences')
        new_sdm_page.select_configuration()
        new_sdm_page.select_sdm_algorithm('Bioclim')
        new_sdm_page.select_occurrences()
        new_sdm_page.select_occurrences_dataset('Koala - Mini occurrence dataset for Redland City')
        new_sdm_page.select_absences()
        new_sdm_page.select_absences_dataset('Koala - Mini absence dataset for Redland City')
        new_sdm_page.select_environment()
        new_sdm_page.select_current_climate_layers('Current climate layers for Redland City, 30" (~1km)')
        new_sdm_page.select_environmental_datasets('Current climate layers for Redland City, 30" (~1km)', 'B14 - Precipitation of Driest Month')
        new_sdm_page.select_environmental_datasets('Current climate layers for Redland City, 30" (~1km)', 'B15 - Precipitation Seasonality (Coefficient of Variation)')
        new_sdm_page.select_run()
        experiment_view = new_sdm_page.select_review_start_experiment()

        # Wait until completion
        experiment_view.wait_for_experiment_to_complete(500)
        self.assertTrue(experiment_view.has_completed_successfully())

        self.assertTrue(experiment_view.has_results_header(title))
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

    def test_brt(self):
        homepage = Homepage(self.driver)
        login_page = homepage.click_login()
        homepage = login_page.valid_login(self.username, self.password)
        experiment_page = homepage.click_experiments()
        new_sdm_page = experiment_page.click_new_sdm_experiment()

        title = "brt_"+self.generate_timestamp()
        self.experiments.append(title)

        new_sdm_page.enter_experiment_name(title)
        new_sdm_page.enter_experiment_description('Boosted Regression Experiment with Koala occurrences')
        new_sdm_page.select_configuration()
        new_sdm_page.select_sdm_algorithm('Boosted Regression Tree')
        new_sdm_page.select_occurrences()
        new_sdm_page.select_occurrences_dataset('Koala - Mini occurrence dataset for Redland City')
        new_sdm_page.select_absences()
        new_sdm_page.select_absences_dataset('Koala - Mini absence dataset for Redland City')
        new_sdm_page.select_environment()
        new_sdm_page.select_current_climate_layers('Current climate layers for Redland City, 30" (~1km)')
        new_sdm_page.select_environmental_datasets('Current climate layers for Redland City, 30" (~1km)', 'B14 - Precipitation of Driest Month')
        new_sdm_page.select_environmental_datasets('Current climate layers for Redland City, 30" (~1km)', 'B15 - Precipitation Seasonality (Coefficient of Variation)')
        new_sdm_page.select_run()
        experiment_view = new_sdm_page.select_review_start_experiment()

        # Wait until completion
        experiment_view.wait_for_experiment_to_complete(500)
        self.assertTrue(experiment_view.has_completed_successfully())

        # Check results
        self.assertTrue(experiment_view.has_results_header(title))
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

    def test_circles(self):
        homepage = Homepage(self.driver)
        login_page = homepage.click_login()
        homepage = login_page.valid_login(self.username, self.password)
        experiment_page = homepage.click_experiments()
        new_sdm_page = experiment_page.click_new_sdm_experiment()

        title = "circles_"+self.generate_timestamp()
        self.experiments.append(title)

        new_sdm_page.enter_experiment_name(title)
        new_sdm_page.enter_experiment_description('Circles Experiment with Koala occurrences')
        new_sdm_page.select_configuration()
        new_sdm_page.select_sdm_algorithm('Circles')
        new_sdm_page.select_occurrences()
        new_sdm_page.select_occurrences_dataset('Koala - Mini occurrence dataset for Redland City')
        new_sdm_page.select_absences()
        new_sdm_page.select_absences_dataset('Koala - Mini absence dataset for Redland City')
        new_sdm_page.select_environment()
        new_sdm_page.select_current_climate_layers('Current climate layers for Redland City, 30" (~1km)')
        new_sdm_page.select_environmental_datasets('Current climate layers for Redland City, 30" (~1km)', 'B14 - Precipitation of Driest Month')
        new_sdm_page.select_environmental_datasets('Current climate layers for Redland City, 30" (~1km)', 'B15 - Precipitation Seasonality (Coefficient of Variation)')
        new_sdm_page.select_run()
        experiment_view = new_sdm_page.select_review_start_experiment()

        # Wait until completion
        experiment_view.wait_for_experiment_to_complete(500)
        self.assertTrue(experiment_view.has_completed_successfully())

        self.assertTrue(experiment_view.has_results_header(title))
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

    def test_classification_tree(self):
        homepage = Homepage(self.driver)
        login_page = homepage.click_login()
        homepage = login_page.valid_login(self.username, self.password)
        experiment_page = homepage.click_experiments()
        new_sdm_page = experiment_page.click_new_sdm_experiment()

        title = "ct_"+self.generate_timestamp()

        self.experiments.append(title)

        new_sdm_page.enter_experiment_name(title)
        new_sdm_page.enter_experiment_description('Classification Tree Experiment with Koala occurrences')
        new_sdm_page.select_configuration()
        new_sdm_page.select_sdm_algorithm('Classification Tree')
        new_sdm_page.select_occurrences()
        new_sdm_page.select_occurrences_dataset('Koala - Mini occurrence dataset for Redland City')
        new_sdm_page.select_absences()
        new_sdm_page.select_absences_dataset('Koala - Mini absence dataset for Redland City')
        new_sdm_page.select_environment()
        new_sdm_page.select_current_climate_layers('Current climate layers for Redland City, 30" (~1km)')
        new_sdm_page.select_environmental_datasets('Current climate layers for Redland City, 30" (~1km)', 'B14 - Precipitation of Driest Month')
        new_sdm_page.select_environmental_datasets('Current climate layers for Redland City, 30" (~1km)', 'B15 - Precipitation Seasonality (Coefficient of Variation)')
        new_sdm_page.select_run()
        experiment_view = new_sdm_page.select_review_start_experiment()

        # Wait until completion
        experiment_view.wait_for_experiment_to_complete(500)
        self.assertTrue(experiment_view.has_completed_successfully())

        self.assertTrue(experiment_view.has_results_header(title))
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

    def test_convex_hull(self):
        homepage = Homepage(self.driver)
        login_page = homepage.click_login()
        homepage = login_page.valid_login(self.username, self.password)
        experiment_page = homepage.click_experiments()
        new_sdm_page = experiment_page.click_new_sdm_experiment()

        title = "convhull_"+self.generate_timestamp()
        self.experiments.append(title)

        new_sdm_page.enter_experiment_name(title)
        new_sdm_page.enter_experiment_description('Convex Hull Experiment with Koala occurrences')
        new_sdm_page.select_configuration()
        new_sdm_page.select_sdm_algorithm('Convex Hull')
        new_sdm_page.select_occurrences()
        new_sdm_page.select_occurrences_dataset('Koala - Mini occurrence dataset for Redland City')
        new_sdm_page.select_absences()
        new_sdm_page.select_absences_dataset('Koala - Mini absence dataset for Redland City')
        new_sdm_page.select_environment()
        new_sdm_page.select_current_climate_layers('Current climate layers for Redland City, 30" (~1km)')
        new_sdm_page.select_environmental_datasets('Current climate layers for Redland City, 30" (~1km)', 'B14 - Precipitation of Driest Month')
        new_sdm_page.select_environmental_datasets('Current climate layers for Redland City, 30" (~1km)', 'B15 - Precipitation Seasonality (Coefficient of Variation)')
        new_sdm_page.select_run()
        experiment_view = new_sdm_page.select_review_start_experiment()

        # Wait until completion
        experiment_view.wait_for_experiment_to_complete(500)
        self.assertTrue(experiment_view.has_completed_successfully())

        self.assertTrue(experiment_view.has_results_header(title))
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

    def test_domain(self):
        homepage = Homepage(self.driver)
        login_page = homepage.click_login()
        homepage = login_page.valid_login(self.username, self.password)
        experiment_page = homepage.click_experiments()
        new_sdm_page = experiment_page.click_new_sdm_experiment()

        title = "domain_"+self.generate_timestamp()
        self.experiments.append(title)

        new_sdm_page.enter_experiment_name(title)
        new_sdm_page.enter_experiment_description('Domain experiments with Koala occurrences')
        new_sdm_page.select_configuration()
        new_sdm_page.select_sdm_algorithm('Domain')
        new_sdm_page.select_occurrences()
        new_sdm_page.select_occurrences_dataset('Koala - Mini occurrence dataset for Redland City')
        new_sdm_page.select_absences()
        new_sdm_page.select_absences_dataset('Koala - Mini absence dataset for Redland City')
        new_sdm_page.select_environment()
        new_sdm_page.select_current_climate_layers('Current climate layers for Redland City, 30" (~1km)')
        new_sdm_page.select_environmental_datasets('Current climate layers for Redland City, 30" (~1km)', 'B14 - Precipitation of Driest Month')
        new_sdm_page.select_environmental_datasets('Current climate layers for Redland City, 30" (~1km)', 'B15 - Precipitation Seasonality (Coefficient of Variation)')
        new_sdm_page.select_run()
        experiment_view = new_sdm_page.select_review_start_experiment()

        # Wait until completion
        experiment_view.wait_for_experiment_to_complete(500)
        self.assertTrue(experiment_view.has_completed_successfully())

        self.assertTrue(experiment_view.has_results_header(title))
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

    def test_fda(self):
        homepage = Homepage(self.driver)
        login_page = homepage.click_login()
        homepage = login_page.valid_login(self.username, self.password)
        experiment_page = homepage.click_experiments()
        new_sdm_page = experiment_page.click_new_sdm_experiment()

        title = "fda_"+self.generate_timestamp()
        self.experiments.append(title)

        new_sdm_page.enter_experiment_name(title)
        new_sdm_page.enter_experiment_description('Flexible Descriminant Analysis with Koala occurrences')
        new_sdm_page.select_configuration()
        new_sdm_page.select_sdm_algorithm('Flexible Discriminant Analysis')
        new_sdm_page.select_occurrences()
        new_sdm_page.select_occurrences_dataset('Koala - Mini occurrence dataset for Redland City')
        new_sdm_page.select_absences()
        new_sdm_page.select_absences_dataset('Koala - Mini absence dataset for Redland City')
        new_sdm_page.select_environment()
        new_sdm_page.select_current_climate_layers('Current climate layers for Redland City, 30" (~1km)')
        new_sdm_page.select_environmental_datasets('Current climate layers for Redland City, 30" (~1km)', 'B14 - Precipitation of Driest Month')
        new_sdm_page.select_environmental_datasets('Current climate layers for Redland City, 30" (~1km)', 'B15 - Precipitation Seasonality (Coefficient of Variation)')
        new_sdm_page.select_run()
        experiment_view = new_sdm_page.select_review_start_experiment()

        # Wait until completion
        experiment_view.wait_for_experiment_to_complete(500)
        self.assertTrue(experiment_view.has_completed_successfully())

        self.assertTrue(experiment_view.has_results_header(title))
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

    def test_gam(self):
        homepage = Homepage(self.driver)
        login_page = homepage.click_login()
        homepage = login_page.valid_login(self.username, self.password)
        experiment_page = homepage.click_experiments()
        new_sdm_page = experiment_page.click_new_sdm_experiment()

        title = "gam_"+self.generate_timestamp()
        self.experiments.append(title)

        new_sdm_page.enter_experiment_name(title)
        new_sdm_page.enter_experiment_description('Generalized Additive Model with Koala occurrences')
        new_sdm_page.select_configuration()
        new_sdm_page.select_sdm_algorithm('Generalized Additive Model')
        new_sdm_page.select_occurrences()
        new_sdm_page.select_occurrences_dataset('Koala - Mini occurrence dataset for Redland City')
        new_sdm_page.select_absences()
        new_sdm_page.select_absences_dataset('Koala - Mini absence dataset for Redland City')
        new_sdm_page.select_environment()
        new_sdm_page.select_current_climate_layers('Current climate layers for Redland City, 30" (~1km)')
        new_sdm_page.select_environmental_datasets('Current climate layers for Redland City, 30" (~1km)', 'B14 - Precipitation of Driest Month')
        new_sdm_page.select_environmental_datasets('Current climate layers for Redland City, 30" (~1km)', 'B15 - Precipitation Seasonality (Coefficient of Variation)')
        new_sdm_page.select_run()
        experiment_view = new_sdm_page.select_review_start_experiment()

        # Wait until completion
        experiment_view.wait_for_experiment_to_complete(500)
        self.assertTrue(experiment_view.has_completed_successfully())

        # TODO: add assertions for results

    def test_gbm(self):
        homepage = Homepage(self.driver)
        login_page = homepage.click_login()
        homepage = login_page.valid_login(self.username, self.password)
        experiment_page = homepage.click_experiments()
        new_sdm_page = experiment_page.click_new_sdm_experiment()

        title = "gbm_"+self.generate_timestamp()
        self.experiments.append(title)

        new_sdm_page.enter_experiment_name(title)
        new_sdm_page.enter_experiment_description('Generalized Boosting Modelwith Koala occurrences')
        new_sdm_page.select_configuration()
        new_sdm_page.select_sdm_algorithm('Generalized Boosting Model')
        new_sdm_page.select_occurrences()
        new_sdm_page.select_occurrences_dataset('Koala - Mini occurrence dataset for Redland City')
        new_sdm_page.select_absences()
        new_sdm_page.select_absences_dataset('Koala - Mini absence dataset for Redland City')
        new_sdm_page.select_environment()
        new_sdm_page.select_current_climate_layers('Current climate layers for Redland City, 30" (~1km)')
        new_sdm_page.select_environmental_datasets('Current climate layers for Redland City, 30" (~1km)', 'B14 - Precipitation of Driest Month')
        new_sdm_page.select_environmental_datasets('Current climate layers for Redland City, 30" (~1km)', 'B15 - Precipitation Seasonality (Coefficient of Variation)')
        new_sdm_page.select_run()
        experiment_view = new_sdm_page.select_review_start_experiment()

        # Wait until completion
        experiment_view.wait_for_experiment_to_complete(500)
        self.assertTrue(experiment_view.has_completed_successfully())

        # TODO: add assertions for results

    def test_glm(self):
        homepage = Homepage(self.driver)
        login_page = homepage.click_login()
        homepage = login_page.valid_login(self.username, self.password)
        experiment_page = homepage.click_experiments()
        new_sdm_page = experiment_page.click_new_sdm_experiment()

        title = "glm_"+self.generate_timestamp()
        self.experiments.append(title)

        new_sdm_page.enter_experiment_name(title)
        new_sdm_page.enter_experiment_description('Generalized Linear Model with Koala occurrences')
        new_sdm_page.select_configuration()
        new_sdm_page.select_sdm_algorithm('Generalized Linear Model')
        new_sdm_page.select_occurrences()
        new_sdm_page.select_occurrences_dataset('Koala - Mini occurrence dataset for Redland City')
        new_sdm_page.select_absences()
        new_sdm_page.select_absences_dataset('Koala - Mini absence dataset for Redland City')
        new_sdm_page.select_environment()
        new_sdm_page.select_current_climate_layers('Current climate layers for Redland City, 30" (~1km)')
        new_sdm_page.select_environmental_datasets('Current climate layers for Redland City, 30" (~1km)', 'B14 - Precipitation of Driest Month')
        new_sdm_page.select_environmental_datasets('Current climate layers for Redland City, 30" (~1km)', 'B15 - Precipitation Seasonality (Coefficient of Variation)')
        new_sdm_page.select_run()
        experiment_view = new_sdm_page.select_review_start_experiment()

        # Wait until completion
        experiment_view.wait_for_experiment_to_complete(500)
        self.assertTrue(experiment_view.has_completed_successfully())

        # TODO: add assertions for results

    # TODO: I don't have maxent.jar working on my local, all yours Stanley!
    def test_maxent(self):
        pass
