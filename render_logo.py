from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch()
    page = browser.new_page(viewport={"width": 1024, "height": 1024})
    page.goto("file:///workspace/logo.html")
    page.wait_for_timeout(2000)
    page.screenshot(path="/workspace/bihari_bites_logo.png", full_page=False)
    browser.close()
    print("Screenshot saved to logo_v3.png")
