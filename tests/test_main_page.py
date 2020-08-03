from pages.main_page import MainPage
import allure
import pytest
from pages.locators import BasePageLocators
from pages.locators import SearchPageLocators
from pages import links


@pytest.fixture()
def page(browser):
    page = MainPage(browser, links.MAIN_PAGE)
    with allure.step(f'Открываем {links.MAIN_PAGE}'):
        page.open()
    return page


@allure.title('Гость находится на главной странице')
@allure.severity(allure.severity_level.NORMAL)
def test_guest_on_main_page(page):
    with allure.step("Проверка на главной ли странице гость"):
        assert page.browser.title == 'Apple (Россия) – Официальный сайт', 'Пользователь не на главной странице'


@allure.title('Гость может перейти в корзину')
@allure.severity(allure.severity_level.NORMAL)
def test_guest_can_go_to_checkout(page):
    with allure.step('Переход в корзину'):
        page.go_to_basket()
    with allure.step('Проверка, что гость находится в корзине'):
        assert '/shop/bag' in page.browser.current_url, \
            f'Ожидалась страница корзины, открылась {page.browser.current_url}'


@allure.title('Проверка работы кнопок топ-бара')
@allure.feature('Parametrized')
@allure.severity(allure.severity_level.NORMAL)
@pytest.mark.parametrize('param_btn', [[BasePageLocators.HOME_PAGE_ICON, links.MAIN_PAGE],
                                       [BasePageLocators.MAC_TOP_MENU_BTN, links.MAC_PAGE],
                                       [BasePageLocators.IPHONE_TOP_MENU_BTN, links.IPHONE_PAGE],
                                       [BasePageLocators.IPAD_TOP_MENU_BTN, links.IPAD_PAGE],
                                       [BasePageLocators.WATCH_TOP_MENU_BTN, links.WATCH_PAGE],
                                       [BasePageLocators.TV_TOP_MENU_BTN, links.TV_PAGE],
                                       [BasePageLocators.MUSIC_TOP_MENU_BTN, links.MUSIC_PAGE],
                                       [BasePageLocators.SUPPORT_TOP_MENU_BTN, links.SUPPORT_PAGE]])
def test_top_bar_btns_working(page, param_btn):
    with allure.step(f'Переход по кнопке {param_btn[0]}'):
        page.click_to(param_btn[0])
    with allure.step('Проверка что переход произошел на нужную страницу'):
        assert page.browser.current_url == param_btn[1], f'Ожидался переход на {param_btn[1]}, но произошел переход ' \
                                                         f'на {page.browser.current_url}'


@allure.title('Проверка отображения поисковой строки')
@allure.severity(allure.severity_level.NORMAL)
def test_search_bar_is_displayed(page):
    with allure.step('Кликаем по иконке поиска'):
        page.click_to(BasePageLocators.SEARCH_TOP_MENU_BTN)
    with allure.step('Проверяем появилось ли поле поиска'):
        assert page.is_element_present(BasePageLocators.SEARCH_BAR), 'Поле поиска остутствует'


@allure.title('Проверка работы поиска')
@allure.severity(allure.severity_level.NORMAL)
@pytest.mark.parametrize('param_search_text', ['apple', 'iphone', 'mac'])
def test_search_is_working_right(page, param_search_text):
    with allure.step('Кликаем по иконке поиска'):
        page.click_to(BasePageLocators.SEARCH_TOP_MENU_BTN)
    with allure.step(f'Вводим {param_search_text}'):
        page.send_string_and_press_enter(BasePageLocators.SEARCH_BAR, param_search_text)
    with allure.step('Проверяем что поисковая выдача работает'):
        assert page.is_element_present(SearchPageLocators.SEARCH_ORGANIC_LIST), 'Поисковой выдачи нет'


@allure.title('Переход на страницу входа в аккаунт')
@allure.severity(allure.severity_level.NORMAL)
def test_guest_can_go_signin(page):
    with allure.step('Кликаем по меню в топ-баре'):
        page.click_to(BasePageLocators.BAG_TOP_MENU_BTN)
    with allure.step('Кликаем на кнопку войти в меню'):
        page.click_to(BasePageLocators.SIGNIN_OVERLAY_BTN)
    with allure.step('Проверяем что пользователь находится на странице входа в аккаунт'):
        assert '/shop/sign_in' in page.browser.current_url, f'Ожидалась страница с /shop/sign_in, по факту' \
                                                            f'{page.browser.current_url}'