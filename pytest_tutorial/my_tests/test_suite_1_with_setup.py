import pytest

pytestmark = [pytest.mark.fe, pytest.mark.slow]

@pytest.fixture(scope="module")
def my_setup():
    print("")
    print(">>>>> My Setup <<<<<<<")
    return {
        "id": 20,
        "name": "Admas"
    }

@pytest.mark.smoke
@pytest.mark.ll
def test_login_page_valid_user(my_setup):
    print("\n\n")
    print("Login with valid user.")
    print("Function: aaaaaaaaaaaaaaaa")
    print(f"My name is {my_setup.get('name')}")
    # import pdb; pdb.set_trace()

@pytest.mark.regression
def test_login_page_wrong_password(my_setup):
    print("Login with wrong password")
    print("Function: bbbbbbbbbbbbbbbbb")
    # assert 1 == 2, "One is not two"