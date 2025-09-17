from playwright.sync_api import sync_playwright
def  run(playwright):
    # Launch Chrome (not just Chromium)
    browser = playwright.chromium.launch(
        headless=False,  # show the browser
        channel="chrome" # ensures Chrome is used
    )
    context = browser.new_context()
    page = context.new_page()

    # Go to Google
    page.goto("https://www.google.com")

    # Accept cookies popup if present (region-specific)
    try:
        page.click('button:has-text("I agree")', timeout=5000)
    except:
        print("No cookie popup found, continuing...")

    # Type search query
    page.fill('textarea[name="q"]', "Playwright automation tutorial")

    # Press Enter
    page.keyboard.press("Enter")

    # Wait for results
    page.wait_for_selector("#search")

    print("Search completed!")

    # Keep browser open for review
    # browser.close()

with sync_playwright() as playwright:
    run(playwright)