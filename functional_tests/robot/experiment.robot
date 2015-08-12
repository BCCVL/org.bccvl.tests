*** Settings ***

Documentation  A resource file containing the application specific keywords
...            that create our own domain specific language. This resource
...            implements keywords for testing HTML version of the test
...            application.
Library        Selenium2Library

*** Keywords ***

Select Occurrence Dataset
    ${button_modal} =  Set Variable  id('species_occurrence_dataset-popup')
    ${modal} =  Set Variable  id('species_occurrence_dataset-modal')
    ${modal_keyword_input} =  Set Variable  ${modal}//input[@name='datasets.filter.text']
    ${modal_search_button} =  Set Variable  ${modal}//button[@type='submit']
    Click Link  xpath=${button_modal}
    Wait Until Element Is Visible  xpath=${modal}
    Input Text  xpath=${modal_keyword_input}  Redland
    Click Button  xpath=${modal_search_button}
    Wait For Ajax
    # Select dataset
    Click Element  xpath=${modal}//div[contains(@class,'datasets-list-entry')]
    # Click Save Changes
    Click Button  xpath=${modal}//button[@class='btn btn-primary']
    Wait For Ajax

Select Absence Dataset
    ${button_modal} =  Set Variable  id('species_absence_dataset-popup')
    ${modal} =  Set Variable  id('species_absence_dataset-modal')
    ${modal_keyword_input} =  Set Variable  ${modal}//input[@name='datasets.filter.text']
    ${modal_search_button} =  Set Variable  ${modal}//button[@type='submit']
    Click Link  xpath=${button_modal}
    Wait Until Element Is Visible  xpath=${modal}
    Input Text  xpath=${modal_keyword_input}  Redland
    Click Button  xpath=${modal_search_button}
    Wait For Ajax
    # Select dataset
    Click Element  xpath=${modal}//div[contains(@class,'datasets-list-entry')]
    # Click Save Changes
    Click Button  xpath=${modal}//button[@class='btn btn-primary']
    Wait For Ajax

Select Environmental Dataset
    ${button_modal} =  Set Variable  id('environmental_datasets-popup')
    ${modal} =  Set Variable  id('environmental_datasets-modal')
    ${modal_keyword_input} =  Set Variable  ${modal}//input[@name='datasets.filter.text']
    ${modal_search_button} =  Set Variable  ${modal}//button[@type='submit']
    Click Link  xpath=${button_modal}
    Wait Until Element Is Visible  xpath=${modal}
    Input Text  xpath=${modal_keyword_input}  Redland
    Click Button  xpath=${modal_search_button}
    Wait For Ajax
    # Select dataset
    Click Element  xpath=${modal}//div[contains(@class,'datasets-list-entry')]
    # Click Save Changes
    Click Button  xpath=${modal}//button[@class='btn btn-primary']
    Wait For Ajax

Select SDM Experiment
    ${button_modal} =  Set Variable  id('species_distribution_models-popup')
    ${modal} =  Set Variable  id('species_distribution_models-modal')
    ${modal_keyword_input} =  Set Variable  ${modal}//input[@name='datasets.filter.text']
    ${modal_search_button} =  Set Variable  ${modal}//button[@type='submit']
    Click Link  xpath=${button_modal}    
    Wait Until Element Is Visible  xpath=${modal}
    Input Text  xpath=${modal_keyword_input}  Base SDM
    Click Button  xpath=${modal_search_button}
    Wait For Ajax
    # Select SDM
    Click Element  xpath=${modal}//div[contains(@class,'datasets-list-entry')]
    # Click Select Experiment
    Click Button  xpath=${modal}//button[@class='btn btn-primary']
    Wait For Ajax

Select Future Climate
    ${button_modal} =  Set Variable  id('future_climate_datasets-popup')
    ${modal} =  Set Variable  id('future_climate_datasets-modal')
    ${modal_keyword_input} =  Set Variable  ${modal}//input[@name='datasets.filter.text']
    ${modal_search_button} =  Set Variable  ${modal}//button[@type='submit']
    Click Link  xpath=${button_modal}
    Wait Until Element Is Visible  xpath=${modal}
    Input Text  xpath=${modal_keyword_input}  RCP3PD CCCMA-CGCM31
    Click Button  xpath=${modal_search_button}
    Wait For Ajax
    # Select Future Datasets
    Click Element  xpath=${modal}//div[contains(@class,'datasets-list-entry') and contains(string(.), '(~5km) - 2015')]
    # Click Select Experiment
    Click Button  xpath=${modal}//button[@class='btn btn-primary']
    Wait For Ajax


Clean Up Experiment
    [Arguments]    ${expid}
    ${listentry} =  Set Variable  id('experiment-list')//tr[.//div[@data-target='#${expid}']]
    ${delete_btn} =  Set Variable  ${listentry}//a[contains(@class,'remove-experiment-btn')]
    Navigate To Experiments
    Click Link  xpath=${delete_btn}
    ${remove_form} =  Set Variable  id('remove-dataset-confirmation-form')
    Wait Until Element is Visible  xpath=${remove_form}
    ${remove_form_btn} =  Set Variable  id('form-buttons-remove')
    Click Button  xpath=${remove_form_btn}
    Wait For Ajax
    # Do some checks
    Location should be  ${LOGIN URL}/experiments
    Page Should Not Contain Element  xpath=${listentry}

