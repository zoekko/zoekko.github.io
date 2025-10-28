from playwright.sync_api import sync_playwright

def run(playwright):
    browser = playwright.chromium.launch()
    page = browser.new_page()

    # Verify "About Me" page
    page.goto("http://127.0.0.1:4000/")
    page.screenshot(path="jules-scratch/verification/about_me.png")

    # Verify "Research" page
    page.goto("http://127.0.0.1:4000/research.html")
    page.screenshot(path="jules-scratch/verification/research.png")

    browser.close()

with sync_playwright() as playwright:
    run(playwright)
