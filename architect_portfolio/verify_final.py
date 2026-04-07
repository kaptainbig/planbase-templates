import asyncio
from playwright.async_api import async_playwright
import os

async def verify():
    async with async_playwright() as p:
        browser = await p.chromium.launch()
        page = await browser.new_page()

        # Test Logo Link
        path = os.path.abspath('about.html')
        await page.goto(f'file://{path}')
        await page.click('text="ARCHITECTS MONOLITH"')
        print(f"Clicked Logo on About, current url: {page.url}")

        # Test Mobile Menu
        await page.set_viewport_size({"width": 375, "height": 812})
        await page.reload()
        # Click menu toggle
        await page.click('.menu-toggle')
        # Check if mobile menu is visible (not translate-x-full)
        is_visible = await page.evaluate("() => !document.querySelector('#mobile-menu').classList.contains('translate-x-full')")
        print(f"Mobile menu visible: {is_visible}")
        await page.screenshot(path='mobile_menu.png')

        # Click a link in mobile menu
        await page.click('#mobile-menu a:text("Projects")')
        print(f"Clicked Projects in mobile menu, current url: {page.url}")

        await browser.close()

if __name__ == "__main__":
    asyncio.run(verify())
