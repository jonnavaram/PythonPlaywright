import logging
import os
from playwright.sync_api import sync_playwright

def before_scenario(context, scenario):
    context.playwright = sync_playwright().start()
    context.browser = context.playwright.chromium.launch(headless=False)
    context.page = context.browser.new_page()

def after_scenario(context, scenario):
    if hasattr(context, 'browser'):
        context.browser.close()
    if hasattr(context, 'playwright'):
        context.playwright.stop()

def before_feature(context, feature):
    # ✅ Get feature file path
    feature_filepath = os.path.abspath(feature.filename)

    # ✅ Get correct directory (feature folder)
    feature_dir = os.path.dirname(feature_filepath)

    # ✅ Get feature name
    feature_name = os.path.splitext(os.path.basename(feature_filepath))[0]

    # ✅ Create log & screenshot paths (same folder as feature)
    log_filename = os.path.join(feature_dir, f"{feature_name}.log")
    context.screenshot_name = os.path.join(feature_dir, f"{feature_name}.png")

    # ✅ Reset logger
    logger = logging.getLogger()
    logger.handlers.clear()

    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s - %(levelname)s - %(message)s",
        handlers=[
            logging.FileHandler(log_filename, mode='w'),  # overwrite each run
            logging.StreamHandler()
        ]
    )
