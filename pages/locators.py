from selenium.webdriver.common.by import By


class BasePageLocators():
    HOME_PAGE_ICON = (By.CSS_SELECTOR, '#ac-gn-firstfocus')
    MAC_TOP_MENU_BTN = (By.CSS_SELECTOR, '.ac-gn-link-mac')
    IPAD_TOP_MENU_BTN = (By.CSS_SELECTOR, '.ac-gn-link-ipad')
    IPHONE_TOP_MENU_BTN = (By.CSS_SELECTOR, '.ac-gn-link-iphone')
    WATCH_TOP_MENU_BTN = (By.CSS_SELECTOR, '.ac-gn-link-watch')
    TV_TOP_MENU_BTN = (By.CSS_SELECTOR, '.ac-gn-link-tv')
    MUSIC_TOP_MENU_BTN = (By.CSS_SELECTOR, '.ac-gn-link-music')
    SUPPORT_TOP_MENU_BTN = (By.CSS_SELECTOR, '.ac-gn-link-support')
    SEARCH_TOP_MENU_BTN = (By.CSS_SELECTOR, '#ac-gn-link-search')
    BAG_TOP_MENU_BTN = (By.CSS_SELECTOR, '#ac-gn-bag')
    BASKET_OVERLAY_BTN = (By.CSS_SELECTOR, '.ac-gn-bagview-nav-link-bag')
    FAVOURITE_OVERLAY_BTN = (By.CSS_SELECTOR, '.ac-gn-bagview-nav-item-favorites')
    ORDERS_OVERLAY_BTN = (By.CSS_SELECTOR, '.ac-gn-bagview-nav-item-orders')
    ACCOUNT_OVERLAY_BTN = (By.CSS_SELECTOR, '.ac-gn-bagview-nav-item-account')
    SIGNIN_OVERLAY_BTN = (By.CSS_SELECTOR, '.ac-gn-bagview-nav-item-signIn')
    SEARCH_BAR = (By.CSS_SELECTOR, '#ac-gn-searchform-input')

class ItemPageLocators():
    BUY_BTN = (By.CSS_SELECTOR, '.ac-ln-action-button')


class MacPageLocators():
    MACBOOK_AIR_BTN = (By.CLASS_NAME, 'chapternav-item-macbook-air')
    MACBOOK_PRO13_BTN = (By.CLASS_NAME, 'chapternav-item-macbook-pro-13')
    MACBOOK_PRO16_BTN = (By.CLASS_NAME, 'chapternav-item-macbook-pro-16')
    IMAC_BTN = (By.CLASS_NAME, 'chapternav-item-imac')
    IMAC_PRO_BTN = (By.CLASS_NAME, 'chapternav-item-imac-pro')
    MAC_PRO_BTN = (By.CLASS_NAME, 'chapternav-item-mac-pro')
    MAC_MINI_BTN = (By.CLASS_NAME, 'chapternav-item-mac-mini')
    COMPARE_MAC_BTN = (By.CLASS_NAME, 'chapternav-item-compare')
    PRO_DISPLAY_XDR_BTN = (By.CLASS_NAME, 'chapternav-item-pro-display-xdr')
    ACCESSORIES_MAC_BTN = (By.CLASS_NAME, 'chapternav-item-accessories')
    MACOS_BTN = (By.CLASS_NAME, 'chapternav-item-macos')


class IpadPageLocators():
    IPAD_PRO_BTN = (By.CLASS_NAME, 'chapternav-item-ipad-pro')
    IPAD_AIR_BTN = (By.CLASS_NAME, 'chapternav-item-ipad-air')
    IPAD_BTN = (By.CLASS_NAME, 'chapternav-item-ipad')
    IPAD_MINI_BTN = (By.CLASS_NAME, 'chapternav-item-ipad-mini')
    COMPARE_BTN = (By.CLASS_NAME, 'chapternav-item-compare')
    APPLE_PENCIL_BTN = (By.CLASS_NAME, 'chapternav-item-apple-pencil')
    KEYBOARD_BTN = (By.CLASS_NAME, 'chapternav-item-keyboard')
    AIRPODS_BTN = (By.CLASS_NAME, 'chapternav-item-airpods')
    ACCESSORIES_BTN = (By.CLASS_NAME, 'chapternav-item-accessories')
    IPADOS_BTN = (By.CLASS_NAME, 'chapternav-item-ipados')


class IphonePageLocators():
    IPHONE11PRO_BTN = (By.CLASS_NAME, 'chapternav-item-iphone-11-pro')
    IPHONE11_BTN = (By.CLASS_NAME, 'chapternav-item-iphone-11')
    IPHONE_SE_BTN = (By.CLASS_NAME, 'chapternav-item-iphone-se')
    IPHONE_XR_BTN = (By.CLASS_NAME, 'chapternav-item-iphone-xr')
    COMPARE_IPHONE_BTN = (By.CLASS_NAME, 'chapternav-item-compare')
    AIRPODS_BTN = (By.CLASS_NAME, 'chapternav-item-airpods')
    ACCESSORIES_IPHONE_BTN = (By.CLASS_NAME, 'chapternav-item-accessories')
    IOS_BTN = (By.CLASS_NAME, 'chapternav-item-ios')


class WatchPageLocators():
    WATCH_SERIES5_BTN = (By.CLASS_NAME, 'chapternav-item-series-5')
    WATCH_NIKE_BTN = (By.CLASS_NAME, 'chapternav-item-nike')
    WATCH_SERIES3_BTN = (By.CLASS_NAME, 'chapternav-item-series-3')
    COMPARE_WATCH_BTN = (By.CLASS_NAME, 'chapternav-item-compare')
    BANDS_BTN = (By.CLASS_NAME, 'chapternav-item-bands')
    AIRPODS_BTN = (By.CLASS_NAME, 'chapternav-item-airpods')
    ACCESSORIES_BTN = (By.CLASS_NAME, 'chapternav-item-accessories')
    WATCHOS_BTN = (By.CLASS_NAME, 'chapternav-item-watchos')


class TvPageLocators():
    TV_PLUS_BTN = (By.CLASS_NAME, 'chapternav-item-tv-plus')
    TV_APP_BTN = (By.CLASS_NAME, 'chapternav-item-tv-app')
    TV_4K_BTN = (By.CLASS_NAME, 'chapternav-item-tv-4k')
    TV_HD_BTN = (By.CLASS_NAME, 'chapternav-item-tv-hd')
    AIRPLAY_BTN = (By.CLASS_NAME, 'chapternav-item-airplay')
    ACCESSORIES_BTN = (By.CLASS_NAME, 'chapternav-item-accessories')


class MusicPageLocators():
    APPLE_MUSIC_BTN = (By.CLASS_NAME, 'chapternav-item-apple-music')
    AIRPODS_PRO_BTN = (By.CLASS_NAME, 'chapternav-item-airpods-pro')
    AIRPODS_BTN = (By.CLASS_NAME, 'chapternav-item-airpods')
    IPOD_BTN = (By.CLASS_NAME, 'chapternav-item-ipod-touch')
    BEATS_BTN = (By.CLASS_NAME, 'chapternav-item-beats')
    MUSIC_ACCESSORIES_BTN = (By.CLASS_NAME, 'chapternav-item-music-accessories')
    GIFT_CARD_BTN = (By.CLASS_NAME, 'chapternav-item-gift-cards')


class SearchPageLocators():
    SEARCH_ORGANIC_LIST = (By.CSS_SELECTOR, '.as-explore-organic')


class SigninPageLocators():
    SIGNIN_FORM = (By.CSS_SELECTOR, '.rs-signin')