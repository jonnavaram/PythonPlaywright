from behave import *
import logging
import os
from locators import Locators


current_file_name = os.path.basename(__file__)
new_file_name = os.path.splitext(current_file_name)[0] + ".png"

@when(u'leave the username field empty')
def step_impl(context):
    try:
        context.page.fill(Locators.LoginPage.USERNAME, "")
        
    except Exception as e:
        context.page.screenshot(f"./{new_file_name}")
        logging.error(f"Error occured at leave the username field empty: {e}")
        raise
    
@then(u'leave the password field empty')
def step_impl(context):
    try:
        context.page.fill(Locators.LoginPage.PASSWORD, "")
        
    except Exception as e:
        context.page.screenshot(f"./{new_file_name}")
        logging.error(f"Error occured at leave the password field empty: {e}")
        raise
        

@then(u'verify the error icon at username')
def step_impl(context):
    try:
        locator = context.page.locator(Locators.LoginPage.ERROR_ICON_USERNAME)
        assert locator.is_visible(), "Error icon is not visible at username field"
        logging.info("Error icon is visible at username field")
        
    except Exception as e:
        context.page.screenshot(f"./{new_file_name}")
        logging.error(f"Error occured at verify the error icon at username: {e}")
        raise
        
@then(u'verify the error icon at password')
def step_impl(context):
    try:
        locator = context.page.locator(Locators.LoginPage.ERROR_ICON_PASSWORD)
        assert locator.is_visible(), "Error icon is not visible at password field"
        logging.info("Error icon is visible at password field")
        
    except Exception as e:
        context.page.screenshot(f"./{new_file_name}")
        logging.error(f"Error occured at verify the error icon at password: {e}")
        raise
    
@then(u'user should see the error "Sorry, this user has been locked out."')
def step_impl(context):
    try:
        errorlocator = context.page.locator(Locators.LoginPage.ERROR_MESSAGE)
        assert errorlocator.is_visible(),"Error message is not visible"
        logging.info("Error message is visible")
        
        #verify text
        err_text = errorlocator.text_content()
        logging.info(f"Error message is: {err_text}")
        assert err_text == "Epic sadface: Sorry, this user has been locked out.","Error message is not matched"
        logging.info("Error message is matched")
        
        
    except Exception as e:
        context.page.screenshot(f"./{new_file_name}")
        logging.error(f'Error occured at user should see the error "Sorry, this user has been locked out.": {e}')
        raise
    
@then(u'user should see an error message containing "Username and password do not match"')
def step_impl(context):
    try:
        errorlocator = context.page.locator(Locators.LoginPage.ERROR_MESSAGE)
        assert errorlocator.is_visible(),"Error message is not visible"
        logging.info("Error message is visible")
        
        #verify text
        err_text = errorlocator.text_content()
        logging.info(f"Error message is: {err_text}")
        
        assert err_text == "Epic sadface: Username and password do not match any user in this service","Error message is not matched"
        logging.info("Error message is matched")
        
    except Exception as e:
        context.page.screenshot(f"./{new_file_name}")
        logging.error(f'Error occured at user should see the error "Sorry, this user has been locked out.": {e}')
        raise
    
@then(u'user should see an error message containing "Username is required"')
def step_impl(context):
    try:
        errorlocator = context.page.locator(Locators.LoginPage.ERROR_MESSAGE)
        assert errorlocator.is_visible(),"Error message is not visible"
        logging.info("Error message is visible")
        
        #verify text
        err_text = errorlocator.text_content()
        logging.info(f"Error message is: {err_text}")
        
        assert err_text == "Epic sadface: Username is required","Error message is not matched"
        logging.info("Error message is matched")
        
        
    except Exception as e:
        context.page.screenshot(f"./{new_file_name}")
        logging.error(f'Error occured at user should see an error message containing "Username is required": {e}')
        raise
    
@then(u'user should see an error message containing "Password is required"')
def step_impl(context):
    try:
        errorlocator = context.page.locator(Locators.LoginPage.ERROR_MESSAGE)
        assert errorlocator.is_visible(),"Error message is not visible"
        logging.info("Error message is visible")
        
        #verify text
        err_text = errorlocator.text_content()
        logging.info(f"Error message is: {err_text}")
        
        assert err_text == "Epic sadface: Password is required","Error message is not matched"
        logging.info("Error message is matched")
        
        
    except Exception as e:
        context.page.screenshot(f"./{new_file_name}")
        logging.error(f'Error occured at user should see an error message containing "Password is required": {e}')
        raise    
        
        
