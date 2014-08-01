from experiment_test_base import ExperimentTestCase
from pages.homepage import Homepage
from test_utils import generate_timestamp
import os


class TestSpeciesTraitModel(ExperimentTestCase):

    def test_STM(self):
        homepage = Homepage(self.driver)
        login_page = homepage.click_login()
        homepage = login_page.valid_login(self.username, self.password)
        dataset_page = homepage.click_datasets()
        dataset_upload_page = dataset_page.select_dataset_upload()
        upload_page = dataset_upload_page.select_dataset_type("Species Trait")

        upload_page.upload_file(os.getcwd() + "/../shuker.csv")
        dataset_title = "species_trait_" + generate_timestamp()
        upload_page.enter_dataset_title(dataset_title)
        upload_page.enter_dataset_description("bleh")
        upload_page.agree_to_terms_and_conditions()
        dataset_page = upload_page.submit()

        experiment_page = homepage.click_experiments()
        new_STM = experiment_page.click_new_species_trait_model()

        experiment_name = "stm_" + generate_timestamp()
        new_STM.enter_experiment_name(experiment_name)
        new_STM.enter_experiment_description("An STM experiment")
        new_STM.select_configuration()
        new_STM.enter_formula("Litoria_olongburensis_A ~ salinity")
        new_STM.select_FRMPA("Linear Models")
        new_STM.select_input_datasets()
        new_STM.select_input_dataset(dataset_title)
        new_STM.select_run()
        experiment_view = new_STM.select_start_experiment()

        # Wait until completion
        experiment_view.wait_for_experiment_to_complete()
        self.assertTrue(experiment_view.has_completed_successfully())

        # Check results
        self.assertTrue(experiment_view.has_results_header(experiment_name))
        self.assertEqual(4, experiment_view.get_num_output_files())
        self.assertTrue(experiment_view.has_result_file('lm.model.object.RData'))
        self.assertTrue(experiment_view.has_result_file('lm.Rout'))
        self.assertTrue(experiment_view.has_result_file('lm_result_summary.txt'))
        self.assertTrue(experiment_view.has_result_file('pstats.json'))

        # Cleanup
        self.delete_experiment(experiment_name)

