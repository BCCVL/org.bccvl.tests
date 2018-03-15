*** Settings ***

Documentation  March 2018 Suite, Test 11
Library        String
Resource       ../resource.robot
Resource       ../experiment.robot
Resource       keywords.robot
Test Setup     Open Browser To BCCVL Home
Test Teardown  Close Browser
Test Timeout   1 minute

*** Test Cases ***

Test 11 - MSDM predefined regions
    ${newid} =  Set Variable  ${null}

    Log in as admin
    Navigate To Experiments
    Click New MSDM

    # Experiment Details Tab
    Input Text  name=form.widgets.IDublinCore.title  ${TEST NAME}
    # TODO: verify input element has class valid
    Input Text  name=form.widgets.IDublinCore.description  ${TEST NAME} with Egernia, Eucalyptus, Rhinella
    # Switch to next tab
    Click Next

    # Occurrences Tab
    Select Multi Occurrence Dataset From Modal  Egernia Eucalyptus Rhinella Occurrence
    Page Should Contain  Egernia Eucalyptus Rhinella Occurrences
    Click Link  css=a.select-all
    # Switch to next tab
    Click Next

    # Absences Tab
    # No absences, default settings
    Click Next

    # Environmental Tab
    Select Environmental Dataset From Modal  Australia, current climate 1976-2005
    Page Should Contain  Australia, current climate (1976-2005), 30 arcsec (~1 km)
    Click Link  css=#form-widgets-environmental_datasets a.select-none
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
    Click Label  Generalized Linear Model
    Click Next

    # Click Button  name=form.buttons.save
    # Check element instead of waiting for Ajax
    Wait Until Page Contains Element  css=section.bccvl-experimentresults

    # new page:
    ${newloc} =  Get Location
    # get new experiment id
    @{urlparts} =  Split String From Right  ${newloc}  /  2
    ${newid} =  Set Variable  @{urlparts}[-2]
    # check id starts with pattern
    Should Start With  ${newid}  test-11-msdm-predefined-regions

    # confirm experiment was started successfully
    Wait For Experiment State  QUEUED
    # confirm experiment scheduled the right number of results
    Locator Should Match X Times  css=#bccvl-experimentresults-table div.experiment-accordion-heading  2

    # Clean up:
    #[Teardown]  SDM Teardown  ${newid}

