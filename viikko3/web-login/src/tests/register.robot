*** Settings ***
Resource  resource.robot
Suite Setup     Open And Configure Browser
Suite Teardown  Close Browser
Test Setup      Reset Application Create User And Go To Register Page

*** Test Cases ***

Register With Valid Username And Password
    Set Username  pekka
    Set Password  pekka123
    Set Password Confirmation  pekka123
    Submit Credentials
    Register Should Succeed

Register With Too Short Username And Valid Password
    Set Username  pe
    Set Password  pekka123
    Set Password Confirmation  pekka123
    Submit Credentials
    Register Should Fail With Message  Username should be more than 3 characters

Register With Valid Username And Too Short Password
    Set Username  matti
    Set Password  matti1
    Set Password Confirmation  matti1
    Submit Credentials
    Register Should Fail With Message  Password should be more than 8 characters

Register With Valid Username And Invalid Password
    Set Username  mattimatti
    Set Password  matti
    Set Password Confirmation  matti
    Submit Credentials
    Register Should Fail With Message  Password must contain some other character than letters

Register With Nonmatching Password And Password Confirmation
    Set Username  kaisa
    Set Password  kaisa123
    Set Password Confirmation  kaisa1234
    Submit Credentials
    Register Should Fail With Message  Passwords differ

Register With Username That Is Already In Use
    Set Username  maria
    Set Password  maria123
    Set Password Confirmation  maria123
    Submit Credentials
    Register Should Fail With Message  Username is already in use

*** Keywords ***
Reset Application Create User And Go To Register Page
    Reset Application
    Create User  maria  maria123
    Go To Register Page

Set Username
    [Arguments]  ${username}
    Input Text  username  ${username}

Set Password
    [Arguments]  ${password}
    Input Password  password  ${password}

Set Password Confirmation
    [Arguments]  ${password_confirmation}
    Input Password  password_confirmation  ${password_confirmation}

Register Should Succeed
    Welcome Page Should Be Open
    
Register Should Not Succeed
    Register Page Should Be Open

Submit Credentials
    Click Button  Register

Register Should Fail With Message
    [Arguments]  ${message}
    Register Page Should Be Open
    Page Should Contain  ${message}