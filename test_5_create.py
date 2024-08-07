import pytest
import requests
import json
import allure

my_ID = None

@pytest.mark.smoke
@pytest.mark.regression
@allure.feature('User Management')
@allure.suite('User Creation Tests')
@allure.title('Successful User Creation Test')
@allure.description('Test to verify successful user creation and response validation.')
@allure.severity(allure.severity_level.CRITICAL)
def test_create_user():
    global my_ID
    data = {
        "name": "morpheus",
        "job": "leader"
    }
    headers = {'Content-Type': 'application/json'}

    response = requests.post(
        'https://reqres.in/api/users',
        data=json.dumps(data),  # Convert the dictionary to a JSON string
        headers=headers
    )

    with allure.step('Verify status code is 201 for successful user creation'):
        assert response.status_code == 201, f"Expected status code 201, but got {response.status_code}"

    response_data = response.json()

    with allure.step('Verify response contains "name", "job", "id", and "createdAt"'):
        assert 'name' in response_data, 'Response is missing "name"'
        assert 'job' in response_data, 'Response is missing "job"'
        assert 'id' in response_data, 'Response is missing "id"'
        assert 'createdAt' in response_data, 'Response is missing "createdAt"'

    with allure.step('Verify "name" is "morpheus"'):
        assert response_data['name'] == 'morpheus', f"Expected name 'morpheus', but got '{response_data['name']}'"

    with allure.step('Verify "job" is "leader"'):
        assert response_data['job'] == 'leader', f"Expected job 'leader', but got '{response_data['job']}'"

    with allure.step('Verify "id" is a non-empty string'):
        id_value = response_data['id']
        assert isinstance(id_value, str) and id_value, f"Expected ID to be a non-empty string, but got '{id_value}'"

        # Save the ID for later use
        my_ID = id_value

    with allure.step('Verify "createdAt" is a valid timestamp'):
        created_at_value = response_data['createdAt']
        assert isinstance(created_at_value,str) and created_at_value, f"Expected createdAt to be a valid timestamp, but got '{created_at_value}'"

test_create_user()