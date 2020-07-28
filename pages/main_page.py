from .base_page import BasePage


class MainPage(BasePage):
    def is_main_page(self):
        current_url = self.browser.current_url
        return current_url == 'https://www.apple.com/ru/'
