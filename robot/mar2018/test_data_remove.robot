*** Settings ***

Documentation  March 2018 Suite, Teardown and remove data
Library        String
Resource       ../resource.robot
Resource       ../experiment.robot
Resource       keywords.robot
Test Setup     Open Browser To BCCVL Home
Test Teardown  Close Browser
Test Timeout   5 minutes

*** Keywords ***

Delete Dataset
    #remove dataset
    Click Link  css=a.remove-dataset-btn
    sleep  2s
    Wait Until Element Is Visible  id=remove-modal
    Click Element  id=form-buttons-remove
    Wait For Ajax

Remove Dataset
    [Arguments]  ${keywords}
    #ensure input is empty
    Clear Element Text  id=c13
    Click Element  id=c13_button
    Sleep  2s
    #search for dataset
    Input Text  id=c13  ${keywords}
    Click Element  id=c13_button
    sleep  2s

    # this hangs for some reason, no logic to in the report
    ${datasetexists}=  Run Keyword And Return Status  Element Should Be Visible  css=a.remove-dataset-btn
    Run Keyword If  ${datasetexists}  Delete Dataset
    Wait Until Element Is Visible  id=c13

Remove Experiment
    [Arguments]  ${keywords}
    Click Link  xpath=id('experiment-list')//td[@class="bccvl-table-controls"]//a[@data-friendlyname='removing_${keywords}']
    sleep  2s
    Wait Until Element Is Visible  id=remove-modal
    Click Element  id=form-buttons-remove
    Wait For Ajax


*** Test Cases ***

Remove Test Datasets
    Log in as admin
    Navigate to Datasets

    @{datasets} =  Create List  Egernia Eucalyptus Rhinella Background Absences  Egernia Eucalyptus Rhinella Occurrences  Monarch Butterfly Occurrences  Egernia Reduced Background Absences  Egernia Occurrences

    :FOR  ${keywords}  IN  @{datasets}
    # Enter search term
    \  Remove Dataset  ${keywords}


Remove Test Experiments
    Log in as admin
    Navigate to Experiments

    @{experiments} =  Create List  Test 1 - SDM baseline  Test 2 - SDM absence settings  Test 3 - SDM true absences  Test 4 - SDM convex and buffer  Test 5 - SDM predefined regions  Test 6 - SDM environmental env  Test 7 - SDM shapefile  Test 8 - MSDM  Test 9 - MSDM true absences  Test 10 - MSDM convex and buffer  Test 11 - MSDM predefined regions  Test 12 - MSDM shapefile  Test 13 - Migratory  Test 14 - Climate Change  Test 15 - Biodiverse

    :FOR  ${keywords}  IN  @{experiments}
    # Enter search term
    \  Remove Experiment  ${keywords}





