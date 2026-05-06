from behave import *
import os
import logging
from locators import Locators, random_name

current_file_name = os.path.basename(__file__)
new_file_name = os.path.splitext(current_file_name)[0] + ".png"


@step(u'leave the last name and postal code filled but first name empty')
def step_impl(context):
    try:
        context.page.fill(Locators.Checkout.FIRSTNAME, "")
        context.page.fill(Locators.Checkout.LASTNAME, random_name())
        context.page.fill(Locators.Checkout.POSTALCODE, random_name(5))
        logging.info("Filled last name and postal code, left first name empty")

    except Exception as e:
        context.page.screenshot(path=f"./{new_file_name}")
        logging.error(f"Error at leave the last name and postal code filled but first name empty: {e}")
        raise


@step(u'leave the first name and postal code filled but last name empty')
def step_impl(context):
    try:
        context.page.fill(Locators.Checkout.FIRSTNAME, random_name())
        context.page.fill(Locators.Checkout.LASTNAME, "")
        context.page.fill(Locators.Checkout.POSTALCODE, random_name(5))
        logging.info("Filled first name and postal code, left last name empty")

    except Exception as e:
        context.page.screenshot(path=f"./{new_file_name}")
        logging.error(f"Error at leave the first name and postal code filled but last name empty: {e}")
        raise


@step(u'leave the first name and last name filled but postal code empty')
def step_impl(context):
    try:
        context.page.fill(Locators.Checkout.FIRSTNAME, random_name())
        context.page.fill(Locators.Checkout.LASTNAME, random_name())
        context.page.fill(Locators.Checkout.POSTALCODE, "")
        logging.info("Filled first name and last name, left postal code empty")

    except Exception as e:
        context.page.screenshot(path=f"./{new_file_name}")
        logging.error(f"Error at leave the first name and last name filled but postal code empty: {e}")
        raise


@then(u'user should see a checkout error message containing "{text}"')
def step_impl(context, text):
    try:
        error_locator = context.page.locator(Locators.Checkout.ERROR_MESSAGE)
        error_locator.wait_for(state="visible", timeout=3000)
        error_text = error_locator.inner_text()
        assert text in error_text, f"Expected error containing '{text}' but got '{error_text}'"
        logging.info(f"Checkout error message verified: '{error_text}'")

    except Exception as e:
        context.page.screenshot(path=f"./{new_file_name}")
        logging.error(f"Error at user should see a checkout error message containing '{text}': {e}")
        raise


@then(u'dismiss the checkout error message')
def step_impl(context):
    try:
        context.page.click(Locators.Checkout.ERROR_BUTTON)
        logging.info("Checkout error message dismissed")

    except Exception as e:
        context.page.screenshot(path=f"./{new_file_name}")
        logging.error(f"Error at dismiss the checkout error message: {e}")
        raise


@then(u'the checkout error message should not be visible')
def step_impl(context):
    try:
        error_locator = context.page.locator(Locators.Checkout.ERROR_MESSAGE)
        assert error_locator.count() == 0 or not error_locator.is_visible(), \
            "Checkout error message is still visible after dismissal"
        logging.info("Checkout error message is no longer visible")

    except Exception as e:
        context.page.screenshot(path=f"./{new_file_name}")
        logging.error(f"Error at the checkout error message should not be visible: {e}")
        raise
