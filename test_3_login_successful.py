import pytest
import requests
import json
import allure

@pytest.mark.smoke
@pytest.mark.regression
@allure.feature('User Authentication')
@allure.suite('Login Tests')
@allure.title('Successful Login Test')
@allure.description('Test to verify successful login returns a valid token.')
@allure.severity(allure.severity_level.CRITICAL)
def test_login_successful():
    data = {
        "email": "eve.holt@reqres.in",
        "password": "cityslicka"
    }
    headers = {'Content-Type': 'application/json'}

    response = requests.post(
        'https://reqres.in/api/login',
        data=json.dumps(data),
        headers=headers
    )

    with allure.step('Verify status code is 200 for successful login'):
        assert response.status_code == 200, f"Expected status code 200, but got {response.status_code}"

    response_data = response.json()

    with allure.step('Verify response contains "token"'):
        assert 'token' in response_data, 'Response is missing "token"'

    with allure.step('Verify "token" is a non-empty string'):
        token_value = response_data['token']
        assert len(response_data.get('token', '')) > 0, 'Token length is 0'

test_login_successful()