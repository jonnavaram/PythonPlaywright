from behave import *
import os
import logging
from locators import Locators

current_file_name = os.path.basename(__file__)
new_file_name = os.path.splitext(current_file_name)[0] + ".png"


@then(u'the inventory page should display all 6 products')
def step_impl(context):
    try:
        context.page.wait_for_load_state("domcontentloaded")
        count = context.page.locator(Locators.InventoryPage.INVENTORY_ITEM).count()
        assert count == 6, f"Expected 6 products on inventory page but found {count}"
        logging.info(f"Inventory page displays all {count} products")

    except Exception as e:
        context.page.screenshot(path=f"./{new_file_name}")
        logging.error(f"Error at the inventory page should display all 6 products: {e}")
        raise
