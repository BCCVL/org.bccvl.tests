*** Settings ***

Documentation  March 2018 Suite, Test 5
Library        String
Resource       ../resource.robot
Resource       ../experiment.robot
Resource       keywords.robot
Test Setup     Open Browser To BCCVL Home
Test Teardown  Close Browser
Test Timeout   1 minute

*** Test Cases ***

# Maybe just pick first (species) in list and click first download link ... fetch species name first to look up in datasets list (should be first in list)
Test 5 - SDM predefined regions
    ${newid} =  Set Variable  ${null}

    Log in as admin
    Navigate To Experiments
    Click New SDM

    # Experiment Details Tab
    Input Text  name=form.widgets.IDublinCore.title  ${TEST NAME}
    # TODO: verify input element has class valid
    Input Text  name=form.widgets.IDublinCore.description  ${TEST NAME} with Egernia occurrences
    # Switch to next tab
    Click Next

    # Occurrences Tab
    Select Occurrences From Modal  Egernia Occurrences
    Page Should Contain  Egernia Occurrences
    # Switch to next tab
    Click Next

    # Absences Tab
    # No absences, default settings
    Click Next

    # Environmental Tab
    Select Environmental Dataset From Modal  Australia, current climate 1976-2005
    Page Should Contain  Australia, current climate (1976-2005), 30 arcsec (~1 km)
    Click Link  link=Select None
    Click Label  B01 - Annual Mean Temperature
    Click Label  B14 - Precipitation of Driest Month
    Click Label  B15 - Precipitation Seasonality (Coefficient of Variation)
    Click Next

    # Constraints tab
    Click Element  id=region_no_offset
    Click Element  css=.selectize-control.select-region-type.single
    Select From Selectize Single  .selectize-control.select-region-type.single  Australian States and Territories
    Wait For Ajax
    @{inputs} =  Create List  Victoria  New South Wales
    Select From Selectize Multi  .selectize-control.select-region.multi  @{inputs}

    Click Next

    # Algorithms tab
    # select all algorithms
    Click Label  Classification Tree
    Click Label  Generalized Linear Model
    Click Next

    Click Button  name=form.buttons.save
    # Check element instead of waiting for Ajax
    Wait Until Page Contains Element  css=section.bccvl-experimentresults

    # new page:
    ${newloc} =  Get Location
    # get new experiment id
    @{urlparts} =  Split String From Right  ${newloc}  /  2
    ${newid} =  Set Variable  @{urlparts}[-2]
    # check id starts with pattern
    Should Start With  ${newid}  test-5-sdm-predefined-regions

    # confirm experiment was started successfully
    Wait For Experiment State  QUEUED
    # confirm experiment scheduled the right number of results
    Locator Should Match X Times  css=#bccvl-experimentresults-table div.experiment-accordion-heading  2

    # How many files inside result?
    #${results_table} =  Set Variable  id('bccvl-experimentresults-table')
    # Verify experiment title
    #Element Should Contain  css=div.experiment-accordion-heading  ${TEST NAME}
    # click accordion
    #Click Element  css=#bccvl-experimentresults-table div.experiment-accordion-heading a.expand-btn
    # make sure we have 23 result files
    #Locator Should Match X Times  css=#bccvl-experimentresults-table div div.row-fluid  23

    # Clean up:
    #[Teardown]  SDM Teardown  ${newid}
    Close Browser
