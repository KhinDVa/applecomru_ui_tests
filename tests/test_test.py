import pytest
import allure
from pages.base_page import BasePage
from pages import links

'''Здесь просто проверяется, что все падения правильно отрабатываются аллюром, скриншоты создаются и прикрепляются'''

@pytest.fixture()
def page(browser):
    page = BasePage(browser, links.MAIN_PAGE)
    with allure.step(f'Открываем {links.MAIN_PAGE}'):
        page.open()
        return page

@allure.title('Главная не главная')
@allure.feature('Test')
@allure.severity(allure.severity_level.TRIVIAL)
def test_nomain(page):
    assert page.browser.title == '42'


