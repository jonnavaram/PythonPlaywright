from behave import *
import os
import logging
from locators import Locators

current_file_name = os.path.basename(__file__)
new_file_name = os.path.splitext(current_file_name)[0] + ".png"


@step(u'click on the All Items link')
def step_impl(context):
    try:
        context.page.click(Locators.Header.ALL_ITEMS)
        logging.info("Successfully clicked on All Items link")

    except Exception as e:
        context.page.screenshot(path=f"./{new_file_name}")
        logging.error(f"Error at click on the All Items link: {e}")
        raise


@step(u'click on the About link')
def step_impl(context):
    try:
        context.page.click(Locators.Header.ABOUT)
        context.page.wait_for_load_state("domcontentloaded", timeout=10000)
        logging.info("Successfully clicked on About link")

    except Exception as e:
        context.page.screenshot(path=f"./{new_file_name}")
        logging.error(f"Error at click on the About link: {e}")
        raise


@step(u'click on the Reset App State link')
def step_impl(context):
    try:
        context.page.click(Locators.Header.RESET_APP_STATE)
        context.page.wait_for_timeout(500)
        logging.info("Successfully clicked on Reset App State link")

    except Exception as e:
        context.page.screenshot(path=f"./{new_file_name}")
        logging.error(f"Error at click on the Reset App State link: {e}")
        raise


@then(u'the URL should contain "saucelabs.com"')
def step_impl(context):
    try:
        current_url = context.page.url
        assert "saucelabs.com" in current_url, \
            f"Expected URL to contain 'saucelabs.com' but got '{current_url}'"
        logging.info(f"URL correctly contains 'saucelabs.com': {current_url}")

    except Exception as e:
        context.page.screenshot(path=f"./{new_file_name}")
        logging.error(f'Error at the URL should contain "saucelabs.com": {e}')
        raise
    
@then(u'the "Add to cart" button should not be visible for "Sauce Labs Backpack"')
def step_impl(context):
    try:
        text = context.page.locator(Locators.InventoryPage.REMOVE_BACKPACK).inner_text()
        logging.info(f"Add to cart text button should not be visible for Sauce Labs Backpack: {text}")
        assert  text == "Remove"

        
    except Exception as e:
        context.page.screenshot(path=f"./{new_file_name}")
        logging.error(f'Error at the URL should contain "saucelabs.com": {e}')
        raise
        
