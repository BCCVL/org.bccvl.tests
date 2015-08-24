*** Settings ***

Documentation  A test suite with a single test for valid login. This test has
...            a workflow that is created using keywords from the resource file.
Library        String
Library        DebugLibrary
Resource       resource.robot
Resource       experiment.robot
Test Setup     Open Browser To BCCVL Home
Test Teardown  Close Browser


*** Test Cases ***

# Maybe just pick first (species) in list and click first download link ... fetch species name first to look up in datasets list (should be first in list)
Test ANN 1km
    Log in as admin
    Navigate To Experiments
    Click New SDM
    # Fill in form
    Input Text  name=form.widgets.IDublinCore.title  ${TEST NAME}
    # TODO: verify input element has class valid
    Input Text  name=form.widgets.IDublinCore.description  ${TEST NAME} with Koala occurrences

    # Switch to next tab
    Click Next
    Select Occurrence Dataset
    Page Should Contain  Koala - Mini occurrence dataset for Redland City

    # Switch to next tab
    Click Next
    Select Absence Dataset
    Page Should Contain  Koala - Mini absence dataset for Redland City
    
    # Switch to next tab
    Click Next
    Select Environmental Dataset
    Page Should Contain  Current climate layers for Redland City, 30" (~1km)
    Click Link  link=Select None
    Click Label  B14 - Precipitation of Driest Month
    
    # Switch to next tab
    Click Next
    # select ANN
    Click Label  Artificial Neural Network
    
    # Switch to next tab
    Click Next
    Click Button  xpath=//button[@name='form.buttons.save']
    # TODO: check spinner
    Wait For Ajax

    # new page:
    Location Should Be  ${LOGIN URL}/experiments/test-ann-1km/view
    # Job submitted info message
    # 1 result on page but empty (xpath count)
    Wait For Experiment State  COMPLETED
    # How many files inside result?
    ${results_table} =  Set Variable  id('bccvl-experimentresults-table')
    # Verify experiment title
    Element Should Contain  css=div.experiment-accordion-heading  ${TEST NAME}
    Element Should Contain  css=div.experiment-accordion-heading  Algorithm: ann
    # click accordion
    Click Element  css=#bccvl-experimentresults-table div.experiment-accordion-heading a.expand-btn
    # make sure we have 14 result files
    Locator Should Match X Times  css=#bccvl-experimentresults-table div div.row-fluid  13
    
    # Clean up:
    Clean Up Experiment  test-ann-1km



**** Keywords ***

Click Label
    [Arguments]    ${label}    ${index}=1
    [Documentation]    Clicks label element which contains text ${label}.
    ...    If there is more than one label with given text, specify index to match those labels.
    Click Element    xpath=(//label[contains(., '${label}')])[${index}]

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
    

Clean Up Experiment
    [Arguments]    ${expid}
    ${listentry} =  Set Variable  id('experiment-list')//tr[.//div[@data-target='#${expid}']]
    ${delete_btn} =  Set Variable  ${listentry}//a[contains(@class,'remove-experiment-btn')]
    ${modal_remove_form} =  Set Variable  id('remove-dataset-confirmation-form')
    Navigate To Experiments
    Click Link  xpath=${delete_btn}
    Wait Until Page Contains Element  xpath=${modal_remove_form}
    Wait Until Element is Visible  xpath=${modal_remove_form}
    ${remove_form_btn} =  Set Variable  id('form-buttons-remove')
    Click Button  xpath=${remove_form_btn}
    Wait For Ajax
    # Do some checks
    Location should be  ${LOGIN URL}/experiments
    Page Should Not Contain Element  xpath=${listentry}
