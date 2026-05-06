from behave import *
import logging
import os
from locators import Locators

current_file_name = os.path.basename(__file__)
new_file_name = os.path.splitext(current_file_name)[0] + ".png"


@then(u'Store the first product data')
def step_impl(context):
    try:
        text = context.page.locator(Locators.InventoryPage.BACKPACK_TITLE_LINK).text_content()
        logging.info(f"Product name is: {text}")
        desc = context.page.locator(Locators.InventoryPage.ITEM_DESC).first.inner_text()
        logging.info(f"Product description is: {desc}")
        
    except Exception as e:
        context.page.screenshot(f"./{new_file_name}")
        logging.info(f"Error occured at Store the first product data: {e}")
        raise

        
@then(u'click on the add to cart button')
def step_impl(context):
    try:
        context.page.click(Locators.InventoryPage.ADD_TO_CART_BACKPACK)
        logging.info(f"Successfully clicked on add to cart button")
        
        
    except Exception as e:
        context.page.screenshot(f"./{new_file_name}")
        logging.info(f"Error occured at click on the add to cart button: {e}")
        raise
        


@then(u'the cart badge should show "{count}"')
def step_impl(context, count):
    try:
        badge = context.page.locator(Locators.Header.CART_BADGE).text_content()
        assert badge == count, f"Expected cart badge to show '{count}' but got '{badge}'"
        logging.info(f"Cart badge correctly shows: {count}")

    except Exception as e:
        context.page.screenshot(f"./{new_file_name}")
        logging.info(f'Error at the cart badge should show "{count}": {e}')
        raise


@then(u'verify the cart is updated or not')
def step_impl(context):
    try:
        updatedcart = context.page.locator(Locators.Header.CART_BADGE).text_content()
        logging.info(f"updated cart count is: {updatedcart}")
        assert "1" == updatedcart, "Cart is not updated"
        logging.info("Cart is updated")
        
        
    
    except Exception as e:
        context.page.screenshot(f"./{new_file_name}")
        logging.info(f"Error occured at verify the cart is updated or not: {e}")
        raise