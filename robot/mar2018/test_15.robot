*** Settings ***

Documentation  March 2018 Suite, Test 15
Library        String
Resource       ../resource.robot
Resource       ../experiment.robot
Resource       keywords.robot
Test Setup     Open Browser To BCCVL Home
Test Teardown  Close Browser
Test Timeout   1 minute

*** Test Cases ***

Test 15 - Biodiverse
    ${newid} =  Set Variable  ${null}

    Log in as admin
    Navigate To Experiments
    Click New BD

    # Experiment Details Tab
    Input Text  name=form.widgets.IDublinCore.title  ${TEST NAME}
    # TODO: verify input element has class valid
    Input Text  name=form.widgets.IDublinCore.description  ${TEST NAME} using MSDM Baseline Test
    # Switch to next tab
    Click Next

    # Source Experiment Tab
    #Select SDM From Modal  Koala, VAST, All algorithms
    #Page Should Contain  Koala, VAST, All algorithms

    Select MSDM From Modal  Test 8 - MSDM
    Page Should Contain  Test 8 - MSDM
    Click Link  css=.select-all
    # Switch to next tab
    Click Next

    # Configuration Tab
    # use default
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
    Should Start With  ${newid}  test-15-biodiverse

    # confirm experiment was started successfully
    Wait For Experiment State  QUEUED
    # confirm experiment scheduled the right number of results
    Page Should Contain Element  css=#bccvl-experimentresults-table div.experiment-accordion-heading  limit=1

    # Clean up:
    #[Teardown]  SDM Teardown  ${newid}

