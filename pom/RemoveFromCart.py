from selenium.common import TimeoutException

from base.seleniumbase import SeleniumBase


class RemoveFromCart(SeleniumBase):
    def __init__(self, driver, remove_from_cart_btns_path, cart_counter_path):
        super(RemoveFromCart, self).__init__(driver)
        self.remove_from_cart_btns_path = remove_from_cart_btns_path
        self.cart_counter_path = cart_counter_path

    def remove_from_cart(self):
        remove_from_cart_buttons = self.are_visible('CSS', self.remove_from_cart_btns_path)
        for remove_from_cart_button in remove_from_cart_buttons:
            remove_from_cart_button.click()

    def cart_is_hidden(self):
        try:
            self.is_visible('CSS', self.cart_counter_path)
            return False
        except TimeoutException:
            return True

