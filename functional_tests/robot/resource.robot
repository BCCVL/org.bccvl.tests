*** Settings ***

Documentation  A resource file containing the application specific keywords
...            that create our own domain specific language. This resource
...            implements keywords for testing HTML version of the test
...            application.
Library        Selenium2Library

*** Variables ***

#${SERVER}        192.168.100.200:443
${SERVER}        %{BCCVL_TEST_SERVER}
${BROWSER}       firefox
${DELAY}         0
${VALID USER}    demo
${VALID PASSWD}  mode
${LOGIN URL}     https://${SERVER}
${DATASETS URL}  https://${SERVER}/datasets
${WELCOME URL}   https://${SERVER}/html/welcome.html
${ERROR URL}     https://${SERVER}/html/error.html
${ADMIN NAME}    %{BCCVL_TEST_USERNAME}
${ADMIN USER}    %{BCCVL_TEST_USER}
${ADMIN PASS}    %{BCCVL_TEST_PASS}


*** Keywords ***

Open Browser To BCCVL Home
    Open Browser  ${LOGIN_URL}  ${BROWSER}
#    Maximize Browser Window
    Set Window Size  ${1200}  ${800}
    Set Selenium Speed  ${DELAY}
    Set Selenium Implicit Wait  ${30}
    Set Selenium Timeout  ${30}
    Title Should Be  BCCVL Home

Should be logged out
    Element Should Contain  css=a.bccvllinks-login   Log in

Should be logged in as admin
    Element Should Contain  css=#user-menu .bccvl-username  ${ADMIN NAME}

Navigate To Login Page
    Click Element  css=a.bccvllinks-login
    Title Should Be  BCCVL Login

Navigate To Datasets
    Click Link  link=Datasets
    Wait Until Element is Visible  link=Search Datasets
    Click Link  link=Search Datasets

Navigate To Experiments
    Click Link  link=Experiments

Navigate To Knowledgebase
    Click Link  link=Knowledge Base

Click New SDM
    Click Link  css=a.bccvllinks-experiment-new

Click New CC
    Click Link  css=a.bccvllinks-experiment-proj-new

Click Import Dataset
    Click Link  link=Import Species Data

Click Next
    Click Button  css=button.btn.bccvl-wizardtabs-next

Click Label
    [Arguments]    ${label}    ${index}=1
    [Documentation]    Clicks label element which contains text ${label}.
    ...    If there is more than one label with given text, specify index to match those labels.
    Click Element    xpath=(//label[contains(., '${label}')])[${index}]

Log in as admin
    Navigate To Login Page
    Click Element  id=login-basic
    Wait Until Element is Visible  id=__ac_name
    Input Text  id=__ac_name  ${ADMIN USER}
    Input Password  id=__ac_password  ${ADMIN PASS}
    Select Checkbox  id=legals-checkbox
    Click Element  css=input.btn-success


Logout
    Click Element  css=#user-menu .bccvl-username
    Wait Until Element is Visible  css=a.bccvllinks-logout
    Click Element  css=a.bccvllinks-logout

# Log in failed
#     # url: /login_form
#     <div class="alert alert-error">
#         <button type="button" class="close" data-dismiss="alert">×</button>
#         <strong>Login failed. Both login name and password are case sensitive, check that caps lock is not enabled.</strong>
#     </div>

Wait For Ajax
    Wait for Condition   return !!window.jQuery && window.jQuery.active == 0;

Experiment State Should Be
    [Arguments]  ${state}
    [Documentation]  Compare overall experiment state to parameter
    ...              Keyword succedds if state is the same otherwise fails
    ${exp_state} =  Get Element Attribute  css=div.bccvl-expstatus@data-status
    Should Be Equal  ${exp_state}  ${state}

Wait For Experiment State
    [Arguments]  ${state}
    [Documentation]  Wait until experiment state matches argument
    Wait Until Keyword Succeeds  5 min  5 sec  Experiment State Should Be  ${state}
