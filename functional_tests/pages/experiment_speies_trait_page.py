from base_page import BasePage
from experiment_results_page import ExperimentResultsPage


class SpeciesTraitExperimentPage(BasePage):

    def select_configuration(self):
        self.driver.find_element_by_link_text("Configuration").click()

    def select_description(self):
        self.driver.find_element_by_link_text("Description").click()

    def select_input_datasets(self):
        self.driver.find_element_by_link_text("Input Datasets").click()

    def select_run(self):
        self.driver.find_element_by_link_text("Run").click()

    def select_start_experiment(self):
        self.driver.find_element_by_css_selector("button.bccvllinks-experiment-start").click()
        view_experiment_page = ExperimentResultsPage(self.driver)
        return view_experiment_page

    def enter_experiment_name(self, name):
        self.driver.find_element_by_name("form.widgets.IDublinCore.title").clear()
        self.driver.find_element_by_name("form.widgets.IDublinCore.title").send_keys(name)

    def enter_experiment_description(self, description):
        self.driver.find_element_by_name("form.widgets.IDublinCore.description").clear()
        self.driver.find_element_by_name("form.widgets.IDublinCore.description").send_keys(description)

    def enter_formula(self, formula):
        self.driver.find_element_by_id("form-widgets-formula").send_keys(formula)

    def select_FRMPA(self, model):
        if model == "Linear Models":
            self.driver.find_element_by_id("form-widgets-algorithm-0").click()
        else:
            assert True is False

    def select_input_dataset(self, name):
        items = self.driver.find_elements_by_css_selector('table.bccvl-datasetstable tbody tr')
        # within each TR there are 3 TDs which are the checkbox, the info and the visualise button
        # get the first ones and put them into a checkbox list, the second one into a namelist
        checkboxes = []
        dataset_names = []

        for item in items:
            data = item.find_elements_by_css_selector('td')
            checkboxes.append(data[0].find_element_by_css_selector('input'))
            dataset_names.append(data[1].find_element_by_css_selector('label'))

        index = 0
        while index < len(dataset_names):
            if name.lower() in dataset_names[index].text.lower():
                checkboxes[index].click()
                return
            index = index + 1

        # Shouldn't get to this point
        assert True is False


