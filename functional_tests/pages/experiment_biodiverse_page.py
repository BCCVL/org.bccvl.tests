from base_page import BasePage
from experiment_results_page import ExperimentResultsPage
from selenium.webdriver.support.ui import Select


class BiodiverseExperimentPage(BasePage):
    def select_source_projection_tab(self):
        self.switch_tab("Source Projection")

    def select_configuration_tab(self):
        self.switch_tab("Configuration")

    def select_description(self):
        self.switch_tab("Description")

    def select_run(self):
        self.switch_tab("Run")

    def select_run_experiment(self):
        self.driver.find_element_by_name("form.buttons.save").click()
        new_experiment_results_page = ExperimentResultsPage(self.driver)
        return new_experiment_results_page

    def enter_experiment_name(self, name):
        self.driver.find_element_by_name("form.widgets.IDublinCore.title").clear()
        self.driver.find_element_by_name("form.widgets.IDublinCore.title").send_keys(name)

    def select_threshold_value(self, threshold):
        self.driver.find_element_by_css_selector("td.bccvl-table-choose a").click()
        self.driver.find_element_by_css_selector("div.select2-search input").clear()
        self.driver.find_element_by_css_selector("div.select2-search input").send_keys(threshold)
        self.driver.find_elements_by_css_selector(".select2-result")[0].click()

    def select_cluster_size(self, size):
        select = Select(self.driver.find_element_by_id("form-widgets-cluster_size"))
        select.select_by_visible_text(size)

    def enter_experiment_description(self, description):
        self.driver.find_element_by_name("form.widgets.IDublinCore.description").clear()
        self.driver.find_element_by_name("form.widgets.IDublinCore.description").send_keys(description)

    def select_species(self, species):
        self._projection_tickboxes(species, "table.bccvl-speciestable p")

    def select_layers(self, layers):
        self._projection_tickboxes(layers, "table.bccvl-layerstable p")

    def select_years(self, years):
        self._projection_tickboxes(years, "table.bccvl-yearstable p")

    def select_projection_experiments(self, projection):
        self._projection_tickboxes(projection, "table.bccvl-projectiontable p")

    def _projection_tickboxes(self, name, table):
        checked = False
        table_items = self.driver.find_elements_by_css_selector(table)
        for item in table_items:
            if item.text.find(name) != -1:
                item.find_element_by_xpath("..").find_element_by_xpath("..").find_element_by_xpath(
                    "..").find_element_by_css_selector("input").click()
                checked = True

        # should have atleast checked something at some point
        assert checked is True
