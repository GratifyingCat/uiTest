import pytest

from pom.AddToCart import AddToCart
from pom.ItemTitle import ItemTitle
from pom.RemoveFromCart import RemoveFromCart
from pom.Login import Login

LOGIN = 'standard_user'
PASSWORD = 'secret_sauce'
LOGIN_FIELD_XPATH = '//*[@id="user-name"]'
PASSWORD_FIELD_XPATH = '//*[@id="password"]'
LOGIN_BTN_XPATH = '//*[@id="login-button"]'
ITEM_TITLES_PATH = '.inventory_item_label a .inventory_item_name'
ADD_TO_CART_BTNS_PATH = '.pricebar .btn_inventory'
CART_COUNTER_PATH = '.shopping_cart_badge'


@pytest.mark.usefixtures('setup')
class TestSite:
    def test_login(self):
        login = Login(self.driver, LOGIN, PASSWORD, LOGIN_FIELD_XPATH, PASSWORD_FIELD_XPATH, LOGIN_BTN_XPATH)
        login.input_login()
        login.input_password()
        login.auth()

    def test_item_title(self):
        self.test_login()
        item_title = ItemTitle(self.driver, ITEM_TITLES_PATH)
        actual_titles_text = item_title.get_titles_text()
        excepted_titles_text = item_title.TITLES_TEXT
        assert excepted_titles_text == actual_titles_text, 'Validating item title text'

    def test_add_to_cart(self):
        self.test_login()
        to_cart = AddToCart(self.driver, ADD_TO_CART_BTNS_PATH, CART_COUNTER_PATH)
        to_cart.add_to_cart()
        actual_cart_value = to_cart.get_items_value()
        excepted_cart_value = to_cart.get_counter_value()
        assert int(actual_cart_value) == int(excepted_cart_value), 'Validating cart items'

    def test_remove_from_cart(self):
        self.test_login()
        to_cart = AddToCart(self.driver, ADD_TO_CART_BTNS_PATH, CART_COUNTER_PATH)
        to_cart.add_to_cart()
        remove_cart = RemoveFromCart(self.driver, ADD_TO_CART_BTNS_PATH, CART_COUNTER_PATH)
        remove_cart.remove_from_cart()
        remove_cart.cart_is_hidden()
