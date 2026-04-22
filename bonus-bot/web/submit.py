from playwright.sync_api import sync_playwright
from config import WEB_URL

def submit_code(code):

    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()

        page.goto(WEB_URL)

        # enter code
        page.fill("#code_input", code)

        # submit
        page.click("#submit_button")

        # confirm popup (fixed position assumed)
        page.click("#confirm_button")

        print("Code submitted:", code)

        browser.close()