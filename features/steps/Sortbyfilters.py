from behave import *
import os
import logging
from locators import Locators

current_file_name = os.path.basename(__file__)
new_file_name = os.path.splitext(current_file_name)[0] + ".png"


@then(u'click on the filterbutton')
def step_impl(context):
    try:
        context.page.wait_for_selector(Locators.InventoryPage.SORT_DROPDOWN)
        logging.info("Sort dropdown is visible")

    except Exception as e:
        context.page.screenshot(path=f"./{new_file_name}")
        logging.error(f"Error at click on the filterbutton: {e}")
        raise


@step(u'select the "{filter}"')
def step_impl(context, filter):
    try:
        context.page.select_option(Locators.InventoryPage.SORT_DROPDOWN, label=filter)
        context.page.wait_for_timeout(300)
        logging.info(f"Selected filter: {filter}")

    except Exception as e:
        context.page.screenshot(path=f"./{new_file_name}")
        logging.error(f'Error at select the "{filter}": {e}')
        raise


@then(u'Verify the products data is in correct filter from A to Z')
def step_impl(context):
    try:
        names = context.page.locator(Locators.InventoryPage.ITEM_NAME).all_inner_texts()
        assert names == sorted(names), \
            f"Products are not sorted A to Z.\nExpected: {sorted(names)}\nGot: {names}"
        logging.info("Products are correctly sorted A to Z")

    except Exception as e:
        context.page.screenshot(path=f"./{new_file_name}")
        logging.error(f"Error at Verify the products data is in correct filter from A to Z: {e}")
        raise


@then(u'Verify the products data is in correct filter from Z to A')
def step_impl(context):
    try:
        names = context.page.locator(Locators.InventoryPage.ITEM_NAME).all_inner_texts()
        assert names == sorted(names, reverse=True), \
            f"Products are not sorted Z to A.\nExpected: {sorted(names, reverse=True)}\nGot: {names}"
        logging.info("Products are correctly sorted Z to A")

    except Exception as e:
        context.page.screenshot(path=f"./{new_file_name}")
        logging.error(f"Error at Verify the products data is in correct filter from Z to A: {e}")
        raise


@then(u'Verify the products data is in correct filter from Low to High')
def step_impl(context):
    try:
        price_texts = context.page.locator(Locators.InventoryPage.ITEM_PRICE).all_inner_texts()
        prices = [float(p.replace("$", "").strip()) for p in price_texts]
        assert prices == sorted(prices), \
            f"Prices are not sorted low to high.\nExpected: {sorted(prices)}\nGot: {prices}"
        logging.info("Products are correctly sorted by price low to high")

    except Exception as e:
        context.page.screenshot(path=f"./{new_file_name}")
        logging.error(f"Error at Verify the products data is in correct filter from Low to High: {e}")
        raise


@then(u'Verify the products data is in correct filter from High to Low')
def step_impl(context):
    try:
        price_texts = context.page.locator(Locators.InventoryPage.ITEM_PRICE).all_inner_texts()
        prices = [float(p.replace("$", "").strip()) for p in price_texts]
        assert prices == sorted(prices, reverse=True), \
            f"Prices are not sorted high to low.\nExpected: {sorted(prices, reverse=True)}\nGot: {prices}"
        logging.info("Products are correctly sorted by price high to low")

    except Exception as e:
        context.page.screenshot(path=f"./{new_file_name}")
        logging.error(f"Error at Verify the products data is in correct filter from High to Low: {e}")
        raise
