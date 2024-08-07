import pytest
import json
import requests
import allure

@pytest.mark.smoke
@pytest.mark.regression


@allure.feature('User Registration')
@allure.suite('Registration Tests')
@allure.title('Unsuccessful Registration')
@allure.description('Tests unsuccessful registration due to missing password')
@allure.severity(allure.severity_level.CRITICAL)

def test_register_unsuccessful():
    data = {
        "email": "sydney@fife"
    }
    headers = {'Content-Type': 'application/json'}

    response = requests.post('https://reqres.in/api/register',
                             data=json.dumps(data),
                             headers=headers
                             )

    with allure.step('Verify status code is 400 for missing password'):
        assert response.status_code == 400, f"Expected status code 400, but got {response.status_code}"

    with allure.step('Verify error message for missing password'):
        error_message = response.json().get('error')
        assert error_message == "Missing password", f"Expected error message 'Missing password', but got '{error_message}'"

test_register_unsuccessful()