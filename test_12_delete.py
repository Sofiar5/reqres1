import pytest
import requests
import allure

@pytest.mark.smoke
@pytest.mark.regression
@allure.feature('User API')
@allure.suite('Delete User Operations')
@allure.title('Delete Existing User')
@allure.description('Test to verify that deleting an existing user returns a 204 status code and an empty response body.')
@allure.severity(allure.severity_level.CRITICAL)
def test_delete_user():
    response = requests.delete('https://reqres.in/api/users/2')

    with allure.step('Verify status code is 204 for successful user deletion'):
        assert response.status_code == 204, f"Expected status code 204, but got {response.status_code}"

    with allure.step('Verify response body is empty'):
        assert len(response.content) == 0, f"Expected empty response body, but got {response.content}"


test_delete_user()