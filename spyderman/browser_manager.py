# browser_manager.py
from playwright.sync_api import sync_playwright

playwright = sync_playwright().start()
browser = playwright.chromium.launch(headless=False)
global_context = browser.new_context()


def create_new_context(**kwargs):
    return browser.new_context(**kwargs)


def get_page_html(
    url,
    context=global_context,
    wait_for_selector="body",
    timeout=60000,
    wait_for_selector_timeout=5000000,
):
    page = context.new_page()
    page.goto(url, timeout=timeout)
    page.wait_for_selector(wait_for_selector, timeout=wait_for_selector_timeout)
    html = page.content()
    page.close()
    return html


def close_browser():

    global_context.close()
    browser.close()
    playwright.stop()
