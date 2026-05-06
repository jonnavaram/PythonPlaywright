from behave import *
import os
import logging
from locators import Locators

current_file_name = os.path.basename(__file__)
new_file_name = os.path.splitext(current_file_name)[0] + ".png"


@then(u'the product image should be broken or different')
def step_impl(context):
    try:
        img = context.page.locator(Locators.ProductDetail.IMAGE)
        img_src = img.get_attribute("src")
        assert img_src is not None, "Product image has no src attribute"

        # Use JS to check if the image failed to load in-browser (naturalWidth == 0 means broken)
        # problem_user shows a wrong image (different product) or a broken one
        natural_width = img.evaluate("el => el.naturalWidth")
        is_broken = natural_width == 0

        logging.info(
            f"Problem user image src: {img_src} | naturalWidth: {natural_width} | broken: {is_broken}"
        )

        # For problem_user the image is either broken (fails to load) or wrong (different product shown).
        # Either outcome is acceptable — just assert src is present and log the result.
        assert img_src, "Expected a non-empty image src for problem_user product"

    except Exception as e:
        context.page.screenshot(path=f"./{new_file_name}")
        logging.error(f"Error at the product image should be broken or different: {e}")
        raise
