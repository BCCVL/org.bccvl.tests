*** Settings ***

Documentation  A resource file containing the application specific keywords
...            that create our own domain specific language. This resource
...            implements keywords for testing HTML version of the test
...            application.
Library        SeleniumLibrary

*** Keywords ***

SDM Teardown
    [Arguments]  ${expid}
    Run Keyword If  '${expid}' != '${null}'  Clean Up Experiment  ${expid}
    Close Browser
    
Select Occurrences From Modal
    [Arguments]  ${datasetname}
    ${field} =  Set Variable  species_occurrence_dataset
    ${search} =  Set Variable  \#${field}-modal div.section-search

    Click Link  id=${field}-popup
    sleep  2s
    Wait Until Element Is Visible  id=${field}-modal
    Wait For Ajax
    Input Text   css=${search} input  ${datasetname}
    Click Button  css=${search} button
    Wait For Ajax
    # Select dataset
    Click Element  xpath=id('${field}-modal')//div[contains(@class,'datasets-list-entry')]
    # Click Save Changes
    Click Button  css=\#${field}-modal button.btn-primary
    Wait For Ajax

Select Multi Occurrence Dataset From Modal
    [Arguments]  ${datasetname}
    ${field} =  Set Variable  species_occurrence_collections
    ${search} =  Set Variable  \#${field}-modal div.section-search

    Click Link  id=${field}-popup
    sleep  2s
    Wait Until Element Is Visible  id=${field}-modal
    Wait For Ajax
    Input Text   css=${search} input  ${datasetname}
    Click Button  css=${search} button
    Wait For Ajax
    # Select dataset
    Click Element  xpath=id('${field}-modal')//div[contains(@class,'datasets-list-entry')]
    # Click Save Changes
    Click Button  css=\#${field}-modal button.btn-primary
    Wait For Ajax

Select Absence Dataset From Modal
    [Arguments]  ${datasetname}
    ${field} =  Set Variable  species_absence_dataset
    ${search} =  Set Variable  \#${field}-modal div.section-search

    Click Element  id=have_absence
    Click Link  id=${field}-popup
    sleep  2s
    Wait Until Element Is Visible  id=${field}-modal
    Wait For Ajax
    Input Text   css=${search} input  ${datasetname}
    Click Button  css=${search} button
    Wait For Ajax
    # Select dataset
    Click Element  xpath=id('${field}-modal')//div[contains(@class,'datasets-list-entry')]
    # Click Save Changes
    Click Button  css=\#${field}-modal button.btn-primary
    Wait For Ajax

Select Multi Absence Dataset From Modal
    [Arguments]  ${datasetname}
    ${field} =  Set Variable  species_absence_collection
    ${search} =  Set Variable  \#${field}-modal div.section-search

    Click Element  id=have_absence
    Click Link  id=${field}-popup
    sleep  2s
    Wait Until Element Is Visible  id=${field}-modal
    Wait For Ajax
    Input Text   css=${search} input  ${datasetname}
    Click Button  css=${search} button
    Wait For Ajax
    # Select dataset
    Click Element  xpath=id('${field}-modal')//div[contains(@class,'datasets-list-entry')]
    # Click Save Changes
    Click Button  css=\#${field}-modal button.btn-primary
    Wait For Ajax

Select Environmental Dataset From Modal
    [Arguments]  ${datasetname}
    ${field} =  Set Variable  environmental_datasets
    ${search} =  Set Variable  \#${field}-modal div.section-search
    ${summary} =  Set Variable  \#${field}-modal div.section-summary

    Click Link  id=${field}-popup
    sleep  1s
    Wait Until Element Is Visible  id=${field}-modal
    Wait Until Element Is Visible  id=datasets-popup-result-list
    Wait For Ajax
    Unselect Checkbox  css=${summary} input
    Wait For Ajax
    Input Text   css=${search} input  ${datasetname}
    Click Button  css=${search} button
    Wait For Ajax
    # Select dataset
    Click Element  xpath=id('${field}-modal')//div[contains(@class,'datasets-list-entry')]
    # Click Save Changes
    Click Button  css=\#${field}-modal button.btn-primary
    Wait For Ajax