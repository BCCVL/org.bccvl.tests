*** Settings ***

Documentation  A test suite with a single test for valid login. This test has
...            a workflow that is created using keywords from the resource file.
Resource       resource.robot
Test Setup     Open Browser To BCCVL Home
Test Teardown  Close Browser


*** Test Cases ***




#*** Keywords ***

# Works but suffers from timing issues
#   - before click to new SDM
#   - when selecting layers
Create Basic SDM
    Log in as admin
    Navigate To Experiments
    Click New SDM
    Input Text  name=form.widgets.IDublinCore.title  admin
    Input Text  name=form.widgets.IDublinCore.description  Artificial Neural Network with Koala occurrences
    Click Link  link=Configuration
    Click Element  xpath=//label/h1[contains(text(),'Artificial Neural Network')]
    Click Link  link=Occurrences
    Click Element  xpath=//label/p[contains(text(),'Koala - Mini occurrence dataset for Redland City')]
    Click Link  link=Absences
    Click Element  xpath=//label/p[contains(text(), 'Koala - Mini absence dataset for Redland City')]
    Click Link  link=Climate & Environmental Data

    Select From List By Label  id=form-widgets-resolution  30" (~1km)
    Click Element  xpath=//td[contains(text(),'Current climate layers for Redland City, 30" (~1km)')]
    Click Element  xpath=//label[contains(text(), 'B14 - Precipitation of Driest Month')]
    Click Element  xpath=//label[contains(text(), 'B15 - Precipitation Seasonality (Coefficient of Variation)')]

    Click Link  link=Run
    Wait Until Element is Visible  css=a.bccvllinks-logout
