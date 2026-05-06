from behave import *
import os
import logging
from locators import Locators

current_file_name = os.path.basename(__file__)
new_file_name = os.path.splitext(current_file_name)[0] + ".png"


@then(u'user should see the product name "{product_name}"')
def step_impl(context, product_name):
    try:
        name = context.page.locator(Locators.ProductDetail.NAME).inner_text()
        assert product_name in name, \
            f"Expected product name '{product_name}' but got '{name}'"
        logging.info(f"Product name verified: {name}")

    except Exception as e:
        context.page.screenshot(path=f"./{new_file_name}")
        logging.error(f'Error at user should see the product name "{product_name}": {e}')
        raise


@then(u'user should see the product price "{price}"')
def step_impl(context, price):
    try:
        displayed_price = context.page.locator(Locators.ProductDetail.PRICE).inner_text()
        assert price in displayed_price, \
            f"Expected price '{price}' but got '{displayed_price}'"
        logging.info(f"Product price verified: {displayed_price}")

    except Exception as e:
        context.page.screenshot(path=f"./{new_file_name}")
        logging.error(f'Error at user should see the product price "{price}": {e}')
        raise
