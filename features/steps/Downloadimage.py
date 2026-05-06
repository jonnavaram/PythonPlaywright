from behave import *
import os
import logging
from locators import Locators

current_file_name = os.path.basename(__file__)
new_file_name = os.path.splitext(current_file_name)[0] + ".png"


@step(u'click on the "{product_name}" image')
def step_impl(context, product_name):
    try:
        context.page.locator(Locators.InventoryPage.INVENTORY_ITEM) \
            .filter(has_text=product_name) \
            .locator("img") \
            .first.click()
        logging.info(f"Clicked on image for: {product_name}")

    except Exception as e:
        context.page.screenshot(path=f"./{new_file_name}")
        logging.error(f'Error at click on the "{product_name}" image: {e}')
        raise


@then(u'download the image')
def step_impl(context):
    try:
        img_src = context.page.locator(Locators.ProductDetail.IMAGE).get_attribute("src")
        if img_src.startswith("/"):
            img_src = f"https://www.saucedemo.com{img_src}"

        response = context.page.request.get(img_src)
        assert response.ok, f"Failed to fetch image. Status: {response.status}"

        filename = img_src.split("/")[-1].split("?")[0]
        with open(f"./{filename}", "wb") as f:
            f.write(response.body())

        logging.info(f"Image downloaded successfully: {filename}")

    except Exception as e:
        context.page.screenshot(path=f"./{new_file_name}")
        logging.error(f"Error at download the image: {e}")
        raise
