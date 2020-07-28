import pytest
import allure
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

#
# def pytest_addoption(parser):
#     parser.addoption('--language', action='store', default='ru',
#                     help='Choose language')
#
#
# @pytest.fixture(scope='function')
# def browser(request):
#     print('\nStarting chrome browser for testing...')
#     options = Options()
#     options.add_experimental_option('prefs', {'intl.accept_language:': request.config.getoption('language')})
#     options.add_argument('start-maximized')
#     browser = webdriver.Chrome(options=options)
#     yield browser
#     print('\n...clothing chrome browser.')
#     browser.quit()


capabilities = {
    "browserName": "chrome",
    "version": "83.0",
    "enableVNC": True,
    "enableVideo": False
}

@pytest.fixture(scope='function')
def browser():
    with allure.step('Запускаем браузер'):
        browser = webdriver.Remote(command_executor="http://localhost:4444/wd/hub", desired_capabilities=capabilities)
        browser.maximize_window()
        browser.implicitly_wait(10)
    yield browser
    with allure.step('Закрываем браузер'):
        browser.quit()


