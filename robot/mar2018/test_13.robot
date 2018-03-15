*** Settings ***

Documentation  March 2018 Suite, Test 13
Library        String
Resource       ../resource.robot
Resource       ../experiment.robot
Resource       keywords.robot
Test Setup     Open Browser To BCCVL Home
Test Teardown  Close Browser
Test Timeout   1 minute

*** Test Cases ***

Test 13 - Migratory
    ${newid} =  Set Variable  ${null}

    Log in as admin
    Navigate To Experiments
    Click New MM

    # Experiment Details Tab
    Input Text  name=form.widgets.IDublinCore.title  ${TEST NAME}
    # TODO: verify input element has class valid
    Input Text  name=form.widgets.IDublinCore.description  ${TEST NAME} with Monarch Butterfly
    # Switch to next tab
    Click Next

    # Occurrences Tab
    Select Occurrences From Modal  Butterfly Occurrences
    Page Should Contain  Monarch Butterfly Occurrences
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
    # use default (convexhull)
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
    Should Start With  ${newid}  test-13-migratory

    # confirm experiment was started successfully
    Wait For Experiment State  QUEUED
    # confirm experiment scheduled the right number of results
    Locator Should Match X Times  css=#bccvl-experimentresults-table div.experiment-accordion-heading  2

    # Clean up:
    #[Teardown]  SDM Teardown  ${newid}
    Close Browser
