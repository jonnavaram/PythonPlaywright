from behave import *
import os
import logging
from locators import Locators

current_file_name = os.path.basename(__file__)
new_file_name = os.path.splitext(current_file_name)[0] + ".png"


@then(u'click on the Twitter footer link')
def step_impl(context):
    try:
        with context.page.context.expect_page() as new_page_info:
            context.page.click(Locators.Footer.TWITTER_LINK)
        context.new_tab = new_page_info.value
        context.new_tab.wait_for_load_state("domcontentloaded", timeout=10000)
        logging.info(f"Twitter footer link opened: {context.new_tab.url}")

    except Exception as e:
        context.page.screenshot(path=f"./{new_file_name}")
        logging.error(f"Error at click on the Twitter footer link: {e}")
        raise


@then(u'click on the Facebook footer link')
def step_impl(context):
    try:
        with context.page.context.expect_page() as new_page_info:
            context.page.click(Locators.Footer.FACEBOOK_LINK)
        context.new_tab = new_page_info.value
        context.new_tab.wait_for_load_state("domcontentloaded", timeout=10000)
        logging.info(f"Facebook footer link opened: {context.new_tab.url}")

    except Exception as e:
        context.page.screenshot(path=f"./{new_file_name}")
        logging.error(f"Error at click on the Facebook footer link: {e}")
        raise


@then(u'click on the LinkedIn footer link')
def step_impl(context):
    try:
        with context.page.context.expect_page() as new_page_info:
            context.page.click(Locators.Footer.LINKEDIN_LINK)
        context.new_tab = new_page_info.value
        context.new_tab.wait_for_load_state("domcontentloaded", timeout=10000)
        logging.info(f"LinkedIn footer link opened: {context.new_tab.url}")

    except Exception as e:
        context.page.screenshot(path=f"./{new_file_name}")
        logging.error(f"Error at click on the LinkedIn footer link: {e}")
        raise


@then(u'the new tab URL should contain "twitter.com" or "x.com"')
def step_impl(context):
    try:
        current_url = context.new_tab.url
        assert "twitter.com" in current_url or "x.com" in current_url, \
            f"Expected URL to contain 'twitter.com' or 'x.com' but got '{current_url}'"
        logging.info(f"Twitter tab URL verified: {current_url}")

    except Exception as e:
        context.page.screenshot(path=f"./{new_file_name}")
        logging.error(f'Error at the new tab URL should contain "twitter.com" or "x.com": {e}')
        raise


@then(u'the new tab URL should contain "{domain}"')
def step_impl(context, domain):
    try:
        current_url = context.new_tab.url
        assert domain in current_url, \
            f"Expected URL to contain '{domain}' but got '{current_url}'"
        logging.info(f"New tab URL verified for '{domain}': {current_url}")

    except Exception as e:
        context.page.screenshot(path=f"./{new_file_name}")
        logging.error(f'Error at the new tab URL should contain "{domain}": {e}')
        raise


@then(u'the footer copyright text should contain "Sauce Labs"')
def step_impl(context):
    try:
        copyright_text = context.page.locator(Locators.Footer.COPYRIGHT).inner_text()
        assert "Sauce Labs" in copyright_text, \
            f"Expected copyright text to contain 'Sauce Labs' but got '{copyright_text}'"
        logging.info(f"Footer copyright text verified: '{copyright_text}'")

    except Exception as e:
        context.page.screenshot(path=f"./{new_file_name}")
        logging.error(f'Error at the footer copyright text should contain "Sauce Labs": {e}')
        raise
