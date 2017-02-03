*** Settings ***

Documentation  Run a simple Climate Change Experiment.
...            This will also run an SDM as base experiment.
Library        String
Library        DebugLibrary
Resource       resource.robot
Resource       experiment.robot
Suite Setup    Create Base SDM
Suite Teardown  Clean Up Base SDM
Test Setup     Open Browser To BCCVL Home
Test Teardown  Close Browser


*** Variables ***
${base_sdm_id}  ${null}


*** Test Cases ***

# Maybe just pick first (species) in list and click first download link ... fetch species name first to look up in datasets list (should be first in list)

Test CC Base
    ${newid} =  Set Variable  ${null}    

    Log in as admin
    Navigate To Experiments
    Click New CC
    # Fill in form
    Input Text  name=form.widgets.IDublinCore.title  ${TEST NAME}
    # TODO: verify input element has class valid
    Input Text  name=form.widgets.IDublinCore.description  ${TEST NAME} with Base SDM

    # Switch to next tab
    Click Next
    Select SDM Experiment
    Page Should Contain  Test Base SDM
    # Select model inside SDM
    sleep  1s
    Select Checkbox  xpath=id('form-widgets-species_distribution_models')//tr[1]/td/input

    # Switch to next tab
    Click Next
    Select Future Climate
    Page Should Contain  Climate Projection RCP2.6 based on CCCMA-CGCM31, 2.5 arcmin (~5 km) - 2015

    # Switch to next tab (constraints)
    Click Next
    # Switch to next tab (Run)
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
    Should Start With  ${newid}  test-cc-base
    # Job submitted info message
    # 1 result on page but empty (xpath count)
    Wait For Experiment State  COMPLETED
    # How many files inside result?
    ${results_table} =  Set Variable  id('bccvl-experimentresults-table')
    # Verify experiment title
    Element Should Contain  css=div.experiment-accordion-heading  ${TEST NAME}
    Element Should Contain  css=div.experiment-accordion-heading  Year: 2015
    # click accordion
    Click Element  css=#bccvl-experimentresults-table div.experiment-accordion-heading a.expand-btn
    # make sure we have 4 result files
    Locator Should Match X Times  css=#bccvl-experimentresults-table div div.row-fluid  4

    # Clean up:
    [Teardown]  Run Keyword If  '${newid}' != '${null}'  Clean Up Experiment  ${newid}


**** Keywords ***

Create Base SDM
    Open Browser To BCCVL Home
    Log in as admin
    Navigate To Experiments
    Click New SDM
    # Fill in form
    Input Text  name=form.widgets.IDublinCore.title  Test Base SDM
    # TODO: verify input element has class valid
    Input Text  name=form.widgets.IDublinCore.description  Test Base SDM with Koala occurrences

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

    # skip constraints tab
    Click Next

    # Switch to next tab
    Click Next
    # select ANN
    Click Label  Artificial Neural Network

    # Switch to next tab (constraints)
    Click Next
    # Switch to next tab (Run)
    Click Next
    Click Button  xpath=//button[@name='form.buttons.save']
    # TODO: check spinner
    Wait For Ajax

    # new page:
    ${newloc} =  Get Location
    # get new experiment id
    @{urlparts} =  Split String From Right  ${newloc}  /  2
    Set Suite Variable  ${base_sdm_id}  @{urlparts}[-2]
    # check id starts with pattern
    Should Start With  ${base_sdm_id}  test-base-sdm
    # Job submitted info message
    # 1 result on page but empty (xpath count)
    Wait For Experiment State  COMPLETED
    # How many files inside result?
    ${results_table} =  Set Variable  id('bccvl-experimentresults-table')
    # Verify experiment title
    Element Should Contain  css=div.experiment-accordion-heading  Test Base SDM
    Element Should Contain  css=div.experiment-accordion-heading  Algorithm: ann
    # click accordion
    Click Element  css=#bccvl-experimentresults-table div.experiment-accordion-heading
    # make sure we have 23 result files
    Locator Should Match X Times  css=#bccvl-experimentresults-table div div.row-fluid  23
    Close Browser


Clean Up Base SDM
    Open Browser To BCCVL Home
    Log in as admin
    Navigate To Experiments
    Run Keyword If  '${base_sdm_id}' != '${null}'  Clean Up Experiment  ${base_sdm_id}
    Close Browser
