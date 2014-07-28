from base_page import BasePage
from experiment_results_page import ExperimentResultsPage


class ProjectionExperimentPage(BasePage):
    def select_source_model_tab(self):
        self.driver.find_element_by_link_text("Source Model").click()

    def select_description(self):
        self.driver.find_element_by_link_text("Description").click()

    def select_projection(self):
        self.driver.find_element_by_link_text("Projection").click()

    def select_run(self):
        self.driver.find_element_by_link_text("Run").click()

    def select_run_experiment(self):
        self.driver.find_element_by_name("form.buttons.save").click()
        new_experiment_results_page = ExperimentResultsPage(self.driver)
        return new_experiment_results_page

    def enter_experiment_name(self, name):
        self.driver.find_element_by_name("form.widgets.IDublinCore.title").clear()
        self.driver.find_element_by_name("form.widgets.IDublinCore.title").send_keys(name)

    def enter_experiment_description(self, description):
        self.driver.find_element_by_name("form.widgets.IDublinCore.description").clear()
        self.driver.find_element_by_name("form.widgets.IDublinCore.description").send_keys(description)

    def select_source_model(self, unique_id):
        source_models = self.driver.find_elements_by_css_selector("table.bccvl-datasetstable label:first-child")
        for source_model in source_models:
            if source_model.text.find(unique_id) != -1:
                # Xpath .. retrieve's an element's parent.
                # We need the 3rd parent's checkbox
                source_model.find_element_by_xpath("..").find_element_by_xpath("..").find_element_by_xpath(
                    "..").find_element_by_css_selector("input").click()
                break

    # these three methods take an string integer value which indicates which of the tickboxes
    # to check on the projection tab
    def select_year(self, year):
        self._projection_tickboxes(year, "table.bccvl-yearstable td.bccvl-table-label p")

    def select_emission_scenario(self, scenario):
        self._projection_tickboxes(scenario, "table.bccvl-emissionscenariostable td.bccvl-table-label p")

    def select_climate_models(self, model):
        self._projection_tickboxes(model, "table.bccvl-climatemodelstable td.bccvl-table-label p")

    def _projection_tickboxes(self, name, table):
        table_items = self.driver.find_elements_by_css_selector(table)
        for item in table_items:
            if item.text.find(name) != -1:
                item.find_element_by_xpath("..").find_element_by_xpath("..").find_element_by_xpath(
                    "..").find_element_by_css_selector("input").click()