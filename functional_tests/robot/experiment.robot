*** Settings ***

Documentation  A resource file containing the application specific keywords
...            that create our own domain specific language. This resource
...            implements keywords for testing HTML version of the test
...            application.
Library        Selenium2Library
Library        OperatingSystem
Library        Process

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

Get Result Link
    [Arguments]    ${friendlyName}
    [Documentation]    Return the associated link

    ${link} =  Get Element Attribute  xpath=//a[@data-friendlyname=${friendlyName}]@href
    Return From Keyword  ${link}

Set Algorithm Parameter Random Seed
    [Arguments]    ${algorithm}    ${value}
    [Documentation]    Set the algorithm parameter to the value specified.

    ${algid} =  Get Element Attribute  //a[contains(string(.), '${algorithm}')]/ancestor::div[@class='accordion-group']@data-function
    Input Text  form.widgets.${algid}.random_seed  ${value}

Verify Result
    [Arguments]    ${link}    ${md5}
    [Documentation]    Verify that the result has a matching md5 signature.

    # Get cookie
    ${value} =  Get Cookie Value  __ac
    ${cookie} =  Set Variable  __ac=${value.strip('"')}

    # Download the result file and return its md5 signature
    Run Process  curl  -k  -L  -b  ${cookie}  ${link}  |  md5sum.exe  |  cut  -d  ${SPACE}  -f1  shell=true  alias=myproc
    ${result} =  Get Process Result  myproc

    #Log To Console  md5:${result.stdout}
    Should Be Equal  ${result.stdout}  ${md5}

Use Pseudo Absence Points
    Click Link  Use Pseudo Absence Points.
    Click Label  Pseudo absence points

Use Absence Dataset
    Select Absence Dataset
    Page Should Contain  Koala - Mini absence dataset for Redland City
