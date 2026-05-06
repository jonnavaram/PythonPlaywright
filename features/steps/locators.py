import random
import string


def random_name(length=6):
    return ''.join(random.choices(string.ascii_letters, k=length))



class Locators:
    class LoginPage:
        USERNAME = "#user-name"
        PASSWORD = "#password"
        LOGIN_BUTTON = "#login-button"
        ERROR_MESSAGE = "h3[data-test='error']"
        ERROR_ICON_USERNAME = "div.login-box div:nth-child(1) svg"
        ERROR_ICON_PASSWORD = "div[class='login_wrapper-inner'] div:nth-child(2) svg path"

    class Header:
        HAMBURGER_MENU = "#react-burger-menu-btn"
        LOGOUT_BUTTON = "#logout_sidebar_link"
        CART_LINK = ".shopping_cart_link"
        CART_BADGE = ".shopping_cart_badge"
        ALL_ITEMS = "#inventory_sidebar_link"
        ABOUT = "#about_sidebar_link"
        RESET_APP_STATE = "#reset_sidebar_link"

    class InventoryPage:
        INVENTORY_ITEM = ".inventory_item"
        ITEM_NAME = ".inventory_item_name"
        ITEM_DESC = ".inventory_item_desc"
        BACKPACK_TITLE_LINK = "a#item_4_title_link .inventory_item_name"
        BACKPACK_NAME = "a[id='item_4_title_link'] div[class='inventory_item_name ']"
        ADD_TO_CART_BACKPACK = "#add-to-cart-sauce-labs-backpack"
        REMOVE_BACKPACK = "#remove-sauce-labs-backpack"
        ADD_TO_CART_BUTTONS = "button[id^='add-to-cart']"
        REMOVE_BUTTONS = "button[id^='remove']"
        BACK_TO_PRODUCTS = "#back-to-products"
        DETAIL_ADD_TO_CART = "#add-to-cart"
        DETAIL_REMOVE = "#remove"
        ITEM_PRICE = ".inventory_item_price"
        SORT_DROPDOWN = ".product_sort_container"
        ADD_TO_CART_BIKE_LIGHT = "#add-to-cart-sauce-labs-bike-light"
        BIKE_LIGHT_NAME = "a[id='item_0_title_link'] div[class='inventory_item_name ']"

    class ProductDetail:
        NAME = ".inventory_details_name"
        PRICE = ".inventory_details_price"
        DESC = ".inventory_details_desc"
        IMAGE = ".inventory_details_img"

    class CartPage:
        ITEM_NAME = ".inventory_item_name"
        ITEM_PRICE = ".inventory_item_price"
        CONTINUE_SHOPPING = "#continue-shopping"
        CART_ITEMS = ".cart_item"
        REMOVE_BUTTONS = "button[id^='remove']"
        TITLE = ".title"
        
    class Checkout:
        CHECKOUTBUTT = "#checkout"
        FIRSTNAME = "#first-name"
        LASTNAME = "#last-name"
        POSTALCODE = "#postal-code"
        CONTINUE_BUTTON = "#continue"
        CART_ITEMS = ".cart_item"
        ITEM_TOTAL = ".summary_subtotal_label"
        CANCEL_BUTTON = "#cancel"
        ERROR_BUTTON = ".error-button"
        ERROR_MESSAGE = "h3[data-test='error']"
        SUBTOTAL = ".summary_subtotal_label"
        FINISH_BUTTON = "#finish"
        TAX_LABEL = ".summary_tax_label"
        TOTAL_LABEL = ".summary_total_label"
        PAYMENT_INFO_LABELS = ".summary_info_label"

    class CheckoutComplete:
        COMPLETE_HEADER = ".complete-header"
        COMPLETE_TEXT = ".complete-text"
        BACK_HOME_BUTTON = "#back-to-products"
        PONY_IMAGE = ".pony_express"

    class Footer:
        TWITTER_LINK = ".social_twitter a"
        FACEBOOK_LINK = ".social_facebook a"
        LINKEDIN_LINK = ".social_linkedin a"
        COPYRIGHT = ".footer_copy"


