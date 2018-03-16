*** Settings ***

Documentation  March 2018 Suite, Test 14
Library        String
Resource       ../resource.robot
Resource       ../experiment.robot
Resource       keywords.robot
Test Setup     Open Browser To BCCVL Home
Test Teardown  Close Browser
Test Timeout   1 minute

*** Test Cases ***

Test 14 - Climate Change
    ${newid} =  Set Variable  ${null}

    Log in as admin
    Navigate To Experiments
    Click New CC

    # Experiment Details Tab
    Input Text  name=form.widgets.IDublinCore.title  ${TEST NAME}
    # TODO: verify input element has class valid
    Input Text  name=form.widgets.IDublinCore.description  ${TEST NAME} using SDM Baseline Test
    # Switch to next tab
    Click Next

    # Source Experiment Tab
    #Select SDM From Modal  Koala, VAST, All algorithms
    #Page Should Contain  Koala, VAST, All algorithms

    Select SDM From Modal  Test 1 - SDM baseline
    Page Should Contain  Test 1 - SDM baseline
    Click Link  css=.select-all
    # Switch to next tab
    Click Next

    # Projection Tab
    #${keywords} =  Set Variable  Australia, climate projection RCP8.5 based on CSIRO-MK30, 30 arcsec (~1 km) - 2085
    #Select Future Climate Dataset From Modal  ${keywords}  RCP8.5  2085  CSIRO Mark 3.0
    #Page Should Contain  Australia, climate projection RCP8.5 based on CSIRO-MK30, 30 arcsec (~1 km) - 2085

    ${keywords} =  Set Variable  Australia, Climate Projection RCP8.5 based on CSIRO-MK30, 2.5 arcmin (~5 km) - 2085
    Select Future Climate Dataset From Modal  ${keywords}  RCP8.5  2085  CSIRO Mark 3.0
    Page Should Contain  Australia, Climate Projection RCP8.5 based on CSIRO-MK30, 2.5 arcmin (~5 km) - 2085
    Click Next

    # Constraints tab
    # use default (convexhull)
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
    Should Start With  ${newid}  test-14-climate-change

    # confirm experiment was started successfully
    Wait For Experiment State  QUEUED
    # confirm experiment scheduled the right number of results
    Page Should Contain Element  css=#bccvl-experimentresults-table div.experiment-accordion-heading  limit=1

    # Clean up:
    #[Teardown]  SDM Teardown  ${newid}

