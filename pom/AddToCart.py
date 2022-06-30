from base.seleniumbase import SeleniumBase


class AddToCart(SeleniumBase):
    def __init__(self, driver, add_to_cart_btns_path, cart_counter_path):
        super(AddToCart, self).__init__(driver)
        self.add_to_cart_btns_path = add_to_cart_btns_path
        self.cart_counter_path = cart_counter_path

    def get_items_value(self):
        items = self.are_visible('CSS', self.add_to_cart_btns_path)
        return len(items)

    def get_counter_value(self):
        return self.is_visible('CSS', self.cart_counter_path).text

    def add_to_cart(self):
        add_to_cart_buttons = self.are_visible('CSS', self.add_to_cart_btns_path)
        for add_to_cart_button in add_to_cart_buttons:
            add_to_cart_button.click()

