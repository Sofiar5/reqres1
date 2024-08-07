import pytest
import requests
import json
import allure

@pytest.mark.smoke
@pytest.mark.regression
@allure.feature('User Authentication')
@allure.suite('Login Tests')
@allure.title('Login Test with Missing Password')
@allure.description('Test to verify login fails when password is missing and appropriate error message is returned.')
@allure.severity(allure.severity_level.CRITICAL)
def test_login_missing_password():
    data = {
        "email": "peter@klaven"
    }
    headers = {'Content-Type': 'application/json'}

    response = requests.post(
        'https://reqres.in/api/login',
        data=json.dumps(data),
        headers=headers
    )

    with allure.step('Verify status code is 400 for missing password'):
        assert response.status_code == 400, f"Expected status code 400, but got {response.status_code}"

    with allure.step('Verify error message for missing password'):
        error_message = response.json().get('error')
        assert error_message == "Missing password", f"Expected error message 'Missing password', but got '{error_message}'"


test_login_missing_password()