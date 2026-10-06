*** Settings ***
Resource          ../resources/PageObjects/LoginPage.robot
Test Setup        Open Login Page
Test Teardown     Close Login Session

*** Test Cases ***
Valid Login Scenario
    Input Username And Password    standard_user    secret_sauce
    Submit Login Form
    Location Should Be             https://www.saucedemo.com/inventory.html

Locked Out User Scenario
    Input Username And Password    locked_out_user    secret_sauce
    Submit Login Form
    Verify Error Message           Epic sadface: Sorry, this user has been locked out.

Invalid Credentials Scenario
    Input Username And Password    invalid_user    wrong_pass
    Submit Login Form
    Verify Error Message           Epic sadface: Username and password do not match