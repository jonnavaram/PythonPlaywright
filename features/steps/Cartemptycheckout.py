from behave import *
import os
import logging
from locators import Locators, random_name

current_file_name = os.path.basename(__file__)
new_file_name = os.path.splitext(current_file_name)[0] + ".png"


@then(u'click on the checkout button')
def step_impl(context):
    try:
        context.page.click(Locators.Checkout.CHECKOUTBUTT)
        logging.info("Successfully clicked on the checkout button")

    except Exception as e:
        context.page.screenshot(path=f"./{new_file_name}")
        logging.error(f"Error at click on the checkout button: {e}")
        raise


@then(u'user fill the valid checkout information')
def step_impl(context):
    try:
        context.page.fill(Locators.Checkout.FIRSTNAME, random_name())
        context.page.fill(Locators.Checkout.LASTNAME, random_name())
        context.page.fill(Locators.Checkout.POSTALCODE, random_name(5))
        context.page.click(Locators.Checkout.CONTINUE_BUTTON)
        logging.info("Successfully filled checkout information and clicked Continue")

    except Exception as e:
        context.page.screenshot(path=f"./{new_file_name}")
        logging.error(f"Error at user fill the valid checkout information: {e}")
        raise


@then(u'the order summary should show no items')
def step_impl(context):
    try:
        count = context.page.locator(Locators.Checkout.CART_ITEMS).count()
        assert count == 0, f"Expected no items in order summary but found {count}"
        logging.info("Order summary shows no items as expected")

    except Exception as e:
        context.page.screenshot(path=f"./{new_file_name}")
        logging.error(f"Error at the order summary should show no items: {e}")
        raise


@then(u'the item total should show "$0"')
def step_impl(context):
    try:
        item_total_text = context.page.locator(Locators.Checkout.ITEM_TOTAL).inner_text()
        amount = item_total_text.split(": ", 1)[-1].strip()
        assert amount == "$0", f"Expected item total '$0' but found '{amount}'"
        logging.info(f"Item total correctly shows $0: '{item_total_text}'")

    except Exception as e:
        context.page.screenshot(path=f"./{new_file_name}")
        logging.error(f"Error at the item total should show '$0': {e}")
        raise
    
@then(u'the cart item list should be empty')
def step_impl(context):
    try:
        context.page.click(Locators.Header.CART_LINK)
        context.page.wait_for_load_state("domcontentloaded")
        count = context.page.locator(Locators.CartPage.CART_ITEMS).count()
        assert count == 0, f"Expected cart to be empty but found {count} item(s)"
        logging.info("Cart item list is empty as expected")

    except Exception as e:
        context.page.screenshot(path=f"./{new_file_name}")
        logging.error(f"Error at the cart item list should be empty: {e}")
        raise


@then(u'"Remove" buttons should not be visible')
def step_impl(context):
    try:
        count = context.page.locator(Locators.CartPage.REMOVE_BUTTONS).count()
        assert count == 0, f"Expected no Remove buttons but found {count}"
        logging.info("No Remove buttons are visible as expected")

    except Exception as e:
        context.page.screenshot(path=f"./{new_file_name}")
        logging.error(f'Error at "Remove" buttons should not be visible: {e}')
        raise
