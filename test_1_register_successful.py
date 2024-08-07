import pytest
import json
import requests
import allure

my_token = None

@pytest.mark.smoke
@pytest.mark.regression

@allure.feature('User Registration')
@allure.suite('Registration Tests')
@allure.title('Successful Registration Test')
@allure.description('Test to verify successful user registration returns a valid token.')
@allure.severity(allure.severity_level.CRITICAL)

def test_register_successful():
    global my_token

    data = {
        "email": "eve.holt@reqres.in",
        "password": "pistol"
    }
    headers = {'Content-Type': 'application/json'}

    response = requests.post('https://reqres.in/api/register',
                             data=json.dumps(data),
                             headers=headers
                             )

    with allure.step('Verify response status code is 200'):
        assert response.status_code == 200, f'Expected status code 200 but got {response.status_code}'

    with allure.step('Verify "token" is present in response'):
        assert 'token' in response.json(), 'Token not found in response'

    with allure.step('Verify "token" length is greater than 0'):
        assert len(response.json().get('token', '')) > 0, 'Token length is 0'

    # Save the token for later use
    my_token = response.json().get('token')

test_register_successful()
