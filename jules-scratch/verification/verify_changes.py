from playwright.sync_api import sync_playwright

def run():
    with sync_playwright() as p:
        browser = p.chromium.launch()
        page = browser.new_page()

        # Screenshot of the blog index page
        page.goto("file:///app/blog.md")
        page.screenshot(path="jules-scratch/verification/blog_index.png")

        # Screenshot of the blog post page
        page.goto("file:///app/blog/gps/gp-toy-example.html")
        page.screenshot(path="jules-scratch/verification/blog_post.png")

        browser.close()

run()
