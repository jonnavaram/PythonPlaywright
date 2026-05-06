from behave import *
import os
import logging
from locators import Locators

current_file_name = os.path.basename(__file__)
new_file_name = os.path.splitext(current_file_name)[0] + ".png"


@then(u'click on the remove button')
def step_impl(context):
    try:
        context.page.click(Locators.InventoryPage.REMOVE_BACKPACK)
        logging.info("Successfully clicked on remove button")
        
        
    except Exception as e:
        context.page.screenshot(path=f"./{new_file_name}")
        logging.info(f"Error occured at click on the remove button: {e}")
        raise
        
@then(u'verify the cart count is decreased or not')
def step_impl(context):
    try:
        badge = context.page.locator(Locators.Header.CART_BADGE)
        updatedcart = badge.text_content() if badge.count() > 0 else "0"
        assert updatedcart == "0", f"Cart not updated, found: {updatedcart}"
        
    except Exception as e:
        context.page.screenshot(path=f"./{new_file_name}")
        logging.info(f"Error occured at verify the cart count is decreased or not: {e}")
        raise
    
@then(u'add the "Sauce Labs Backpack" to cart')
def step_impl(context):
    try:
        global product_name
        proname = context.page.locator(Locators.InventoryPage.BACKPACK_NAME)
        product_name = proname.inner_text()
        logging.info(f"Product name is:{product_name}")
        assert product_name == "Sauce Labs Backpack"
        
        context.page.click(Locators.InventoryPage.ADD_TO_CART_BACKPACK)



    except Exception as e:
        context.page.screenshot(path=f"./{new_file_name}")
        logging.info(f'Error occured at add the "Sauce Labs Backpack" to cart: {e}')
        raise 

@then(u'click on the cart button')
def step_impl(context):
    try:
        context.page.wait_for_timeout(500)  

        context.page.click(Locators.Header.CART_LINK)
        logging.info("Successfully clicked on the cart button")
        context.page.wait_for_timeout(500)  

        
    
    except Exception as e:
        context.page.screenshot(path=f"./{new_file_name}")
        logging.info(f'Error occured at click on the cart button: {e}')
        raise 
    
    
@then(u'Verify the product data and cart data same or not')
def step_impl(context):
    try:
        global product_name

        cartproname = context.page.locator(Locators.CartPage.ITEM_NAME).inner_text()
        logging.info(f"Cart product name is: {cartproname}")
        assert product_name == cartproname, "Product name from main page and cart product name are different"
        logging.info("Product name from main page and cart product name are same")
        
        
    
    except Exception as e:
        context.page.screenshot(path=f"./{new_file_name}")
        logging.info(f'Error occured at Verify the product data and cart data same or not: {e}')
        raise 
    
@then(u'click on the continue shopping button')
def step_impl(context):
    try:
        context.page.click(Locators.CartPage.CONTINUE_SHOPPING)
        logging.info("Successfully clicked on the continue shopping button")
        
        
    except Exception as e:
        context.page.screenshot(path=f"./{new_file_name}")
        logging.info(f'Error occured at click on the continue shopping button: {e}')
        raise 
        
    
    
@then(u'the "Add to cart" button should be visible for "Sauce Labs Backpack"')
def step_impl(context):
    try:
        addtocarttext = context.page.locator(Locators.InventoryPage.ADD_TO_CART_BACKPACK).inner_text()
        logging.info(f"Add to cart text is visible for Sauce Labs Backpack: {addtocarttext}")
        assert addtocarttext == "Add to cart"

    except Exception as e:
        context.page.screenshot(path=f"./{new_file_name}")
        logging.info(f'Error occured at the "Add to cart" button should be visible for "Sauce Labs Backpack": {e}')
        raise
    
@then(u'add all products to the cart')
def step_impl(context):
    try:
        btn_locator = context.page.locator(Locators.InventoryPage.ADD_TO_CART_BUTTONS)
        count = btn_locator.count()

        for _ in range(count):
            btn_locator.first.scroll_into_view_if_needed()
            btn_id = btn_locator.first.get_attribute("id")
            xpath = f"//*[@id='{btn_id}']"
            logging.info(f"Clicking button with XPath: {xpath}")
            btn_locator.first.click()
            context.page.wait_for_timeout(500)  

            

        logging.info(f"{count} products added to cart")
    except Exception as e:
        context.page.screenshot(path=f"./{new_file_name}")
        logging.info(f'Error occured at the add all products to the cart: {e}')
        raise


@then(u'remove all products from the cart')
def step_impl(context):
    try:
        buttons = context.page.locator(Locators.InventoryPage.REMOVE_BUTTONS)
        count = buttons.count()

        for _ in range(count):
            buttons.first.click()

        logging.info(f"{count} products removed from cart")
        context.page.wait_for_timeout(500)  

        
    except Exception as e:
        context.page.screenshot(path=f"./{new_file_name}")
        logging.info(f'Error occured at the add all products to the cart: {e}')
        raise

@then(u'cart badge should not be visible')
def step_impl(context):
    try:
        context.page.wait_for_timeout(500)  

        badge = context.page.locator(Locators.Header.CART_BADGE)

        assert badge.count() == 0, "Cart is not empty (badge still visible)"

        logging.info("Cart is empty (no badge displayed)")
        
    except Exception as e:
        context.page.screenshot(path=f"./{new_file_name}")
        logging.info(f'Error occured at cart should be empty: {e}')
        raise