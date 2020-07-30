import pytest

MAIN_PAGE = 'https://www.apple.com/ru/'
MAC_PAGE = 'https://www.apple.com/ru/mac/'
IPAD_PAGE = 'https://www.apple.com/ru/ipad/'
IPHONE_PAGE = 'https://www.apple.com/ru/iphone/'
WATCH_PAGE = 'https://www.apple.com/ru/watch/'
TV_PAGE = 'https://www.apple.com/ru/tv/'
MUSIC_PAGE = 'https://www.apple.com/ru/music/'
SUPPORT_PAGE = 'https://support.apple.com/ru-ru'

ITEM_PAGES_LIST = ['https://www.apple.com/ru/macbook-pro-13/',
                   'https://www.apple.com/ru/ipad-pro/',
                   'https://www.apple.com/ru/iphone-11-pro/',
                   pytest.param('https://www.apple.com/ru/', marks=pytest.mark.xfail(
                       reason='Тест не должен проходить'))]
