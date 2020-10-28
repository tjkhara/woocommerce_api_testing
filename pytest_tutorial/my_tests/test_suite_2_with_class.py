import pytest

@pytest.fixture(scope="module")
def my_setup():
    print("")
    print(">>>>> My Setup <<<<<<<")
    return {
        "id": 20,
        "name": "Admas"
    }

@pytest.mark.abc
class TestCheckout(object):

    def test_checkout_as_guest(self, my_setup):
        print("Checkout as guest")
        print("Class: 111111111111")

    def test_checkout_with_existing_user(self):
        print("Checkout with existing user")
        assert 1 == 2
        print("Class: 22222222222222")