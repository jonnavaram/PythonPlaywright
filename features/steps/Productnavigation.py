from behave import *
import os
import logging
from locators import Locators

current_file_name = os.path.basename(__file__)
new_file_name = os.path.splitext(current_file_name)[0] + ".png"


@step(u'click on the product "{product_name}"')
def step_impl(context, product_name):
    try:
        context.page.click(f".inventory_item_name:has-text('{product_name}')")
        logging.info(f"Successfully clicked on product: {product_name}")

    except Exception as e:
        context.page.screenshot(path=f"./{new_file_name}")
        logging.error(f'Error at click on the product "{product_name}": {e}')
        raise


@then(u'verify it navigates to the correct detail page')
def step_impl(context):
    try:
        current_url = context.page.url
        assert "/inventory-item.html" in current_url, \
            f"Expected URL to contain '/inventory-item.html' but got '{current_url}'"
        logging.info(f"User is on the product detail page: {current_url}")

    except Exception as e:
        context.page.screenshot(path=f"./{new_file_name}")
        logging.error(f"Error at verify it navigates to the correct detail page: {e}")
        raise


@step(u'click on the back to products')
def step_impl(context):
    try:
        context.page.click(Locators.InventoryPage.BACK_TO_PRODUCTS)
        logging.info("Successfully clicked on back to products")

    except Exception as e:
        context.page.screenshot(path=f"./{new_file_name}")
        logging.error(f"Error at click on the back to products: {e}")
        raise


@then(u'click on the add to cart button for "{product_name}"')
def step_impl(context, product_name):
    try:
        context.page.click(Locators.InventoryPage.DETAIL_ADD_TO_CART)
        logging.info(f"Successfully added {product_name} to cart from detail page")

    except Exception as e:
        context.page.screenshot(path=f"./{new_file_name}")
        logging.error(f'Error at click on the add to cart button for "{product_name}": {e}')
        raise


@then(u'the cart should be updated as "{count}"')
def step_impl(context, count):
    try:
        badge = context.page.locator(Locators.Header.CART_BADGE).text_content()
        assert badge == count, f"Expected cart badge '{count}' but got '{badge}'"
        logging.info(f"Cart badge correctly shows: {count}")

    except Exception as e:
        context.page.screenshot(path=f"./{new_file_name}")
        logging.error(f'Error at the cart should be updated as "{count}": {e}')
        raise


@then(u'Verify the full product list is visible')
def step_impl(context):
    try:
        count = context.page.locator(Locators.InventoryPage.INVENTORY_ITEM).count()
        assert count == 6, f"Expected 6 products but found {count}"
        logging.info(f"Full product list is visible with {count} products")

    except Exception as e:
        context.page.screenshot(path=f"./{new_file_name}")
        logging.error(f"Error at Verify the full product list is visible: {e}")
        raise


@then(u'click on the remove button on the detail page')
def step_impl(context):
    try:
        context.page.click(Locators.InventoryPage.DETAIL_REMOVE)
        logging.info("Successfully clicked the remove button on the detail page")

    except Exception as e:
        context.page.screenshot(path=f"./{new_file_name}")
        logging.error(f"Error at click on the remove button on the detail page: {e}")
        raise
