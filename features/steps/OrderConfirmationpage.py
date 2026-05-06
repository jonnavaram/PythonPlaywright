from behave import *
import os
import logging
from locators import Locators

current_file_name = os.path.basename(__file__)
new_file_name = os.path.splitext(current_file_name)[0] + ".png"


@step(u'click on the finish button')
def step_impl(context):
    try:
        context.page.click(Locators.Checkout.FINISH_BUTTON)
        logging.info("Successfully clicked on the finish button")

    except Exception as e:
        context.page.screenshot(path=f"./{new_file_name}")
        logging.error(f"Error at click on the finish button: {e}")
        raise


@then(u'I should see the "THANK YOU FOR YOUR ORDER!" heading')
def step_impl(context):
    try:
        header_text = context.page.locator(Locators.CheckoutComplete.COMPLETE_HEADER).inner_text()
        logging.info(f"Confirmation header text: {header_text}")
        assert "THANK YOU FOR YOUR ORDER" in header_text.upper(), \
            f"Expected thank you heading but got: '{header_text}'"

    except Exception as e:
        context.page.screenshot(path=f"./{new_file_name}")
        logging.error(f'Error at I should see the "THANK YOU FOR YOUR ORDER!" heading: {e}')
        raise


@then(u'I should see the order dispatched confirmation text')
def step_impl(context):
    try:
        text = context.page.locator(Locators.CheckoutComplete.COMPLETE_TEXT).inner_text()
        logging.info(f"Confirmation text: {text}")
        assert len(text) > 0, "Order dispatched confirmation text is empty"

    except Exception as e:
        context.page.screenshot(path=f"./{new_file_name}")
        logging.error(f"Error at I should see the order dispatched confirmation text: {e}")
        raise


@step(u'click on the back home button')
def step_impl(context):
    try:
        context.page.click(Locators.CheckoutComplete.BACK_HOME_BUTTON)
        logging.info("Successfully clicked on the back home button")

    except Exception as e:
        context.page.screenshot(path=f"./{new_file_name}")
        logging.error(f"Error at click on the back home button: {e}")
        raise


@then(u'the URL should contain "/checkout-complete.html"')
def step_impl(context):
    try:
        current_url = context.page.url
        assert "/checkout-complete.html" in current_url, \
            f"Expected URL to contain '/checkout-complete.html' but got '{current_url}'"
        logging.info(f"URL correctly contains '/checkout-complete.html': {current_url}")

    except Exception as e:
        context.page.screenshot(path=f"./{new_file_name}")
        logging.error(f'Error at the URL should contain "/checkout-complete.html": {e}')
        raise
