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
    ${dsurl} =  Wait for ALA import  Strongylium
    Clean up ALA import  ${dsurl}


Import Bad ALA record
    Log in as admin
    Navigate To Datasets
    Click Discover Dataset
    ${url} =  Get Location
    ${query} =  Set Variable  ${url}?import=Import&lsid=bad%3Alsid%3Ahere&taxon=Bad%20Species
    Go To  ${query}
    ${dsurl} =  Wait for ALA import to fail  Bad Species
    Clean up ALA import  ${dsurl}


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
    Click Link  xpath=//div[@id='searchOccurrence']/ul/li/a[contains(., '(species)') and contains(., '${species}')]
    # Wait for species search result
    Wait Until Element is Visible  id=searchOccurrence_results
    # Click download link in search result
    Click Link  xpath=//div[@id='searchOccurrence_results']//td[contains(., '${species}')]/..//a[contains(*/@class, 'icon-download-alt')]


Wait for ALA import
    [Arguments]  ${species}
    [Documentation]  Wait until species import finishes
    ...              This keyword assumes that the first element in the dataset listing
    ...              is the one we are interested in.
    ...              The title needs to include 'occurrences' to indicate a successful import
    ...              Keyword returns the url of the imported dataset
    # define xpath query for first dataset list entry matching given species
    ${listentry} =  Set Variable  (//div[@id='datasets-listing']/div[contains(., '${species}')])[1]
    # Verify url ends with datasets
    ${url}  Get Location
    Should End With  ${url}  datasets
    # check spinner
    Wait Until Element is Visible  xpath=${listentry}/div[@class="dataset-list-dropdown"]/a/i[contains(@class, 'bccvl-small-spinner')]
    # Wait until import is finished
    Wait Until Page Contains Element  xpath=${listentry}//p[contains(., 'occurrences')]  5 min
    # Get dataset url and return it
    ${dataseturl} =  Get Element Attribute  xpath=${listentry}//a[contains(@class, 'dataset-info-btn')]@href
    # need to get rid of /details on url
    ${dataseturl} =  Fetch From Left  ${dataseturl}  /details
    [Return]  ${dataseturl}


Wait for ALA import to fail
    [Arguments]  ${species}
    [Documentation]  Wait until species import finishes
    ...              This keyword assumes that the first element in the dataset listing
    ...              is the one we are interested in.
    ...              The details bar will include a warning icon when finished
    ...              Keyword returns the url of the imported dataset
    # define xpath query for first dataset list entry matching given species
    ${listentry} =  Set Variable  (//div[@id='datasets-listing']/div[contains(., '${species}')])[1]
    # Verify url ends with datasets
    ${url}  Get Location
    Should End With  ${url}  datasets
    # check spinner
    Wait Until Element is Visible  xpath=${listentry}/div[@class="dataset-list-dropdown"]/a/i[contains(@class, 'bccvl-small-spinner')]
    # Wait until warning icon appears
    Wait Until Page Contains Element  xpath=${listentry}/div[@class="dataset-list-dropdown"]/a/i[contains(@class, 'icon-warning-sign')]  5 min
    # Get dataset url and return it
    ${dataseturl} =  Get Element Attribute  xpath=${listentry}/div[@class="dataset-list-dropdown"]/a/i[contains(@class, 'icon-warning-sign')]@data-url
    [Return]  ${dataseturl}


Clean up ALA import
    [Arguments]  ${dataseturl}
    [Documentation]  Removes dataset import via ALA
    ...              The dataset to remove is identified via the dataseturl parameter
    ${delurl} =  Set Variable  ${dataseturl}/delete_confirmation
    Go To  ${delurl}
    Click Button  Delete
