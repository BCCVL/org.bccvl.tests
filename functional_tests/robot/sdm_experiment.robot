*** Settings ***

Documentation  A test suite with a single test for valid login. This test has
...            a workflow that is created using keywords from the resource file.
Library        String
Library        DebugLibrary
Library        Collections
Resource       resource.robot
Resource       experiment.robot
Test Setup     Open Browser To BCCVL Home
Test Teardown  Close Browser


*** Test Cases ***

Test ANN 1km with Absence Dataset
    # Verify the results by checking their md5 signature
    ${md5} =  Create Dictionary  "a_experimentoutput_mean_response_curves_Phascolarctus.cinereus_AllData_Full_ANN.png"=8c317ce78029278600a0f0ca54d7e096
    Set To Dictionary  ${md5}  "a_experimentoutput_proj_current_ClampingMask.tif"=3d65ad5c43f14301beaa71b5a2e26ec6
    Set To Dictionary  ${md5}  "a_experimentoutput_proj_current_Phascolarctus.cinereus.tif"=2af082089da5a559c46829938156f572
    Set To Dictionary  ${md5}  "a_experimentoutput_pROC.Full.png"=51eb77c04e707084e9d54f5994d773a7
    Set To Dictionary  ${md5}  "a_experimentoutput_biomod2.modelEvaluation.csv"=65f9731c6cd7719535552fe2e65cc3c6
    Set To Dictionary  ${md5}  "a_experimentoutput_combined.Full.modelEvaluation.csv"=ec57d29e571cbd9c94396c4e6f9d548d
    Set To Dictionary  ${md5}  "a_experimentoutput_true_and_false_posivite_rates.Full.png"=35edee93e34d7a7be06090120e06e9ce
    Set To Dictionary  ${md5}  "a_experimentoutput_occurence_absence_hist.Full.png"=7b6780465aca9884733ef042c6abed54
    Set To Dictionary  ${md5}  "a_experimentoutput_occurence_absence_pdf.Full.png"=bb895305ba24006cea3bf554a2f041e5

    Run Sdm Experiement  test-ann-1km-with-absence-dataset  Artificial Neural Network  ann  ${md5}  12


Test ANN 1km with Pseudo Absence Points
    # Verify the results by checking their md5 signature
    ${md5} =  Create Dictionary  "a_experimentoutput_mean_response_curves_Phascolarctus.cinereus_PA1_Full_ANN.png"=fb6da5f3006f554d1305d6f1105bb3ec
    Set To Dictionary  ${md5}  "a_experimentoutput_proj_current_ClampingMask.tif"=11f6a12ccb04298e3607ccb05171e929
    Set To Dictionary  ${md5}  "a_experimentoutput_proj_current_Phascolarctus.cinereus.tif"=2f0a9b4b1ec9f24c18953b26f3e9dd01
    Set To Dictionary  ${md5}  "a_experimentoutput_pROC.Full.png"=af398961da8702d64322a5b948ac41ec
    Set To Dictionary  ${md5}  "a_experimentoutput_biomod2.modelEvaluation.csv"=7c19e86338efc05613c3dafb6d9f3a17
    Set To Dictionary  ${md5}  "a_experimentoutput_combined.Full.modelEvaluation.csv"=50d8afb21f7623c45df74021a5f16c99
    Set To Dictionary  ${md5}  "a_experimentoutput_true_and_false_posivite_rates.Full.png"=6bee3fdcc88709488033115b696ea824
    Set To Dictionary  ${md5}  "a_experimentoutput_occurence_absence_hist.Full.png"=55fbcea14a83281d8b267a4be1d12c81
    Set To Dictionary  ${md5}  "a_experimentoutput_occurence_absence_pdf.Full.png"=ad6865b56964915dfe14aef2c6aed570

    Run Sdm Experiement  test-ann-1km-with-pseudo-absence-points  Artificial Neural Network  ann  ${md5}  12  pseudoAbsence=True  randomSeed=12345678


Test RF 1km with Pseudo Absence Points
    # Verify the results by checking their md5 signature
    ${md5} =  Create Dictionary  "a_experimentoutput_mean_response_curves_Phascolarctus.cinereus_PA1_Full_RF.png"=dea2debe387f4a3ab98ae5b562293135
    Set To Dictionary  ${md5}  "a_experimentoutput_proj_current_ClampingMask.tif"=11f6a12ccb04298e3607ccb05171e929
    Set To Dictionary  ${md5}  "a_experimentoutput_proj_current_Phascolarctus.cinereus.tif"=0d615c7b9feacc46d12976b795d90216
    Set To Dictionary  ${md5}  "a_experimentoutput_pROC.Full.png"=4f060c29930a21b90da9c288e84612c7
    Set To Dictionary  ${md5}  "a_experimentoutput_biomod2.modelEvaluation.csv"=9ba64ed0dbd3eace271eb6373c9300c4
    Set To Dictionary  ${md5}  "a_experimentoutput_combined.Full.modelEvaluation.csv"=2aa7aa2332b9df9c1bdd4014f19b7b2e
    Set To Dictionary  ${md5}  "a_experimentoutput_true_and_false_posivite_rates.Full.png"=18a7450c09b69bd8dbb445f2a4714348
    Set To Dictionary  ${md5}  "a_experimentoutput_occurence_absence_hist.Full.png"=cee1e41e6614e5fb411af0693214c5fa
    Set To Dictionary  ${md5}  "a_experimentoutput_occurence_absence_pdf.Full.png"=b6674327d2db4879304bc84ddf050c0e

    Run Sdm Experiement  test-rf-1km-with-pseudo-absence-points  Random Forest  rf  ${md5}  12  pseudoAbsence=True  randomSeed=12345678


Test MAXENT 1km with Pseudo Absence Points
    # Verify the results by checking their md5 signature
    ${md5} =  Create Dictionary  "a_experimentoutput_mean_response_curves_Phascolarctus.cinereus_PA1_Full_MAXENT.png"=edd282d4075d3de1eb671410efa465ad
    Set To Dictionary  ${md5}  "a_experimentoutput_proj_current_ClampingMask.tif"=11f6a12ccb04298e3607ccb05171e929
    Set To Dictionary  ${md5}  "a_experimentoutput_proj_current_Phascolarctus.cinereus.tif"=1f990f84920838386653cf66b114ae22
    Set To Dictionary  ${md5}  "a_experimentoutput_pROC.Full.png"=e9cec62e25804e9834fdc137815b5722
    Set To Dictionary  ${md5}  "a_experimentoutput_biomod2.modelEvaluation.csv"=f8b57ccac0f67b19d1480d7dfe7e5c0d
    Set To Dictionary  ${md5}  "a_experimentoutput_combined.Full.modelEvaluation.csv"=61ed1364115d1c3f04715883b032bae9
    Set To Dictionary  ${md5}  "a_experimentoutput_true_and_false_posivite_rates.Full.png"=da7dc615bf99ca9d62fc633b97a46817
    Set To Dictionary  ${md5}  "a_experimentoutput_occurence_absence_hist.Full.png"=09d904a20c99cfc5e4e97964fbfb0a3e
    Set To Dictionary  ${md5}  "a_experimentoutput_occurence_absence_pdf.Full.png"=f6e820d6fd9e60a6f498d04802edfc15
    Set To Dictionary  ${md5}  "a_experimentoutput_maxentResults.csv"=f059be9837dd3592b03172c9c5f4ace7
    
    Run Sdm Experiement  test-maxent-1km-with-pseudo-absence-points  Maximum Entropy Modeling  maxent  ${md5}  14  pseudoAbsence=True  randomSeed=12345678


**** Keywords ***

Run Sdm Experiement
    [Arguments]    ${testLabel}    ${algorithmName}    ${algoShortName}    ${md5}    ${resultCount}    ${pseudoAbsence}=False    ${randomSeed}=None
    [Documentation]    Run a SDM experiment and verify the results to match to the specified MD5 signatures.

    Log in as admin
    Navigate To Experiments
    Click New SDM
    # Fill in form
    Input Text  name=form.widgets.IDublinCore.title  ${TEST NAME}
    # TODO: verify input element has class valid
    Input Text  name=form.widgets.IDublinCore.description  ${TEST NAME} with Koala occurrences

    # Switch to next tab
    Click Next
    Select Occurrence Dataset
    Page Should Contain  Koala - Mini occurrence dataset for Redland City

    # Switch to next tab
    Click Next

    # Use either pseudo absence points or absence dataset
    Run Keyword If  ${pseudoAbsence}  Use Pseudo Absence Points  ELSE  Use Absence Dataset
    
    # Switch to next tab
    Click Next
    Select Environmental Dataset
    Page Should Contain  Current climate layers for Redland City, 30" (~1km)
    Click Link  link=Select None
    Click Label  B14 - Precipitation of Driest Month
    
    # Switch to next tab
    Click Next
    # select an algorithm
    Click Label  ${algorithmName}
    Click Link  configuration for ${algorithmName}

    # Set random seed
    Run Keyword If  ${randomSeed}  Set Algorithm Parameter Random Seed  ${algorithmName}  12345678
    
    # Switch to next tab
    Click Next
    Click Button  xpath=//button[@name='form.buttons.save']
    # TODO: check spinner
    Wait For Ajax

    # new page:
    Location Should Be  ${LOGIN URL}/experiments/${testLabel}/view
    # Job submitted info message
    # 1 result on page but empty (xpath count)
    Wait For Experiment State  COMPLETED
    # How many files inside result?
    ${results_table} =  Set Variable  id('bccvl-experimentresults-table')
    # Verify experiment title
    Element Should Contain  css=div.experiment-accordion-heading  ${TEST NAME}
    Element Should Contain  css=div.experiment-accordion-heading  Algorithm: ${algoShortName}
    # click accordion
    Click Element  css=#bccvl-experimentresults-table div.experiment-accordion-heading a.expand-btn
    # make sure we have all the result files
    Locator Should Match X Times  css=#bccvl-experimentresults-table div div.row-fluid  ${resultCount}

    # Verify the results by checking their md5 signature
    ${keys} =  Get Dictionary Keys  ${md5}
    :For  ${key}  IN  @{keys}
    \  ${sig} =  Get From Dictionary  ${md5}  ${key}
    \  ${link} =  Get Result Link  ${key}
    \  Verify Result  ${link}  ${sig}

    # Clean up:
    Clean Up Experiment  ${testLabel}


Click Label
    [Arguments]    ${label}    ${index}=1
    [Documentation]    Clicks label element which contains text ${label}.
    ...    If there is more than one label with given text, specify index to match those labels.
    Click Element    xpath=(//label[contains(., '${label}')])[${index}]
