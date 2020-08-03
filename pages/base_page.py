from .locators import BasePageLocators
from selenium.common.exceptions import TimeoutException
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.keys import Keys


class BasePage:
    def __init__(self, browser, url):
        self.browser = browser
        self.url = url

    def open(self):
        self.browser.get(self.url)

    def go_to_home_page(self):
        self.browser.find_element(*BasePageLocators.HOME_PAGE_ICON).click()

    def go_to_mac_page(self):
        self.browser.find_element(*BasePageLocators.MAC_TOP_MENU_BTN).click()

    def go_to_ipad_page(self):
        self.browser.find_element(*BasePageLocators.IPAD_TOP_MENU_BTN).click()

    def go_to_iphone_page(self):
        self.browser.find_element(*BasePageLocators.IPHONE_TOP_MENU_BTN).click()

    def go_to_watch_page(self):
        self.browser.find_element(*BasePageLocators.WATCH_TOP_MENU_BTN).click()

    def go_to_tv_page(self):
        self.browser.find_element(*BasePageLocators.TV_TOP_MENU_BTN).click()

    def go_to_music_page(self):
        self.browser.find_element(*BasePageLocators.MUSIC_TOP_MENU_BTN).click()

    def go_to_support_page(self):
        self.browser.find_element(*BasePageLocators.SUPPORT_TOP_MENU_BTN).click()

    def go_to_basket(self):
        self.browser.find_element(*BasePageLocators.BAG_TOP_MENU_BTN).click()
        self.browser.find_element(*BasePageLocators.BASKET_OVERLAY_BTN).click()

    def click_to(self, locator):
        self.browser.find_element(*locator).click()

    def is_element_present(self, locator):
        try:
            self.browser.find_element(*locator)
        except NoSuchElementException:
            return False
        return True

    def is_not_element_present(self, locator):
        try:
            self.browser.find_element(*locator)
        except TimeoutException:
            return True
        return False

    def is_element_displayed(self, locator):
        return self.browser.find_element(*locator).is_displayed()

    def send_string(self, locator, text):
        self.browser.find_element(*locator).send_keys(text)

    def send_string_and_submit(self, locator, text):
        elem = self.browser.find_element(*locator)
        elem.send_keys(text)
        elem.submit()

    def send_string_and_press_enter(self, locator, text):
        elem = self.browser.find_element(*locator)
        elem.send_keys(text)
        elem.send_keys(Keys.ENTER)

