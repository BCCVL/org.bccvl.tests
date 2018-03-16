*** Settings ***

Documentation  March 2018 Suite, Test 1
Library        String
Resource       ../resource.robot
Resource       ../experiment.robot
Resource       keywords.robot
Test Setup     Open Browser To BCCVL Home
Test Teardown  Close Browser
Test Timeout   2 minutes

*** Keywords ***

Navigate to Uploads
    Click Link  link=Datasets
    Wait Until Element is Visible  link=Upload Dataset
    Click Link  link=Upload Dataset

Wait for Upload
    [Arguments]  ${species}
    # define xpath query for first dataset list entry matching given species
    ${listentry} =  Set Variable  id('datasets-listing')/div[contains(., '${species}')][1]
    ${maininfo} =  Set Variable  ${listentry}//div[contains(@class, "dataset-main-info")]
    ${spinner} =  Set Variable  ${maininfo}/div[contains(@class, "dataset-loading")]
    # Verify url ends with datasets
    ${url}  Get Location
    ${url} =  Fetch From Left  ${url}  \#
    Should End With  ${url}  datasets
    # check spinner
    Run Keyword And Ignore Error  Wait Until Page Contains Element  xpath=${spinner}
    Run Keyword And Ignore Error  Wait Until Element is Visible  xpath=${spinner}
    # Wait until import is finished (export button is available after upload completes)
    Wait Until Page Contains Element  xpath=${listentry}//a[contains(., 'Export to ALA Spatial Portal')]  1 minute
    # Get dataset uuid and return it
    ${dsuuid} =  Get Element Attribute  xpath=${listentry}  attribute=data-uuid
    [Return]  ${dsuuid}

*** Test Cases ***

Upload Egernia Occurrences
    Log in as admin
    Navigate to Uploads

    Select From List By Label  id=upload-dataset-type  Species Occurrence
    Sleep  2s

    Choose File  id=speciesoccurrence-widgets-file  ${CURDIR}/Egernia_occ.csv
    Input Text  id=speciesoccurrence-widgets-title  Egernia Occurrences
    Input Text  id=speciesoccurrence-widgets-description  Robot testing dataset.
    Input Text  id=speciesoccurrence-widgets-scientificName  Egernia

    Select Checkbox  id=speciesoccurrence-widgets-legalcheckbox-0

    Click Element  id=speciesoccurrence-buttons-save

    Wait Until Page Contains Element  css=section.bccvl-datasetlist

    Wait for Upload  Egernia Occurrences

Upload Egernia Reduced Background Absences
    Log in as admin
    Navigate to Uploads

    Select From List By Label  id=upload-dataset-type  Species Absence
    Sleep  2s

    Choose File  id=speciesabsence-widgets-file  ${CURDIR}/Egernia_bg_reduced.csv
    Input Text  id=speciesabsence-widgets-title  Egernia Reduced Background Absences
    Input Text  id=speciesabsence-widgets-description  Robot testing dataset.
    Input Text  id=speciesabsence-widgets-scientificName  Egernia

    Select Checkbox  id=speciesabsence-widgets-legalcheckbox-0

    Click Element  id=speciesabsence-buttons-save

    Wait Until Page Contains Element  css=section.bccvl-datasetlist

    Wait for Upload  Egernia Reduced Background Absences

Upload Monarch Butterfly Monthly Occurrences
    Log in as admin
    Navigate to Uploads

    Select From List By Label  id=upload-dataset-type  Species Occurrence
    Sleep  2s

    Choose File  id=speciesoccurrence-widgets-file  ${CURDIR}/Monarch_butterfly_occ.csv
    Input Text  id=speciesoccurrence-widgets-title  Monarch Butterfly Occurrences
    Input Text  id=speciesoccurrence-widgets-description  Robot testing dataset.
    Input Text  id=speciesoccurrence-widgets-scientificName  Danaus plexippus

    Select Checkbox  id=speciesoccurrence-widgets-legalcheckbox-0

    Click Element  id=speciesoccurrence-buttons-save

    Wait Until Page Contains Element  css=section.bccvl-datasetlist

    Wait for Upload  Monarch Butterfly Occurrences

Upload Multispecies Occurrences
    Log in as admin
    Navigate to Uploads

    Select From List By Label  id=upload-dataset-type  Multi Species Occurrence
    Sleep  2s

    Choose File  id=multispeciesoccurrence-widgets-file  ${CURDIR}/Egernia_Eucalyptus_Rhinella_occ.csv
    Input Text  id=multispeciesoccurrence-widgets-title  Egernia Eucalyptus Rhinella Occurrences
    Input Text  id=multispeciesoccurrence-widgets-description  Robot testing dataset.

    Select Checkbox  id=multispeciesoccurrence-widgets-legalcheckbox-0

    Click Element  id=multispeciesoccurrence-buttons-save

    Wait Until Page Contains Element  css=section.bccvl-datasetlist

    Wait for Upload  Egernia Eucalyptus Rhinella Occurrences

Upload Multispecies Background Absences
    Log in as admin
    Navigate to Uploads

    Select From List By Label  id=upload-dataset-type  Multi Species Absence
    Sleep  2s

    Choose File  id=multispeciesabsence-widgets-file  ${CURDIR}/Egernia_Eucalyptus_Rhinella_bg.csv
    Input Text  id=multispeciesabsence-widgets-title  Egernia Eucalyptus Rhinella Background Absences
    Input Text  id=multispeciesabsence-widgets-description  Robot testing dataset.

    Select Checkbox  id=multispeciesabsence-widgets-legalcheckbox-0

    Click Element  id=multispeciesabsence-buttons-save

    Wait Until Page Contains Element  css=section.bccvl-datasetlist

    Wait for Upload  Egernia Eucalyptus Rhinella Background Absences



