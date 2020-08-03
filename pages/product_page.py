from pages.base_page import BasePage


def locators_list(locators_name):
    sorted_locators = []
    for i in dir(locators_name):
        if i != '__class__':
            sorted_locators.append(i)
        else:
            break
    return sorted_locators


class ProductPage(BasePage):
    def is_buy_page(self, current_link):
        if '/shop/buy-' in current_link:
            return True
        return False