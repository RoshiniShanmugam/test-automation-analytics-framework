*** Settings ***
Library    SeleniumLibrary

*** Variables ***
${LOGIN_URL}        https://www.saucedemo.com/
${BROWSER}          chrome
${USERNAME_FIELD}   id=user-name
${PASSWORD_FIELD}   id=password
${LOGIN_BTN}        id=login-button
${ERROR_CONTAINER}  css=h3[data-test="error"]

*** Keywords ***
Open Login Page
    Open Browser    ${LOGIN_URL}    ${BROWSER}
    Maximize Browser Window

Input Username And Password
    [Arguments]    ${username}    ${password}
    Input Text     ${USERNAME_FIELD}    ${username}
    Input Text     ${PASSWORD_FIELD}    ${password}

Submit Login Form
    Click Button    ${LOGIN_BTN}

Verify Error Message
    [Arguments]    ${expected_error}
    Element Should Contain    ${ERROR_CONTAINER}    ${expected_error}

Close Login Session
    Close Browser