

from playwright.sync_api import sync_playwright

with sync_playwright() as playwright:
    browser = playwright.chromium.launch(headless=False)
    page = browser.new_page()
    page.goto('https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/login')

    input_email = page.get_by_test_id('login-form-email-input').locator('input')
    input_email.focus()

    for char in 'user@gmail.com':
        page.keyboard.type(char, delay=300)

    page.keyboard.press('ControlOrMeta+A')

    page.wait_for_timeout(3000)