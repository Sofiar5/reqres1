import pytest
import requests
import json
import allure


@pytest.mark.regression
@allure.feature('User API')
@allure.suite('Update User Details')
@allure.title('Update Existing User')
@allure.description('Test to verify that updating an existing user returns a 200 status code and the correct response body.')
@allure.severity(allure.severity_level.CRITICAL)
def test_update_user():
    url = 'https://reqres.in/api/users/2'
    data = {
        "name": "morpheus",
        "job": "zion resident"
    }
    headers = {'Content-Type': 'application/json'}

    response = requests.put(
        url,
        data=json.dumps(data),
        headers=headers
    )

    with allure.step('Verify status code is 200 for successful user update'):
        assert response.status_code == 200, f"Expected status code 200, but got {response.status_code}"

    response_data = response.json()

    with allure.step('Verify response contains "name", "job", and "updatedAt"'):
        assert 'name' in response_data, 'Response is missing "name"'
        assert 'job' in response_data, 'Response is missing "job"'
        assert 'updatedAt' in response_data, 'Response is missing "updatedAt"'

    with allure.step('Verify "name" is "morpheus"'):
        assert response_data['name'] == 'morpheus', f"Expected name 'morpheus', but got '{response_data['name']}'"

    with allure.step('Verify "job" is "zion resident"'):
        assert response_data['job'] == 'zion resident', f"Expected job 'zion resident', but got '{response_data['job']}'"

    with allure.step('Verify "updatedAt" is a valid timestamp'):
        updated_at_value = response_data['updatedAt']
        assert isinstance(updated_at_value,str) and updated_at_value, f"Expected updatedAt to be a valid timestamp, but got '{updated_at_value}'"


test_update_user()
