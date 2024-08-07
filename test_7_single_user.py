import pytest
import requests
import allure

@pytest.mark.regression
@allure.feature('User Management')
@allure.suite('User Retrieval Tests')
@allure.title('Get User by ID')
@allure.description('Test to verify retrieval of a user by ID and response validation.')
@allure.severity(allure.severity_level.NORMAL)
def test_get_user_by_id():
    url = f'https://reqres.in/api/users/2'
    response = requests.get(url)

    with allure.step('Verify status code is 200'):
        assert response.status_code == 200, f"Expected status code 200, but got {response.status_code}"

    response_data = response.json()

    with allure.step('Verify "data" field is present'):
        assert 'data' in response_data, 'Response is missing "data"'

    user_data = response_data['data']

    with allure.step('Verify user data fields are present'):
        assert 'id' in user_data, 'User object is missing "id"'
        assert 'email' in user_data, 'User object is missing "email"'
        assert 'first_name' in user_data, 'User object is missing "first_name"'
        assert 'last_name' in user_data, 'User object is missing "last_name"'
        assert 'avatar' in user_data, 'User object is missing "avatar"'

    with allure.step('Verify user data values'):
        assert user_data['id'] == 2, f"Expected id 2, but got {user_data['id']}"
        assert user_data['email'] == "janet.weaver@reqres.in", f"Expected email 'janet.weaver@reqres.in', but got '{user_data['email']}'"
        assert user_data['first_name'] == "Janet", f"Expected first_name 'Janet', but got '{user_data['first_name']}'"
        assert user_data['last_name'] == "Weaver", f"Expected last_name 'Weaver', but got '{user_data['last_name']}'"
        assert user_data['avatar'] == "https://reqres.in/img/faces/2-image.jpg", f"Expected avatar 'https://reqres.in/img/faces/2-image.jpg', but got '{user_data['avatar']}'"

    with allure.step('Verify "support" field is present'):
        assert 'support' in response_data, 'Response is missing "support"'
        support = response_data['support']
        assert 'url' in support, 'Support object is missing "url"'
        assert 'text' in support, 'Support object is missing "text"'
        assert support['url'] == "https://reqres.in/#support-heading", f"Expected support url 'https://reqres.in/#support-heading', but got '{support['url']}'"
        assert support['text'] == "To keep ReqRes free, contributions towards server costs are appreciated!", f"Expected support text 'To keep ReqRes free, contributions towards server costs are appreciated!', but got '{support['text']}'"


test_get_user_by_id()
