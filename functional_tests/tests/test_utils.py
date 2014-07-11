import time

#
# Contains methods to help with testing
#


# Generates a unique timestamp of the format YYYYMMDDHHmmSS so we can name things uniquely
def generate_timestamp():
    return time.strftime("%Y%m%d%H%M%S", time.localtime())

# Generates a generic SDM experiment
def create_sdm(test, new_sdm_page):
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
    experiment_view.wait_for_experiment_to_complete()
    test.assertTrue(experiment_view.has_completed_successfully())
    return sdm_experiment_name

# Generates a generic SDM experiment
def create_projection(test,sdm_experiment_name, new_projection_page):
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
    experiment_result_page.wait_for_experiment_to_complete()
    test.assertTrue(experiment_result_page.has_completed_successfully())
    return projection_experiment_name