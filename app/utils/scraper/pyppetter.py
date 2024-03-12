import asyncio
from pyppeteer import launch

async def main():
    print("Launching browser...")
    browser = await launch()
    print("Browser launched.")
    
    page = await browser.newPage()
    print("New page created.")
    
    await page.goto("https://www.python.org/")
    print("Page navigated.")
    
    await page.screenshot({"path": "python.png"})
    print("Screenshot taken.")
    
    await browser.close()
    print("Browser closed.")

print("Starting...")
asyncio.get_event_loop().run_until_complete(main())
print("Screenshot has been taken")
