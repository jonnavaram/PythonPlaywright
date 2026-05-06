from behave import *
import os
import logging
from locators import Locators, random_name

current_file_name = os.path.basename(__file__)
new_file_name = os.path.splitext(current_file_name)[0] + ".png"

@then(u'click on the cancel button')
def step_impl(context):
    try:
        context.page.click(Locators.Checkout.CANCEL_BUTTON)
        logging.info("Successfully clicked on the cancel button")
        
        
    except Exception as e:
        context.page.screenshot(path=f"./{new_file_name}")
        logging.error(f"Error at click on the cancel button: {e}")
        raise
