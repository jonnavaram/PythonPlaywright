from behave import *
import os
import logging
from playwright.sync_api import expect
from locators import Locators

current_file_name = os.path.basename(__file__)
new_file_name = os.path.splitext(current_file_name)[0] + ".png"


@then(u'user should see "Sauce Labs Backpack" in the order summary')
def step_impl(context):
    try:
        text = context.page.locator(Locators.InventoryPage.ITEM_NAME).inner_text()
        logging.info(f"User should able to see the {text} product")
        
    except Exception as e:
        context.page.screenshot(path=f"./{new_file_name}")
        logging.error(f'Error at user should see "Sauce Labs Backpack" in the order summary: {e}')
        raise

@then(u'the item price for "Sauce Labs Backpack" should be "$29.99"')
def step_impl(context):
    try:
        price = context.page.locator(Locators.CartPage.ITEM_PRICE).inner_text()
        logging.info(f"User should be able to see the {price} price")
        assert price == "$29.99"
        
    except Exception as e:
        context.page.screenshot(path=f"./{new_file_name}")
        logging.error(f'Error at the item price for "Sauce Labs Backpack" should be "$29.99": {e}')
        raise


@then(u'the item total should be "$29.99"')
def step_impl(context):
    try:
        subtotal = context.page.locator(Locators.Checkout.SUBTOTAL).inner_text()
        logging.info(f"Subtotal price is: {subtotal}")
        assert subtotal == "Item total: $29.99"
        
    except Exception as e:
        context.page.screenshot(path=f"./{new_file_name}")
        logging.error(f'Error at the item total should be "$29.99": {e}')
        raise


@then(u'the tax amount should be visible and greater than "$0.00"')
def step_impl(context):
    try:
        tax_locator = context.page.locator(Locators.Checkout.TAX_LABEL)
        assert tax_locator.is_visible(), "Tax label is not visible"
        tax_text = tax_locator.inner_text()
        amount = float(tax_text.split("$")[-1].strip())
        assert amount > 0.0, f"Tax amount should be greater than $0.00 but got ${amount}"
        logging.info(f"Tax amount is visible and valid: {tax_text}")

    except Exception as e:
        context.page.screenshot(path=f"./{new_file_name}")
        logging.error(f'Error at the tax amount should be visible and greater than "$0.00": {e}')
        raise


@then(u'the grand total should equal the item total plus tax')
def step_impl(context):
    try:
        subtotal_text = context.page.locator(Locators.Checkout.SUBTOTAL).inner_text()
        tax_text = context.page.locator(Locators.Checkout.TAX_LABEL).inner_text()
        total_text = context.page.locator(Locators.Checkout.TOTAL_LABEL).inner_text()

        subtotal = float(subtotal_text.split("$")[-1].strip())
        tax = float(tax_text.split("$")[-1].strip())
        total = float(total_text.split("$")[-1].strip())

        assert abs(total - (subtotal + tax)) < 0.01, \
            f"Grand total ${total} does not equal subtotal ${subtotal} + tax ${tax}"
        logging.info(f"Grand total ${total} correctly equals subtotal ${subtotal} + tax ${tax}")

    except Exception as e:
        context.page.screenshot(path=f"./{new_file_name}")
        logging.error(f"Error at the grand total should equal the item total plus tax: {e}")
        raise


@then(u'I should see the payment information section')
def step_impl(context):
    try:
        labels = context.page.locator(Locators.Checkout.PAYMENT_INFO_LABELS).all_inner_texts()
        assert any("Payment Information" in label for label in labels), \
            f"Payment information section not found. Labels: {labels}"
        logging.info("Payment information section is visible")

    except Exception as e:
        context.page.screenshot(path=f"./{new_file_name}")
        logging.error(f"Error at I should see the payment information section: {e}")
        raise


@then(u'I should see the shipping information section')
def step_impl(context):
    try:
        labels = context.page.locator(Locators.Checkout.PAYMENT_INFO_LABELS).all_inner_texts()
        assert any("Shipping Information" in label for label in labels), \
            f"Shipping information section not found. Labels: {labels}"
        logging.info("Shipping information section is visible")

    except Exception as e:
        context.page.screenshot(path=f"./{new_file_name}")
        logging.error(f"Error at I should see the shipping information section: {e}")
        raise


@then(u'the URL should contain "/inventory.html"')
def step_impl(context):
    try:
        current_url = context.page.url
        assert "/inventory.html" in current_url, \
            f"Expected URL to contain '/inventory.html' but got '{current_url}'"
        logging.info(f"URL correctly contains '/inventory.html': {current_url}")

    except Exception as e:
        context.page.screenshot(path=f"./{new_file_name}")
        logging.error(f'Error at the URL should contain "/inventory.html": {e}')
        raise