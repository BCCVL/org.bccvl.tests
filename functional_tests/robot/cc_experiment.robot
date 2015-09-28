*** Settings ***

Documentation  A test suite with a single test for valid login. This test has
...            a workflow that is created using keywords from the resource file.
Library        String
Library        DebugLibrary
Resource       resource.robot
Resource       experiment.robot
Suite Setup    Create Base SDM
Suite Teardown  Clean Up Base SDM
Test Setup     Open Browser To BCCVL Home
Test Teardown  Close Browser


*** Test Cases ***

# Maybe just pick first (species) in list and click first download link ... fetch species name first to look up in datasets list (should be first in list)

Test CC Base
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
    Select Checkbox  xpath=id('form-widgets-species_distribution_models')//tr[1]/td/input

    # Switch to next tab
    Click Next
    Select Future Climate
    Page Should Contain  Climate Projection RCP3PD based on CCCMA-CGCM31, 2.5arcmin (~5km) - 2015

    # Switch to next tab
    Click Next
    Click Button  xpath=//button[@name='form.buttons.save']
    # TODO: check spinner
    Wait For Ajax

    # new page:
    Location Should Be  ${LOGIN URL}/experiments/test-cc-base/view
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
    # make sure we have 14 result files
    Locator Should Match X Times  css=#bccvl-experimentresults-table div div.row-fluid  5
    
    # Clean up:
    Clean Up Experiment  test-cc-base


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
    Location Should Be  ${LOGIN URL}/experiments/test-base-sdm/view
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
    # make sure we have 14 result files
    Locator Should Match X Times  css=#bccvl-experimentresults-table div div.row-fluid  12
    Close Browser
    

Clean Up Base SDM
    Open Browser To BCCVL Home
    Log in as admin
    Navigate To Experiments
    Clean Up Experiment  test-base-sdm
    Close Browser