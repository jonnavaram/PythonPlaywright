from behave import *
import os
import logging
from locators import Locators

current_file_name = os.path.basename(__file__)
new_file_name = os.path.splitext(current_file_name)[0] + ".png"


@when(u'user add "{product_name}" to the cart')
def step_impl(context, product_name):
    try:
        context.page.locator(Locators.InventoryPage.INVENTORY_ITEM).filter(has_text=product_name).locator(Locators.InventoryPage.ADD_TO_CART_BUTTONS).click()
        logging.info(f"Added '{product_name}' to the cart")
        context.page.wait_for_timeout(500)  


    except Exception as e:
        context.page.screenshot(path=f"./{new_file_name}")
        logging.error(f"Error at user add '{product_name}' to the cart: {e}")
        raise


@then(u'user should see "{product_name}" in the cart')
def step_impl(context, product_name):
    try:
        cart_item_names = context.page.locator(Locators.CartPage.ITEM_NAME).all_inner_texts()
        assert product_name in cart_item_names, f"'{product_name}' not found in cart. Found: {cart_item_names}"
        logging.info(f"'{product_name}' is visible in the cart")
        context.page.wait_for_timeout(500)  


    except Exception as e:
        context.page.screenshot(path=f"./{new_file_name}")
        logging.error(f"Error at user should see '{product_name}' in the cart: {e}")
        raise


@then(u'the item price should show "{price}"')
def step_impl(context, price):
    try:
        item_price = context.page.locator(Locators.CartPage.ITEM_PRICE).inner_text()
        assert item_price == price, f"Expected price '{price}' but found '{item_price}'"
        logging.info(f"Item price '{price}' is correctly shown in the cart")
        context.page.wait_for_timeout(500)  


    except Exception as e:
        context.page.screenshot(path=f"./{new_file_name}")
        logging.error(f"Error at the item price should show '{price}': {e}")
        raise
