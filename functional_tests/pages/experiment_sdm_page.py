from base_page import BasePage
from experiment_results_page import ExperimentResultsPage
from selenium.webdriver.support.ui import Select


class SDMExperimentPage(BasePage):

    def select_configuration(self):
        self.switch_tab("Configuration")

    def select_description(self):
        self.switch_tab("Description")

    def select_occurrences(self):
        self.switch_tab("Occurrences")

    def select_absences(self):
        self.switch_tab("Absences")

    def select_environment(self):
        self.switch_tab("Climate & Environmental Data")

    def select_review(self):
        self.switch_tab("Review")

    def select_run(self):
        self.switch_tab("Run")

    def enter_experiment_name(self, name):
        self.driver.find_element_by_name("form.widgets.IDublinCore.title").clear()
        self.driver.find_element_by_name("form.widgets.IDublinCore.title").send_keys(name)

    def enter_experiment_description(self, description):
        self.driver.find_element_by_name("form.widgets.IDublinCore.description").clear()
        self.driver.find_element_by_name("form.widgets.IDublinCore.description").send_keys(description)

    def select_sdm_algorithm(self, string):
        path_string = "(//input[@data-friendlyname='checkbox_algorithm_" + string + "'])"
        self.driver.find_element_by_xpath(path_string).click()

    def select_occurrences_dataset(self, dataset_name):
        path_string = 'table.bccvl-occurrencestable input[data-friendlyname="radio_' + dataset_name + '"]'
        self.driver.find_element_by_css_selector(path_string).click()

    def select_absences_dataset(self, dataset_name):
        path_string = 'table.bccvl-absencestable input[data-friendlyname="radio_' + dataset_name + '"]'
        self.driver.find_element_by_css_selector(path_string).click()

    def select_current_climate_layers(self, resolution, string):
        # select the correct resolution filter
        select = Select(self.driver.find_element_by_name("form.widgets.resolution:list"))
        select.select_by_visible_text(resolution)
        # Yes, there is a type here, but that's how it is on the backend
        path_string = "(//tr[@data-friendlyname='collapbsable_climatelayer_" + string + "'])"
        self.driver.find_element_by_xpath(path_string).click()

    def select_environmental_datasets(self, dataset, checkbox):
        # Yes, there is a type here, but that's how it is on the backend
        path_string = "(//tr[@data-friendlyname='collapbsable_climatelayer_" + dataset + \
                      "']/..//input[@data-friendlyname='checkbox_climatelayer_" + checkbox + "'])"
        self.driver.find_element_by_xpath(path_string).click()

    def select_review_start_experiment(self):
        self.driver.find_element_by_name("form.buttons.save").click()
        view_experiment_page = ExperimentResultsPage(self.driver)
        return view_experiment_page

    def check_review_start_experiment(self):
        self.driver.find_element_by_name("form.buttons.save")

    def select_submit_invalid_experiment(self):
        self.driver.find_element_by_name("form.buttons.save").click()

    def enter_ala_search_string(self,string):
        self.driver.find_element_by_name("searchOccurrence_query").clear()
        self.driver.find_element_by_name("searchOccurrence_query").send_keys(string)

    def select_ala_dataset_to_download(self,string):
        self.driver.find_element_by_link_text(string).click()

    def check_tab_displayed(self, string):
        self.driver.find_element_by_link_text(string)

    def check_experiment_name_textbox(self):
        self.driver.find_element_by_name("form.widgets.IDublinCore.title")

    def check_experiment_description_textbox(self):
        self.driver.find_element_by_name("form.widgets.IDublinCore.title")

    def select_algorithms_configuration(self, algorithm):
        path_string = "configuration for " + algorithm
        self.driver.find_element_by_link_text(path_string).click()

    def enter_brt_config_tree_complexity(self, value):
        self.driver.find_element_by_name("form.widgets.parameters_brt.widgets.tree_complexity").clear()
        self.driver.find_element_by_name("form.widgets.parameters_brt.widgets.tree_complexity").send_keys(value)

    def enter_brt_config_learning_rate(self, value):
        self.driver.find_element_by_name("form.widgets.parameters_brt.widgets.learning_rate").clear()
        self.driver.find_element_by_name("form.widgets.parameters_brt.widgets.learning_rate").send_keys(value)

    def enter_brt_config_bag_fraction(self, value):
        self.driver.find_element_by_name("form.widgets.parameters_brt.widgets.bag_fraction").clear()
        self.driver.find_element_by_name("form.widgets.parameters_brt.widgets.bag_fraction").send_keys(value)

    def enter_brt_config_var_monotone(self, value):
        self.driver.find_element_by_xpath("//select[@name='form.widgets.parameters_brt.widgets.var_monotone:list']/option[text()='" + value + "']").click()

    def enter_brt_config_n_folds(self, value):
        self.driver.find_element_by_name("form.widgets.parameters_brt.widgets.n_folds").clear()
        self.driver.find_element_by_name("form.widgets.parameters_brt.widgets.n_folds").send_keys(value)

    def enter_brt_config_family(self, name):
        self.driver.find_element_by_xpath("//select[@name='form.widgets.parameters_brt.widgets.family:list']/option[text()='" + name + "']").click()

    def enter_brt_config_n_trees(self, value):
        self.driver.find_element_by_name("form.widgets.parameters_brt.widgets.n_trees").clear()
        self.driver.find_element_by_name("form.widgets.parameters_brt.widgets.n_trees").send_keys(value)

    def enter_brt_config_max_trees(self, value):
        self.driver.find_element_by_name("form.widgets.parameters_brt.widgets.max_trees").clear()
        self.driver.find_element_by_name("form.widgets.parameters_brt.widgets.max_trees").send_keys(value)

    def enter_brt_config_tolerance_method(self, name):
        self.driver.find_element_by_xpath("//select[@name='form.widgets.parameters_brt.widgets.tolerance_method:list']/option[text()='" + name + "']").click()

    def enter_brt_config_tolerance_value(self, value):
        self.driver.find_element_by_name("form.widgets.parameters_brt.widgets.tolerance_value").clear()
        self.driver.find_element_by_name("form.widgets.parameters_brt.widgets.tolerance_value").send_keys(value)
