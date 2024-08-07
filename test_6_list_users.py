import pytest
import requests
import allure


@pytest.mark.regression
@allure.feature('User Management')
@allure.suite('User Retrieval Tests')
@allure.title('Get Users from Page 2')
@allure.description('Test to verify retrieval of users from page 2 and response validation.')
@allure.severity(allure.severity_level.NORMAL)
def test_get_users_page_2():
    url = 'https://reqres.in/api/users?page=2'
    response = requests.get(url)

    with allure.step('Verify status code is 200'):
        assert response.status_code == 200, f"Expected status code 200, but got {response.status_code}"

    response_data = response.json()

    with allure.step('Verify pagination fields are present'):
        assert 'page' in response_data, 'Response is missing "page"'
        assert 'per_page' in response_data, 'Response is missing "per_page"'
        assert 'total' in response_data, 'Response is missing "total"'
        assert 'total_pages' in response_data, 'Response is missing "total_pages"'
        assert 'data' in response_data, 'Response is missing "data"'

    with allure.step('Verify pagination values'):
        assert response_data['page'] == 2, f"Expected page 2, but got {response_data['page']}"
        assert response_data['per_page'] == 6, f"Expected per_page 6, but got {response_data['per_page']}"
        assert response_data['total'] == 12, f"Expected total 12, but got {response_data['total']}"
        assert response_data['total_pages'] == 2, f"Expected total_pages 2, but got {response_data['total_pages']}"

    with allure.step('Verify "data" contains list of users'):
        data = response_data['data']
        assert isinstance(data, list), f"Expected data to be a list, but got {type(data)}"
        assert len(data) == 6, f"Expected 6 users in data, but got {len(data)}"

        for user in data:
            assert 'id' in user, 'User object is missing "id"'
            assert 'email' in user, 'User object is missing "email"'
            assert 'first_name' in user, 'User object is missing "first_name"'
            assert 'last_name' in user, 'User object is missing "last_name"'
            assert 'avatar' in user, 'User object is missing "avatar"'

    with allure.step('Verify "support" field is present'):
        assert 'support' in response_data, 'Response is missing "support"'
        support = response_data['support']
        assert 'url' in support, 'Support object is missing "url"'
        assert 'text' in support, 'Support object is missing "text"'


test_get_users_page_2()
