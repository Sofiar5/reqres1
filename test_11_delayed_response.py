import pytest
import requests
import allure

@pytest.mark.regression
@allure.feature('User API')
@allure.suite('Get User Details')
@allure.title('Get Users with Delay')
@allure.description('Test to verify that getting a list of users with a delay returns a 200 status code and the correct response body.')
@allure.severity(allure.severity_level.NORMAL)
def test_get_users_with_delay():
    url = 'https://reqres.in/api/users?delay=3'
    response = requests.get(url)

    with allure.step('Verify status code is 200'):
        assert response.status_code == 200, f"Expected status code 200, but got {response.status_code}"

    response_data = response.json()

    with allure.step('Verify response contains pagination fields'):
        assert 'page' in response_data, 'Response is missing "page"'
        assert 'per_page' in response_data, 'Response is missing "per_page"'
        assert 'total' in response_data, 'Response is missing "total"'
        assert 'total_pages' in response_data, 'Response is missing "total_pages"'
        assert 'data' in response_data, 'Response is missing "data"'

    with allure.step('Verify "data" is a non-empty list'):
        data_list = response_data['data']
        assert isinstance(data_list, list) and len(data_list) > 0, 'Expected "data" to be a non-empty list'

    for user in data_list:
        with allure.step('Verify user object contains required fields'):
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
        assert support['url'] == "https://reqres.in/#support-heading", f"Expected support url 'https://reqres.in/#support-heading', but got '{support['url']}'"
        assert support['text'] == "To keep ReqRes free, contributions towards server costs are appreciated!", f"Expected support text 'To keep ReqRes free, contributions towards server costs are appreciated!', but got '{support['text']}'"


test_get_users_with_delay()
