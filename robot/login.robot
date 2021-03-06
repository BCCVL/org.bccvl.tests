*** Settings ***

Documentation  A test suite with a single test for valid login. This test has
...            a workflow that is created using keywords from the resource file.
Resource       resource.robot
Test Setup     Open Browser To BCCVL Home
Test Teardown  Close Browser


*** Test Cases ***

Log in out
    Should be logged out
    Log in as admin
    Should be logged in as admin
    Logout

Test Logout
    Log in as admin
    Should be logged in as admin
    Logout
    Should be logged out

Test Datasets page
    Log in as admin
    Navigate To Datasets
    Title Should Be  BCCVL Datasets

Test Experiments page
    Log in as admin
    Navigate To Experiments
    Title Should Be  BCCVL Experiment List

Test Knowledge page
    Log in as admin
    Navigate To Knowledgebase
    ${cur_window} =  Wait Until Keyword Succeeds  30 sec  5 sec  Select Window   url=https://support.bccvl.org.au/support/home
    Title Should Be  Support : BCCVL
    Close Window
