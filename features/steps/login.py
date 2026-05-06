from behave import *
import logging
import os
from locators import Locators

logging.basicConfig(level=logging.INFO)

current_file_name = os.path.basename(__file__)
new_file_name = os.path.splitext(current_file_name)[0] + ".png"

@given(u'I launch the browser')
def step_impl(context):
    try:
        logging.info("Browser launched successfully")
    
    except Exception as e:
        context.page.screenshot(f"./{new_file_name}")
        logging.error(f"Error occured at open the home page: {e}")
        raise
    
@when(u'open the home page')
def step_impl(context):
    try: 
        context.page.goto("https://www.saucedemo.com")
        logging.info("Opened home page")
        
    except Exception as e:
        context.page.screenshot(f"./{new_file_name}")
        logging.error(f"Error occured at open the home page: {e}")
        raise
        
@then(u'verify the title "Swag Labs"')
def step_impl(context):
    try:
        title = context.page.title()
        logging.info(f"Text from home screen is: {title}")
        assert "Swag Labs" in title
        logging.info("Title verified sucessfully")
            
    except Exception as e:
        context.page.screenshot(f"./{new_file_name}")
        logging.error(f'Error occured at verify the title "Swag Labs": {e}')
        raise


@then(u'Enter the username and password')
def step_impl(context):
    try:
        context.page.fill(Locators.LoginPage.USERNAME, "standard_user")
        context.page.fill(Locators.LoginPage.PASSWORD, "secret_sauce")
        logging.info("Successfully entered the username and password")
        
    except Exception as e:
        context.page.screenshot(f"./{new_file_name}")
        logging.error(f'Error occured at Enter the username and password: {e}')
        raise
    
@step(u'Enter the username "{username}"')
def step_impl(context, username):
    try:
        context.page.fill(Locators.LoginPage.USERNAME, username)

    except Exception as e:
        context.page.screenshot(f"./{new_file_name}")
        logging.error(f'Error occured at Enter the username: {e}')
        raise

@step(u'Enter the password "{password}"')
def step_impl(context, password):
    try:
        context.page.fill(Locators.LoginPage.PASSWORD, password)
        
        
    except Exception as e:
        context.page.screenshot(f"./{new_file_name}")
        logging.error(f'Error occured at Enter the password: {e}')
        raise
    
        
@then(u'click on the login button')
def step_impl(context):
    try:
        context.page.click(Locators.LoginPage.LOGIN_BUTTON)
        logging.info("Successfully clicked on login button")
        context.page.wait_for_timeout(500)  
        
    except Exception as e:
        context.page.screenshot(f"./{new_file_name}")
        logging.error(f'Error occured at click on the login button: {e}')
        raise
    
    
@then(u'user should be redirected to the main page')
def step_impl(context):
    try:
        mainpage = context.page.title()
        logging.info(f"User is redirected to {mainpage}")
        
        
    except Exception as e:
        context.page.screenshot(f"./{new_file_name}")
        logging.error(f'Error occured at user should be redirected to the main page: {e}')
        raise
        
@then(u'user should be redirected to the main page after a delay')
def step_impl(context):
    try:
        context.page.wait_for_timeout(3000)
        mainpage = context.page.title
        logging.info(f"User is redirected to {mainpage} after a delay")

    except Exception as e:
        context.page.screenshot(f"./{new_file_name}")
        logging.error(f'Error occured at user should be redirected to the main page after a delay: {e}')
        raise

@step(u'click on the hamburger')
def step_impl(context):
    try:
        context.page.click(Locators.Header.HAMBURGER_MENU)
        logging.info("Successfully clicked on hamburger button")
        
    except Exception as e:
        context.page.screenshot(f"./{new_file_name}")
        logging.error(f'Error occured at click on the hamburger: {e}')
        raise

@step(u'click on the logout button')
def step_impl(context):
    try:
        context.page.click(Locators.Header.LOGOUT_BUTTON)
        logging.info("Successfully clicked on logout button")
        
    except Exception as e:
        context.page.screenshot(f"./{new_file_name}")
        logging.error(f'Error at click on the logout button: {e}')
        raise

@step(u'close the browser')
def step_impl(context):
    logging.info("Browser will be closed after scenario")
