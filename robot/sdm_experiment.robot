*** Settings ***

Documentation  Run some SDM experiments.
Library        String
# Library        DebugLibrary
Resource       resource.robot
Resource       experiment.robot
Test Setup     Open Browser To BCCVL Home
Test Teardown  Close Browser


*** Test Cases ***

# Maybe just pick first (species) in list and click first download link ... fetch species name first to look up in datasets list (should be first in list)
Test ANN 1km
    ${newid} =  Set Variable  ${null}

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
    # yes we have absences
    Select Radio Button  group_name=if_absence  value=yes
    sleep  0.5s
    Select Absence Dataset
    Page Should Contain  Koala - Mini absence dataset for Redland City

    # Switch to next tab
    Click Next
    Select Environmental Dataset
    Page Should Contain  Current climate layers for Redland City, 30\" (~1km)
    Click Link  link=Select None
    Click Label  B14 - Precipitation of Driest Month
    Click Label  B13 - Precipitation of Wettest Month

    # skip constraints tab
    Click Next

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
    ${newloc} =  Get Location
    # get new experiment id
    @{urlparts} =  Split String From Right  ${newloc}  /  2
    ${newid} =  Set Variable  @{urlparts}[-2]
    # check id starts with pattern
    Should Start With  ${newid}  test-ann-1km
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
    # make sure we have 23 result files
    Locator Should Match X Times  css=#bccvl-experimentresults-table div div.row-fluid  23

    # Clean up:
    [Teardown]  SDM Teardown  ${newid}



**** Keywords ***
SDM Teardown
    [Arguments]  ${expid}
    Run Keyword If  '${expid}' != '${null}'  Clean Up Experiment  ${expid}
    Close Browser
