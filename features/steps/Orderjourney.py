from behave import *
import os
import logging
from locators import Locators, random_name

current_file_name = os.path.basename(__file__)
new_file_name = os.path.splitext(current_file_name)[0] + ".png"


@then(u'add the "Sauce Labs Bike Light" to cart')
def step_impl(context):
    try:
        name = context.page.locator(Locators.InventoryPage.BIKE_LIGHT_NAME).inner_text()
        logging.info(f"Bike Light product name: {name}")
        assert name == "Sauce Labs Bike Light"
        context.page.click(Locators.InventoryPage.ADD_TO_CART_BIKE_LIGHT)
        logging.info("Sauce Labs Bike Light added to cart")

    except Exception as e:
        context.page.screenshot(path=f"./{new_file_name}")
        logging.error(f'Error at add the "Sauce Labs Bike Light" to cart: {e}')
        raise


@then(u'Store the second product data')
def step_impl(context):
    try:
        name = context.page.locator(Locators.InventoryPage.BIKE_LIGHT_NAME).inner_text()
        logging.info(f"Second product name: {name}")
        assert name == "Sauce Labs Bike Light"
        context.page.click(Locators.InventoryPage.ADD_TO_CART_BIKE_LIGHT)
        logging.info("Second product added to cart")

    except Exception as e:
        context.page.screenshot(path=f"./{new_file_name}")
        logging.error(f"Error at Store the second product data: {e}")
        raise


@then(u'Verify the multiple products are added in cart or not')
def step_impl(context):
    try:
        count = context.page.locator(Locators.CartPage.CART_ITEMS).count()
        assert count >= 2, f"Expected at least 2 items in cart but found {count}"
        logging.info(f"Multiple products verified in cart: {count} items")

    except Exception as e:
        context.page.screenshot(path=f"./{new_file_name}")
        logging.error(f"Error at Verify the multiple products are added in cart or not: {e}")
        raise


@step(u'enter the information')
def step_impl(context):
    try:
        context.page.fill(Locators.Checkout.FIRSTNAME, random_name())
        context.page.fill(Locators.Checkout.LASTNAME, random_name())
        context.page.fill(Locators.Checkout.POSTALCODE, random_name(5))
        logging.info("Checkout information entered successfully")

    except Exception as e:
        context.page.screenshot(path=f"./{new_file_name}")
        logging.error(f"Error at enter the information: {e}")
        raise


@then(u'get the payment information and shipping information')
def step_impl(context):
    try:
        labels = context.page.locator(Locators.Checkout.PAYMENT_INFO_LABELS).all_inner_texts()
        assert any("Payment Information" in label for label in labels), \
            "Payment information section not found"
        assert any("Shipping Information" in label for label in labels), \
            "Shipping information section not found"
        logging.info("Payment and shipping information sections verified")

    except Exception as e:
        context.page.screenshot(path=f"./{new_file_name}")
        logging.error(f"Error at get the payment information and shipping information: {e}")
        raise


@then(u'verify the item total amount')
def step_impl(context):
    try:
        subtotal_text = context.page.locator(Locators.Checkout.SUBTOTAL).inner_text()
        assert "$" in subtotal_text, f"Item total not found: '{subtotal_text}'"
        logging.info(f"Item total verified: {subtotal_text}")

    except Exception as e:
        context.page.screenshot(path=f"./{new_file_name}")
        logging.error(f"Error at verify the item total amount: {e}")
        raise


@then(u'add the item total and tax = total bill amount')
def step_impl(context):
    try:
        subtotal_text = context.page.locator(Locators.Checkout.SUBTOTAL).inner_text()
        tax_text = context.page.locator(Locators.Checkout.TAX_LABEL).inner_text()
        total_text = context.page.locator(Locators.Checkout.TOTAL_LABEL).inner_text()

        subtotal = float(subtotal_text.split("$")[-1].strip())
        tax = float(tax_text.split("$")[-1].strip())
        total = float(total_text.split("$")[-1].strip())

        assert abs(total - (subtotal + tax)) < 0.01, \
            f"Total ${total} does not equal subtotal ${subtotal} + tax ${tax}"
        logging.info(f"Total bill verified: ${subtotal} + ${tax} = ${total}")

    except Exception as e:
        context.page.screenshot(path=f"./{new_file_name}")
        logging.error(f"Error at add the item total and tax = total bill amount: {e}")
        raise


@then(u'show the order confirmation page')
def step_impl(context):
    try:
        header = context.page.locator(Locators.CheckoutComplete.COMPLETE_HEADER).inner_text()
        assert "THANK YOU FOR YOUR ORDER" in header.upper(), \
            f"Order confirmation page not shown. Got: '{header}'"
        logging.info(f"Order confirmation page verified: {header}")

    except Exception as e:
        context.page.screenshot(path=f"./{new_file_name}")
        logging.error(f"Error at show the order confirmation page: {e}")
        raise


@then(u'verify that cart badge should not be visible')
def step_impl(context):
    try:
        badge = context.page.locator(Locators.Header.CART_BADGE)
        assert badge.count() == 0, "Cart badge is still visible after order completion"
        logging.info("Cart badge is not visible after order completion")

    except Exception as e:
        context.page.screenshot(path=f"./{new_file_name}")
        logging.error(f"Error at verify that cart badge should not be visible: {e}")
        raise


@step(u'unable to click on the finish button')
def step_impl(context):
    try:
        context.page.click(Locators.Checkout.FINISH_BUTTON)
        context.page.wait_for_timeout(1000)
        current_url = context.page.url
        assert "/checkout-complete.html" not in current_url, \
            "Error user should not be able to complete the order but checkout-complete page was reached"
        logging.info("Finish button did not complete the order as expected for error user")

    except Exception as e:
        context.page.screenshot(path=f"./{new_file_name}")
        logging.error(f"Error at unable to click on the finish button: {e}")
        raise
