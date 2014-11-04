*** Settings ***

Documentation  A resource file containing the application specific keywords
...            that create our own domain specific language. This resource
...            implements keywords for testing HTML version of the test
...            application.
Library        Selenium2Library

*** Variables ***

${SERVER}        192.168.100.200:443
${BROWSER}       firefox
${DELAY}         0
${VALID USER}    demo
${VALID PASSWD}  mode
${LOGIN URL}     https://${SERVER}/
${WELCOME URL}   https://${SERVER}/html/welcome.html
${ERROR URL}     https://${SERVER}/html/error.html


*** Keywords ***

Open Browser To BCCVL Home
    Open Browser  ${LOGIN_URL}  ${BROWSER}
#    Maximize Browser Window
    Set Window Size  ${1200}  ${800}
    Set Selenium Speed  ${DELAY}
    Set Selenium Implicit Wait  ${15}
    Set Selenium Timeout  ${15}
    Title Should Be  BCCVL Home

Should be logged out
    Element Should Contain  css=a.bccvllinks-login   Log in

Should be logged in as admin
    Element Should Contain  css=#user-menu .bccvl-username  admin

Navigate To Login Page
    Click Element  css=a.bccvllinks-login
    Title Should Be  BCCVL Login

Navigate To Datasets
    Click Link  link=Datasets

Navigate To Experiments
    Click Link  link=Experiments

Navigate To Knowledgebase
    Click Link  link=Knowledge Base

Click New SDM
    Click Link  css=a.bccvllinks-experiment-new

Click Discover Dataset
    Click Link  link=Discover Dataset

Log in as admin
    Navigate To Login Page
    Click Element  id=login-basic
    Wait Until Element is Visible  id=__ac_name
    Input Text  id=__ac_name  admin
    Input Password  id=__ac_password  admin
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
