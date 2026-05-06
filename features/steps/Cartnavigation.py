from behave import *
from locators import Locators
import logging
import os

current_file_name = os.path.basename(__file__)
new_file_name = os.path.splitext(current_file_name)[0] + ".png"



@then(u'user should be on the cart page')
def step_impl(context):
    try:
        carttext = context.page.locator(Locators.CartPage.TITLE).inner_text()
        assert carttext == "Your Cart",f"User is not in {carttext} page"
        logging.info(f"User is in {carttext} page")

        
    except Exception as e:
        context.page.screenshot(path=f"./{new_file_name}")
        logging.error(f"Error at user should be on the cart page: {e}")
        raise


@then(u'the URL should contain "/cart.html"')
def step_impl(context):
    try:
        current_url = context.page.url                                                                                           
        assert "/cart.html" in current_url, f"Expected URL to contain '/cart.html' but got '{current_url}'"
        logging.info(f"URL correctly contains '/cart.html': {current_url}")


    except Exception as e:
        context.page.screenshot(path=f"./{new_file_name}")
        logging.error(f"Error at user should be on the cart page: {e}")
        raise

@then(u'user is in main page')
def step_impl(context):
    try:
        text = context.page.locator(Locators.CartPage.TITLE).inner_text()
        assert text == "Products",f"User is not in {text} page"
        logging.info(f"User is in {text} page")
        
    except Exception as e:
        context.page.screenshot(path=f"./{new_file_name}")
        logging.error(f"Error at user is in main page: {e}")
        raise


@then(u'user navigate to the cart page again')
def step_impl(context):
    try:
        context.page.click(Locators.Header.CART_LINK)
        carttext = context.page.locator(Locators.CartPage.TITLE).inner_text()
        assert carttext == "Your Cart", f"User is not in {carttext} page"
        logging.info(f"User is in {carttext} page")

    except Exception as e:
        context.page.screenshot(path=f"./{new_file_name}")
        logging.error(f"Error at user navigate to the cart page again: {e}")
        raise


@then(u'user should still see "Sauce Labs Backpack" in the cart')
def step_impl(context):
    try:
        item_names = context.page.locator(Locators.CartPage.ITEM_NAME).all_inner_texts()
        assert "Sauce Labs Backpack" in item_names, f"'Sauce Labs Backpack' not found in cart. Found: {item_names}"
        logging.info("'Sauce Labs Backpack' is still present in the cart")

    except Exception as e:
        context.page.screenshot(path=f"./{new_file_name}")
        logging.error(f"Error at user should still see Sauce Labs Backpack in the cart: {e}")
        raise

@then(u'user should be on the checkout step one page')
def step_impl(context):
    try:
        text = context.page.locator(Locators.CartPage.TITLE).inner_text()
        assert text == "Checkout: Your Information",f"User is not in {text} page"
        logging.info(f"User is in {text} page")
        
    except Exception as e:
        context.page.screenshot(path=f"./{new_file_name}")
        logging.error(f"Error at user should be on the checkout step one page: {e}")
        raise


@then(u'the URL should contain "/checkout-step-one.html"')
def step_impl(context):
    try:
        current_url = context.page.url                                                                                           
        assert "/checkout-step-one.html" in current_url, f"Expected URL to contain '/checkout-step-one.html' but got '{current_url}'"
        logging.info(f"URL correctly contains '/checkout-step-one.html': {current_url}")
        
    except Exception as e:
        context.page.screenshot(path=f"./{new_file_name}")
        logging.error(f'Error at the URL should contain "/checkout-step-one.html": {e}')
        raise
