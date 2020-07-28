import allure
import pytest
from pages.product_page import ProductPage
from pages.locators import ItemPageLocators
from pages import links


@pytest.mark.parametrize('link', links.ITEM_PAGES_LIST)
class TestItemPages(object):
    @pytest.fixture()
    def page(self, browser, link):
        page = ProductPage(browser, link)
        with allure.step(f'Открываем {link}'):
            page.open()
        return page

    @allure.title('Проверка работы перехода по кнопке купить')
    @allure.severity(allure.severity_level.NORMAL)
    def test_is_buy_page(self, page):
        with allure.step('Переходим по кнопке купить'):
            page.click_to(ItemPageLocators.BUY_BTN)
        with allure.step('Проверяем, что мы на странице конфигуратора'):
            assert page.is_buy_page(page.browser.current_url)
