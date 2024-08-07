import pytest
import requests
import allure


@pytest.mark.regression
@allure.feature('User API')
@allure.suite('Get User Details')
@allure.title('Get Non-Existent User')
@allure.description('Test to verify that fetching a non-existent user returns a 404 status code and an empty response body.')
@allure.severity(allure.severity_level.CRITICAL)
def test_get_non_existent_user():
    url = 'https://reqres.in/api/users/23'
    response = requests.get(url)

    with allure.step('Verify status code is 404'):
        assert response.status_code == 404, f"Expected status code 404, but got {response.status_code}"

    with allure.step('Verify response body is empty'):
        response_data = response.json()
        assert response_data == {}, f"Expected empty response body, but got {response_data}"


test_get_non_existent_user()
