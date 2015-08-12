*** Settings ***

Documentation  A test suite with a single test for valid login. This test has
...            a workflow that is created using keywords from the resource file.
Library        String
Library        DebugLibrary
Resource       resource.robot
Test Setup     Open Browser To BCCVL Home
Test Teardown  Close Browser


*** Test Cases ***

# Maybe just pick first (species) in list and click first download link ... fetch species name first to look up in datasets list (should be first in list)
Import ALA
    Log in as admin
    Import From ALA  koala  Strongylium
    ${dsuuid} =  Wait for ALA import  Strongylium
    Clean up ALA import  ${dsuuid}


Import Bad ALA record
    Log in as admin
    Navigate To Datasets
    Click Discover Dataset
    ${url} =  Get Location
    ${query} =  Set Variable  ${url}?import=Import&lsid=bad%3Alsid%3Ahere&taxon=Bad%20Species
    Go To  ${query}
    ${dsuuid} =  Wait for ALA import to fail  Bad Species
    Clean up ALA import  ${dsuuid}


**** Keywords ***


Import From ALA
    [Arguments]  ${search}  ${species}
    [Documentation]  Import dataset from ALA matching Species
    # go to import ALA page
    Navigate To Datasets
    Click Discover Dataset
    # Enter search term
    Input Text  name=searchOccurrence_query  ${search}
    # wait until ala autocompletion finishes
    Wait Until Element is Visible  css=div#searchOccurrence ul li
    # Click selected species entry in autocomplete box
    Click Link  xpath=//div[@id='searchOccurrence']//a[contains(., '(species)') and contains(., '${species}')]
    # Wait for species search result
    Wait Until Element is Visible  id=searchOccurrence_results
    # Click download link in search result
    Click Link  xpath=//div[@id='searchOccurrence_results']//td[contains(., '${species}')]/..//a[contains(@class, 'import-dataset-btn')]


Wait for ALA import
    [Arguments]  ${species}
    [Documentation]  Wait until species import finishes
    ...              This keyword assumes that the first element in the dataset listing
    ...              is the one we are interested in.
    ...              The title needs to include 'occurrences' to indicate a successful import
    ...              Keyword returns the url of the imported dataset
    # define xpath query for first dataset list entry matching given species
    ${listentry} =  Set Variable  id('datasets-listing')/div[contains(., '${species}')][1]
    ${spinner} =  Set Variable  ${listentry}/div[@class="dataset-list-dropdown"]/a/i[contains(@class, 'bccvl-small-spinner')]
    # Verify url ends with datasets
    ${url}  Get Location
    Should End With  ${url}  datasets
    # check spinner
    Wait Until Element is Visible  xpath=${spinner}
    # Wait until import is finished (occurrences is added to title by ala import)
    Wait Until Page Contains Element  xpath=${listentry}//p[contains(., 'occurrences')]  5 min
    # Get dataset uuid and return it (dataset-info-btn is always there even if import failed)
    ${dsuuid} =  Get Element Attribute  xpath=${listentry}@data-uuid
    [Return]  ${dsuuid}


# TODO: make this return dataset uuid?
Wait for ALA import to fail
    [Arguments]  ${species}
    [Documentation]  Wait until species import finishes
    ...              This keyword assumes that the first element in the dataset listing
    ...              is the one we are interested in.
    ...              The details bar will include a warning icon when finished
    ...              Keyword returns the url of the imported dataset
    # define xpath query for first dataset list entry matching given species
    ${listentry} =  Set Variable  id('datasets-listing')/div[contains(., '${species}')][1]
    # Verify url ends with datasets
    ${url}  Get Location
    Should End With  ${url}  datasets
    # check spinner
    Wait Until Element is Visible  xpath=${listentry}/div[@class="dataset-list-dropdown"]/a/i[contains(@class, 'bccvl-small-spinner')]
    # Wait until warning icon appears
    Wait Until Page Contains Element  xpath=${listentry}/div[@class="dataset-list-dropdown"]/a/i[contains(@class, 'icon-warning-sign')]  5 min
    # Get dataset uuid and return it (dataset-info-btn is always there even if import failed)
    ${dsuuid} =  Get Element Attribute  xpath=${listentry}@data-uuid
    [Return]  ${dsuuid}


Clean up ALA import
    [Arguments]  ${dsuuid}
    [Documentation]  Removes dataset import via ALA
    ...              The dataset to remove is identified via the dataseturl parameter
    ${listentry} =  Set Variable  id('datasets-listing')/div[@data-uuid='${dsuuid}']
    ${details_btn} =  Set Variable  ${listentry}//a[contains(@class, 'dropdown-button')]
    ${remove_btn} =  Set Variable  ${listentry}//a[contains(@class, 'remove-dataset-btn')]
    ${modal_remove_btn} =  Set Variable  id('form-buttons-remove')
    # make remove button visible
    Click Link  xpath=${details_btn}
    Wait until Element is Visible  xpath=${remove_btn}
    Click Link  xpath=${remove_btn}
    # Wait until remove button in modal is on page and is visible
    Wait Until Page Contains Element  xpath=${modal_remove_btn}
    Wait Until Element is Visible  xpath=${modal_remove_btn}
    Click Button  xpath=${modal_remove_btn}
    # The form is submitted via ajax
    Wait For Ajax
    # Do some checks
    Location should be  ${DATASETS URL}
    Page Should Not Contain Element  xpath=${listentry}
    
