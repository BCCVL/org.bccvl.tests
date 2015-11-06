*** Settings ***

Documentation  A resource file containing the application specific keywords
...            that create our own domain specific language. This resource
...            implements keywords for testing HTML version of the test
...            application.
Library        Selenium2Library

*** Keywords ***

Select Occurrence Dataset
    ${field} =  Set Variable  species_occurrence_dataset
    ${search} =  Set Variable  \#${field}-modal div.section-search
    
    Click Link  id=${field}-popup
    Wait Until Element Is Visible  id=${field}-modal
    Input Text   css=${search} input  Redland
    Click Button  css=${search} button
    Wait For Ajax
    # Select dataset
    Click Element  xpath=id('${field}-modal')//div[contains(@class,'datasets-list-entry')]
    # Click Save Changes
    Click Button  css=\#${field}-modal button.btn-primary
    Wait For Ajax

Select Absence Dataset
    ${field} =  Set Variable  species_absence_dataset
    ${search} =  Set Variable  \#${field}-modal div.section-search

    Click Link  id=${field}-popup
    Wait Until Element Is Visible  id=${field}-modal
    Input Text   css=${search} input  Redland
    Click Button  css=${search} button
    Wait For Ajax
    # Select dataset
    Click Element  xpath=id('${field}-modal')//div[contains(@class,'datasets-list-entry')]
    # Click Save Changes
    Click Button  css=\#${field}-modal button.btn-primary
    Wait For Ajax

Select Environmental Dataset
    ${field} =  Set Variable  environmental_datasets
    ${search} =  Set Variable  \#${field}-modal div.section-search

    Click Link  id=${field}-popup
    Wait Until Element Is Visible  id=${field}-modal
    Input Text   css=${search} input  Redland
    Click Button  css=${search} button
    Wait For Ajax
    # Select dataset
    Click Element  xpath=id('${field}-modal')//div[contains(@class,'datasets-list-entry')]
    # Click Save Changes
    Click Button  css=\#${field}-modal button.btn-primary
    Wait For Ajax

Select SDM Experiment
    ${field} =  Set Variable  species_distribution_models
    ${search} =  Set Variable  \#${field}-modal div.section-search
    
    Click Link  id=${field}-popup
    Wait Until Element Is Visible  id=${field}-modal
    Input Text  css=${search} input  Base SDM
    Click Button  css=${search} button
    Wait For Ajax
    # Select SDM
    Click Element  xpath=id('${field}-modal')//div[contains(@class,'datasets-list-entry')]
    # Click Select Experiment
    Click Button  css=\#${field}-modal button.btn-primary
    Wait For Ajax

Select Future Climate
    ${field} =  Set Variable  future_climate_datasets
    ${search} =  Set Variable  \#${field}-modal div.section-search

    Click Link  id=${field}-popup
    Wait Until Element Is Visible  id=${field}-modal
    Input Text  css=${search} input  RCP3PD CCCMA-CGCM31
    Click Button  css=${search} button
    Wait For Ajax
    # Select Future Datasets
    Click Element  xpath=id('${field}-modal')//div[contains(@class,'datasets-list-entry') and contains(string(.), '(~5km) - 2015')]
    # Click Select Experiment
    Click Button  css=\#${field}-modal button.btn-primary
    Wait For Ajax


Clean Up Experiment
    [Arguments]    ${expid}
    ${listentry} =  Set Variable  id('experiment-list')//tr[.//div[@data-target='#${expid}']]
    ${delete_btn} =  Set Variable  ${listentry}//a[contains(@class,'remove-experiment-btn')]
    ${modal_remove_btn} =  Set Variable  id('form-buttons-remove')
    Navigate To Experiments
    Click Link  xpath=${delete_btn}
    Wait For Ajax
    Wait Until Page Contains Element  xpath=${modal_remove_btn}    
    Wait Until Element is Visible  xpath=${modal_remove_btn}
    Click Button  xpath=${modal_remove_btn}
    Wait For Ajax
    # Do some checks
    Location should be  ${LOGIN URL}/experiments
    Page Should Not Contain Element  xpath=${listentry}

