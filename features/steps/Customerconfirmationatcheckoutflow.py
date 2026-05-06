from behave import *
import os
import logging
from playwright.sync_api import expect
from locators import Locators

current_file_name = os.path.basename(__file__)
new_file_name = os.path.splitext(current_file_name)[0] + ".png"




@step(u'user enter first name "{firstname}"')
def step_impl(context,firstname):
    try:
        name = context.page.fill(Locators.Checkout.FIRSTNAME, firstname)
        logging.info(f"Entered first name is: {name}")
        
    except Exception as e:
        context.page.screenshot(path=f"./{new_file_name}")
        logging.error(f'Error at user enter first name "{firstname}": {e}')
        raise


@step(u'user enter last name "{lastname}"')
def step_impl(context,lastname):
    try:
        name = context.page.fill(Locators.Checkout.LASTNAME, lastname)
        logging.info(f"Entered last name is: {name}")

        
    except Exception as e:
        context.page.screenshot(path=f"./{new_file_name}")
        logging.error(f'Error at user enter last name "{lastname}": {e}')
        raise

        


@step(u'user enter postal code "{postalcode}"')
def step_impl(context,postalcode):
    try:
        text = context.page.fill(Locators.Checkout.POSTALCODE, postalcode)
        logging.info(f"Entered postal code is: {text}")

        
    except Exception as e:
        context.page.screenshot(path=f"./{new_file_name}")
        logging.error(f'Error at user enter postal code "{postalcode}": {e}')
        raise

        


@step(u'click on the continue button')
def step_impl(context):
    try:
        context.page.click(Locators.Checkout.CONTINUE_BUTTON)
        logging.info("Successfully clicked Continue Button")

        
    except Exception as e:
        context.page.screenshot(path=f"./{new_file_name}")
        logging.error(f"Error at user should be on the cart page: {e}")
        raise

        


@step(u'user at overview page')
def step_impl(context):
    try:
        text = context.page.locator(Locators.CartPage.TITLE).inner_text()
        logging.info(f"User is in {text} page")
        
        
        
    except Exception as e:
        context.page.screenshot(path=f"./{new_file_name}")
        logging.error(f"Error at user at overview page: {e}")
        raise
        


@step(u'the URL should contain "/checkout-step-two.html"')
def step_impl(context):
    try:
        current_url = context.page.url                                                                                           
        assert "/checkout-step-two.html" in current_url, f"Expected URL to contain '/checkout-step-two.html' but got '{current_url}'"
        logging.info(f"URL correctly contains '/checkout-step-two.html': {current_url}")
        
    except Exception as e:
        context.page.screenshot(path=f"./{new_file_name}")
        logging.error(f'Error at the URL should contain "/checkout-step-two.html": {e}')
        raise


@then(u'user should see the error "First Name is required"')
def step_impl(context):
    try:
        text = context.page.locator(Locators.LoginPage.ERROR_MESSAGE).inner_text()
        logging.info(f"Error text is: {text}")
        assert text == "Error: First Name is required"
        
        
    except Exception as e:
        context.page.screenshot(path=f"./{new_file_name}")
        logging.error(f'Error at user should see the error "First Name is required": {e}')
        raise

@then(u'user should see the error "Last Name is required"')
def step_impl(context):
    try:
        text = context.page.locator(Locators.LoginPage.ERROR_MESSAGE).inner_text()
        logging.info(f"Error text is: {text}")
        assert text == "Error: Last Name is required"
        
    except Exception as e:
        context.page.screenshot(path=f"./{new_file_name}")
        logging.error(f'Error at user should see the error "Last Name is required": {e}')
        raise
        


@then(u'user should see the error "Postal Code is required"')
def step_impl(context):
    try:
        text = context.page.locator(Locators.LoginPage.ERROR_MESSAGE).inner_text()
        logging.info(f"Error text is: {text}")
        assert text == "Error: Postal Code is required"

        
    except Exception as e:
        context.page.screenshot(path=f"./{new_file_name}")
        logging.error(f'Error at user should see the error "Postal Code is required": {e}')
        raise
    
@when(u'user click the error close button')
def step_impl(context):
    try:
        context.page.locator(Locators.Checkout.ERROR_BUTTON).click()
        logging.info("Successfully clicked on the error close button")
        
    
    except Exception as e:
        context.page.screenshot(path=f"./{new_file_name}")
        logging.error(f'Error at user click the error close button: {e}')
        raise

@then(u'the error message should not be visible')
def step_impl(context):
    try:
        expect(context.page.locator(Locators.LoginPage.ERROR_MESSAGE)).not_to_be_visible()
        
        
    except Exception as e:
        context.page.screenshot(path=f"./{new_file_name}")
        logging.error(f'Error at the error message should not be visible: {e}')
        raise
        
