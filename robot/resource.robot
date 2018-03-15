*** Settings ***

Documentation  A resource file containing the application specific keywords
...            that create our own domain specific language. This resource
...            implements keywords for testing HTML version of the test
...            application.
Library        SeleniumLibrary


*** Variables ***

#${SERVER}        192.168.100.200:443
${SERVER}        %{BCCVL_TEST_SERVER}
${BROWSER}       Firefox
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
# TODO: work around a bug in geckodriver ... we have to click the element inside
#       the a tag (in case it is a block element)
#    Click Link  css=a.bccvllinks-login
    Click Element  css=a.bccvllinks-login div
    Title Should Be  BCCVL

Navigate To Datasets
    Click Link  link=Datasets
    Wait Until Element is Visible  link=Search Datasets
    Click Link  link=Search Datasets

Navigate To Experiments
    Click Link  link=Experiments

Navigate To Knowledgebase
    Click Link  link=Support

Click New SDM
    Click Link  css=a.bccvllinks-experiment-new

Click New MSDM
    Click Link  css=a.bccvllinks-experiment-msdm-new

Click New MM
    Click Link  css=a.bccvllinks-experiment-mme-new

Click New CC
    Click Link  css=a.bccvllinks-experiment-proj-new

Click New BD
    Click Link  css=a.bccvllinks-experiment-biodiverse-new

Click Import Dataset
# TODO: this is another workaround a bug in geckodriver failing no locate
#       a link by text
#    Click Link  link=Get Species Data
    Click Element  css=li.tab-datasetsimport a

Click Next
    sleep  1s
    Click Button  css=button.bccvl-wizardtabs-next

Click Label
    [Arguments]    ${label}    ${index}=1
    [Documentation]    Clicks label element which contains text ${label}.
    ...    If there is more than one label with given text, specify index to match those labels.
    Execute Javascript  window.document.evaluate("//label[contains(., '${label}')]", document, null, XPathResult.FIRST_ORDERED_NODE_TYPE, null).singleNodeValue.scrollIntoView()

    Click Element    xpath=(//label[contains(., '${label}')])[${index}]

Log in as admin
    Navigate To Login Page
    sleep  1s
    Wait Until Element is Visible  id=__ac_name
    Input Text  id=__ac_name  ${ADMIN USER}
    Input Password  id=__ac_password  ${ADMIN PASS}
    Select Checkbox  id=legals-checkbox-site
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
    sleep  1s
    Wait for Condition   return !!window.jQuery && window.jQuery.active == 0;

Experiment State Should Be
    [Arguments]  ${state}
    [Documentation]  Compare overall experiment state to parameter
    ...              Keyword succedds if state is the same otherwise fails
    ${exp_state} =  Get Element Attribute  css=div.bccvl-expstatus  attribute=data-status
    Should Be Equal  ${exp_state}  ${state}

Wait For Experiment State
    [Arguments]  ${state}
    [Documentation]  Wait until experiment state matches argument
    Wait Until Keyword Succeeds  5 min  5 sec  Experiment State Should Be  ${state}


Select From Selectize Single
    [Arguments]  ${element}  ${input}
    [Documentation]  Select item in Selectize widget

    # Enter search term
    Click Element  css=${element}
    Input Text  css=${element} input  ${input}
    Sleep  2s
    Press Key   css=${element} input  \\13


Select From Selectize Multi
    [Arguments]  ${element}  @{inputs}
    [Documentation]  Select item in Selectize widget
    
    :FOR  ${input}  IN  @{inputs}
    # Enter search term
    \  Click Element  css=${element}
    \  Input Text  css=${element} input  ${input}
    \  Sleep  1s
    \  Press Key   css=${element} input  \\13

    
